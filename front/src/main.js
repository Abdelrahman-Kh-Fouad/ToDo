import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookies from 'vue3-cookies';

createApp(App).use(VueCookies).use(router).use(VueAxios, axios ).mount('#app')

