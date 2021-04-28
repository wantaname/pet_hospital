import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import VueParticles from 'vue-particles'
import myconfig from "@/myconfig";
Vue.use(VueParticles)

// 导入全局样式表
import './assets/css/global.css'
import axios from 'axios'

import qs from 'qs';
Vue.prototype.$qs = qs;
// baseurl
// axios.defaults.baseURL='http://127.0.0.1:5000/'
axios.defaults.baseURL =myconfig.baseURL

// 请求拦截器，加上token
axios.interceptors.request.use(config => {
  config.headers.Authorization = window.localStorage.getItem('token') //设置响应头

  return config
}, err => {
  console.log(err)
})
//挂载到Vue的原型对象上
Vue.prototype.$http=axios
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
