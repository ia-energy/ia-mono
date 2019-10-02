<template>
 <div>
    <div>
      <h1>External API Test</h1>

      <div v-if="apiMessage">
        <h2>Result</h2>
        <p>{{ apiMessage }}</p>

        <!-- fix below: https://www.thetechieshouse.com/vue-js-pagination-example-with-bootstrap-server-side-pagination/ -->
        <b-pagination
            @input="getMessages(msgPage)"
            v-model="msgPage"
            :total-rows="msgTotal"
            :per-page="msgPerPage"
            aria-controls="my-table">
        </b-pagination>

        <p class="mt-3">Current Page: {{ msgPage }}</p>

        <b-table
            id="my-table"
            :items="msgItems"
            small>
        </b-table>

        <div v-if="message">
           {{ message.value }}
        </div>
      </div>

      <h2>Get test</h2>
      <p>Ping an external API by clicking the button below. This will call the external API using an access token, and the API will validate it using
        the API's audience value.
      </p>
      <button @click="getNoAuth">Get private list w/o required auth_access</button>
      <button @click="getMessages">Get private list required auth_access</button>
    </div>

    <h2> Post test </h2>
    <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
    <button @click="postMessage">Post Message</button>

    <div v-if="message.uuid">
       <h2>Put test </h2>
       <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
       <button @click="putMessage">Post Message</button>
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
      msgPage: 1,
      msgPerPage: 2,
      msgItems: null,
      msgTotal: null,
      message: {uuid:'', value:'test' + (new Date()).getTime()},
    };
  },
  methods: {
    async getNoAuth() {
      try {
        const { data } = await axios.get("/api/1/test_messages/", {});
        this.apiMessage = 'Got 200 with data';
        this.pageList = data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
        this.messages = null;
    },
    async getMessages(page) {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/1/test_messages/?perPage=" + this.msgPerPage + "&page=" + this.msgPage, {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.apiMessage = 'Got 200 with data';
        this.msgItems = data.items;
        this.msgTotal = data.total
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async postMessage() {
      const accessToken = await this.$auth.getAccessToken();
      const json = this.message

      try {
        const { data } =  await axios.post("/api/1/test_messages/",
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
    async putMessage() {
      const accessToken = await this.$auth.getAccessToken();
      const json = this.message

      try {
        const { data } =  await axios.put("/api/1/test_messages/"+json['uuid'],
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
  },
  mounted(msgPage){
    this.getMessages(msgPage)
  }
};
</script>
