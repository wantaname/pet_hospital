import Vue from 'vue'
import VCharts from "v-charts"
Vue.use(VCharts)
import App from './App.vue'
import router from './router'
import myconfig from "@/myconfig";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
import VueParticles from 'vue-particles'  
Vue.use(VueParticles) 
// 导入全局样式表
import './assets/css/global.css'
import axios from 'axios'

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
