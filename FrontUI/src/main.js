<<<<<<< HEAD
import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
=======
import { createApp } from 'vue'
import './style.scss'
import App from './App.vue'
import router from './router/';  
createApp(App).use(router).mount('#app')
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
