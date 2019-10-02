<template>
 <div>
    <div>
      <h1>External API Test</h1>

      <div v-if="apiMessage">
        <h2>Result</h2>
        <p>{{ apiMessage }}</p>
        <div v-if="messages">
           <div v-for="message in messages" v-bind:key="message.public_id">
              {{ message.value }}
           </div>
        </div>
        <div v-if="message">
           {{ message.value }}
        </div>
      </div>

      <h2>Get test</h2>
      <p>Ping an external API by clicking the button below. This will call the external API using an access token, and the API will validate it using
        the API's audience value.
      </p>
      <button @click="callPublicList">Get public list </button>
      <button @click="callPrivateList">Get private list w/o required auth_access</button>
      <button @click="callPrivateWAuth">Get private list w/o required auth_access</button>
    </div>

    <h2> Post test </h2>
    <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
    <button @click="callPostMessage">Post Message</button>

    <div v-if="message.public_id">
       <h2>Put test </h2>
       <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
       <button @click="callPutMessage">Post Message</button>
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
      messages: null,
      message: {public_id:'', value:'test' + (new Date()).getTime()},
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
    },
    async callPostMessage() {
      const accessToken = await this.$auth.getAccessToken();
      const json = this.message

      try {
        const { data } =  await axios.post("/api/1/test/auth_access/",
        json,
         {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.apiMessage = 'Got 200 with data';
        this.message =  data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async callPutMessage() {
      const accessToken = await this.$auth.getAccessToken();
      const json = this.message

      try {
        const { data } =  await axios.put("/api/1/test/auth_access/"+json['public_id'],
        json,
         {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.apiMessage = 'Got 200 with data';
        this.message =  data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    }
  }
};
</script>
