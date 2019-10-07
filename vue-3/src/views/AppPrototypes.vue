<template>
 <div>
    <h1>App Prototypes</h1>
    <div>
      <h2>API Prototypes</h2>

      <div v-if="apiMessage">

        <h3>Pagination</h3>

        <p class="mt-3">Current Page: {{ msgPage }}</p>

        <b-table
            id="my-table"
            :items="msgItems"
            small>
        </b-table>

        <b-pagination
            @input="getMessages(msgPage)"
            v-model="msgPage"
            :total-rows="msgTotal"
            :per-page="msgPerPage"
            aria-controls="my-table">
        </b-pagination>

        <div v-if="message">
           {{ message.value }}
        </div>
      </div>
      </div>

      <hr />


      <div>
         <h2>Get</h2>
         <p>Ping the apps API by clicking the buttons below.<br />
           <button @click="getNoAuth">Get private list w/o required auth_access</button>
           <button @click="getMessages">Get private list required auth_access</button>
         </p>
        <h2>Result</h2>
        <p>{{ apiMessage }}</p>
        <code>{{getResponse}}</code>
      </div>

    <hr />

    <div>
       <h2> Post test </h2>
       <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
       <button @click="postMessage">Post Message</button>
       <h2>Result</h2>
       <p>{{ apiMessage }}</p>
       <code>{{postResponse}}</code>
    </div>

    <div v-if="message.uuid">
       <h2>Put test </h2>
       <b-form-input v-model="message.value" placeholder="Enter test value"></b-form-input>
       <button @click="putMessage">Post Message</button>
       <h2>Result</h2>
       <p>{{ apiMessage }}</p>
       <code>{{putResponse}}</code>
       <p></p>
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
      response: null,
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
    async getMessages() {
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
        this.getResponse = data;
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
        this.postResponse = data;
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
        this.putResponse = data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    }
  },
  mounted(){
    this.getMessages()
  }
};
</script>
