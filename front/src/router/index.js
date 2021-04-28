import Vue from 'vue'
import VueRouter from 'vue-router'
// 导入组件
import home from "@/components/home";
import introduction from '../components/overview/introduction.vue'
import cosplay from "@/components/cosplay/cosplay";
import _case from "@/components/case/case";
import receive from "@/components/receive/receive";
import inspect from "@/components/inspect/inspect";
import result from "@/components/result/result";
import cure from "@/components/cure/cure";
import administrator from "@/components/administrator/administrator";
import user from "@/components/user/user";
import question from "@/components/question/question";
import exam_subject from "@/components/exam_subject/exam_subject";
import score_analysis from "@/components/score_analysis/score_analysis";
import image from "@/components/image/image";
import video from "@/components/video/video";
import user_exam from "@/components/user_exam/user_exam";
import test from "@/components/test/test";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: home,
    redirect: '/introduction',

    
    children: [
      {path:'/introduction',component:introduction},
      {path:"/cosplay",component: cosplay},
      {path: "/case",component: _case},
      {path: "/receive",component: receive},
      {path: "/inspect",component: inspect},
      {path: "/result",component: result},
      {path: "/cure",component: cure},
      {path: "/administrator",component: administrator},
      {path: "/user",component: user},
      {path: "/question",component: question},
      {path: "/exam_subject",component: exam_subject},
      {path: "/user_exam",component: user_exam},
      {path: "/score_analysis",component: score_analysis},
      {path:"/image",component: image},
      {path:"/video",component: video}

    ]
  },
  {
    path:"/test",component: test
  }

  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  routes
})

//挂载路由导航守卫

export default router
