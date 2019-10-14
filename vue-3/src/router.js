// src/router.js

import Vue from 'vue';
import Router from 'vue-router';
import Callback from './components/Callback';
import Profile from "./views/Profile.vue";
import Index from "./views/Index.vue";
import AppPrototypesView from "./views/AppPrototypes.vue";
import auth from "./auth/authService";

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/callback',
    name: 'callback',
    component: Callback
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
  },
  {
      path: "/app-prototypes",
      name: "app-prototypes",
      component: AppPrototypesView,
  },
];

const router = new Router({
  mode: 'history',
  routes
});

router.beforeEach((to, from, next) => {
  if (to.path === "/" || to.path === "/callback" || auth.isAuthenticated()) {
    return next();
  }

  // Specify the current path as the customState parameter, meaning it
  // will be returned to the application after auth
  auth.login({ target: to.path });
});

export default router;
