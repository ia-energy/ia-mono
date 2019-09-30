<template>
 <div>
    <div>
      <h1>External API Test</h1>
      <p>Ping an external API by clicking the button below. This will call the external API using an access token, and the API will validate it using
        the API's audience value.
      </p>
      <button @click="callPublicList">Get public list </button>
      <button @click="callPrivateList">Get private list w/o required auth_access</button>
      <button @click="callPrivateWAuth">Get private list w/o required auth_access</button>
    </div>

    <div v-if="apiMessage">
      <h2>Result</h2>
      <p>{{ apiMessage }}</p>
    </div>

    <div v-for="message in messages"  v-bind:key="message.id">
       {{ message.value }}
    </div>

 </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Api",
  data() {
    return {
      apiMessage: null,
      messages: null
    };
  },
  methods: {
    async callPublicList() {

      try {
        const { data } = await axios.get("/api/1/test/no_auth_access/", {});
        this.apiMessage = 'Got 200 with data';
        this.messages = data
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async callPrivateList() {
      try {
        const { data } = await axios.get("/api/1/test/auth_access/", {});
        this.apiMessage = 'Got 200 with data';
        this.messages = data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
        this.messages = null;
    },
    async callPrivateWAuth() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/1/test/auth_access/", {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.apiMessage = 'Got 200 with data';
        this.messages = data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    }
  }
};
</script>
