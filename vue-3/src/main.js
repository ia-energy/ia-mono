import Vue from 'vue'
import AuthPlugin from "./plugins/auth";
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router';


Vue.use(AuthPlugin);

Vue.config.productionTip = false

new Vue({
  router, 
  render: h => h(App),
}).$mount('#app')
