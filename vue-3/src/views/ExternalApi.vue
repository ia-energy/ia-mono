<template>
 <div>
    <div>
      <h1>External API</h1>
      <p>Ping an external API by clicking the button below. This will call the external API using an access token, and the API will validate it using
        the API's audience value.
      </p>
      <button @click="callApi">Ping API</button>
      <button @click="callApiPrivate">Ping API Private</button>
      <button @click="callApiPrivateScoped">Ping API Private Scoped</button>
    </div>

    <div v-if="apiMessage">
      <h2>Result</h2>
      <p>{{ apiMessage }}</p>
    </div>

 </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Api",
  data() {
    return {
      apiMessage: null
    };
  },
  methods: {
    async callApi() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/public", {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });

        this.apiMessage = data.message;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async callApiPrivate() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/private", {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });

        this.apiMessage = data.message;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async callApiPrivateScoped() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/private-scoped", {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });

        this.apiMessage = data.message;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    }
  }
};
</script>
