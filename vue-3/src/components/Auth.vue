<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">IA.energy</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
         <b-navbar-nav>
            <b-nav-item :to="{ path: '/' }">Home</b-nav-item>
            <b-nav-item :to="{ path: '/external-api' }">External API</b-nav-item>
         </b-navbar-nav>

         <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown text="User" right>
               <b-dropdown-item :to="{ path: '/' }">Home</b-dropdown-item>
               <b-dropdown-item href="#" v-if="!isAuthenticated" @click.prevent="login">Login</b-dropdown-item>
               <b-dropdown-item v-if="isAuthenticated" :to="{ path: '/profile' }">Profile</b-dropdown-item>
               <b-dropdown-item href="#" v-if="isAuthenticated" @click.prevent="logout">Log out</b-dropdown-item>
            </b-nav-item-dropdown>
         </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div>
      <router-view></router-view>
    </div>
  </div>


</template>

<script>
export default {
  name: "Auth",
  data() {
    return {
      isAuthenticated: false
    };
  },
  async created() {
    try {
      await this.$auth.renewTokens();
    } catch (e) {
      console.log(e);
    }
  },
  methods: {
    login() {
      this.$auth.login({ target: this.$route.query.page });
    },
    logout() {
      this.$auth.logOut();
    },
    handleLoginEvent(data) {
      this.isAuthenticated = data.loggedIn;
      this.profile = data.profile;
    }
  }
};
</script>
