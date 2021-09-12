import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
import register from '../views/register.vue'
import github from "@/views/github";
import todo from "@/views/todo";

const routes = [
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/register',
    name: 'register',
    component : register
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
  ,{
    path : '/github',
    name : 'github',
    component: github
  }
  ,{
    path : '/todo',
    name : 'todo',
    component: todo
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
