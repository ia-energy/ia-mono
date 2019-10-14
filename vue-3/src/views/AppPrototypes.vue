<template>
  <div  class="container">

    <div class="row">
      <h1>App Prototypes</h1>
    </div>

    <div v-if="pagi.apiMessage" class="row">

      <div class="col">
        <h3>API Pagination</h3>
      </div>

      <div class="col-10">
        <p class="mt-3">Current Page: {{ pagi.msgPage }}</p>

        <b-table
            id="my-table"
            :items="pagi.msgItems"
            small>
        </b-table>

        <b-pagination
            @input="getMessages(pagi.msgPage)"
            v-model="pagi.msgPage"
            :total-rows="pagi.msgTotal"
            :per-page="pagi.msgPerPage"
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
           <b-form-input v-model="get.uuid" placeholder="Enter uuid"></b-form-input>
           <button @click="getNoAuth">Get message w/o auth_access</button>
           <button @click="getMessage">Get message w/auth_access</button>
         </p>
        <p>{{ get.apiMessage }}</p>
        <code>{{ get.data }}</code>
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
       <p>{{ post.apiMessage }}</p>
       <code>{{ post.data }}</code>
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
          <p>{{ put.apiMessage }}</p>
          <code>{{ put.data }}</code>
          <p></p>
       </div>
    </div>

    <div class="row">
      <div class="col">
         <h2>Sample Chart</h2>
      </div>
      <div class="col-10">
         <PackChart :tweetData='sampleTweetData' />
      </div>
    </div>
</div>

</template>

<script>
import axios from 'axios';
import * as d3 from "d3";
import PackChart from "../components/SampleChart.vue";

export default {
  name: "Api",
  components: {
    PackChart
  },
  data() {
    return {

      pagi: {
        msgPage: 1,
        msgPerPage: 2,
        msgItems: null,
        msgTotal: null,
        apiMessage: null,
      },
      get: {
         data: null,
         apiMessage: null,
         uuid: null,
      },
      post: {
         data: null,
         apiMessage: null
      },
      put: {
         data: null,
         apiMessage: null
      },
      message: {uuid:'', value:'test' + (new Date()).getTime()},
      sampleTweetData: [],
    };
  },
  methods: {
    async getNoAuth() {
      try {
        const { data } = await axios.get("/api/1/test_messages/" + this.uuid , {
        });
        this.get.apiMessage = 'Got 200 with data';
        this.get.data = data;
        console.log(data);
      } catch (e) {
        this.get.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`;
        this.get.data = null;
      }
    },
    async getMessages() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/1/test_messages/?perPage=" + this.pagi.msgPerPage + "&page=" + this.pagi.msgPage, {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.pagi.apiMessage = 'Got 200 with data';
        this.pagi.msgItems = data.items;
        this.pagi.msgTotal = data.total;
        if (this.uuid == null)
          if (data.items != undefined)
            if (data.items[0] != undefined)
              this.get.uuid = data.items[0].uuid;
        console.log(data);
      } catch (e) {
        this.pagi.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`; }
    },
    async getMessage() {
      const accessToken = await this.$auth.getAccessToken();

      try {
        const { data } = await axios.get("/api/1/test_messages/" + this.get.uuid , {
          headers: {
            Authorization: `Bearer ${accessToken}`
          }
        });
        this.get.apiMessage = 'Got 200 with data';
        this.get.data = data;
      } catch (e) {
        this.get.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`;
        this.get.data = null;
      }
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
        this.post.apiMessage = 'Got 200 with data';
        this.message =  data;
        this.post.data = data;
        console.log(data);
      } catch (e) {
        this.post.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`;
        this.post.data = null;
      }
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
        this.put.apiMessage = 'Got 200 with data';
        this.message =  data;
        this.put.data = data;
        console.log(data);
      } catch (e) {
        this.put.apiMessage = `Error: the server responded with '${ e.response.status }: ${e.response.statusText}'`;
        this.put.data = null;
      }
    },
    async fetchSampleTweets() {
      let data = await d3.json("./tweets_sample.json");
      this.sampleTweetData = data;
    }
  },
  mounted(){
    this.getMessages();
    this.fetchSampleTweets();
  }
};
</script>
