<template>
  <div  class="container">

    <div class="row">
      <h1>App Prototypes</h1>
    </div>

    <div v-if="apiMessage" class="row">
      <div class="col">
        <h3>API Pagination</h3>
      </div>
      <div class="col-10">
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

    <div class="row">
      <div class="col">
         <h2>API Get</h2>
      </div>
      <div class="col-10">
         <p>Ping the apps API by clicking the buttons below.<br />
           <b-form-input v-model="uuid" placeholder="Enter uuid"></b-form-input>
           <button @click="getNoAuth">Get message w/o auth_access</button>
           <button @click="getMessage">Get message w/auth_access</button>
         </p>
        <h2>Result</h2>
        <p>{{ apiMessage }}</p>
        <code>{{getResponse}}</code>
      </div>
    </div>


    <div class="row">
      <div class="col">
       <h2>API Post test </h2>
     </div>
     <div class="col-10">
       <b-form-input v-model="message.value" placeholder="Enter test value">
       </b-form-input>
       <button @click="postMessage">Post Message</button>
       <h2>Result</h2>
       <p>{{ apiMessage }}</p>
       <code>{{postResponse}}</code>
     </div>
    </div>

    <div v-if="message.uuid" class="row">
      <div class="col">
       <h2>API Put test </h2>
     </div>
     <div class="col-10">
       <b-form-input v-model="message.value" placeholder="Enter test value">
       </b-form-input>
       <button @click="putMessage">Post Message</button>
       <h2>Result</h2>
       <p>{{ apiMessage }}</p>
       <code>{{putResponse}}</code>
       <p></p>
     </div>
    </div>

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
      getResponse: null,
      postResponse: null,
      puttResponse: null,
      uuid: null,
      message: {uuid:'', value:'test' + (new Date()).getTime()},
    };
  },
  methods: {
    async getNoAuth() {
      try {
        const { data } = await axios.get("/api/1/test_messages/" + this.uuid , {
        });
        this.apiMessage = 'Got 200 with data';
        this.getResponse = data;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
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
        this.msgTotal = data.total;
        if (this.uuid == null)
          if (data.items != undefined)
            if (data.items[0] != undefined)
              this.uuid = data.items[0].uuid;
        console.log(data);
      } catch (e) {
        this.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async getMessage() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/1/test_messages/" + this.uuid , {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.apiMessage = 'Got 200 with data';
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
