import Vue from 'vue'
import VueRouter from 'vue-router'
// 导入组件
import Home from '../components/home/home.vue'
import account from '../components/account/account.vue'
import login from '../components/login/login'
import overview from "@/components/overview/overview";
import qiantai from "@/components/qiantai/qiantai";
import yizhu from "@/components/yizhu/yizhu";
import yishi from "@/components/yishi/yishi";
import _case from "@/components/case/case";
import exam from "@/components/exam/exam";
import {use} from "element-ui/src/locale";
import userInfo from "@/components/account/userInfo";
import examInfo from "@/components/account/examInfo";
import examDetail from "@/components/examDetail/examDetail";
import score_analysis from "@/components/scoreAnalysis/score_analysis";
/**
 * 重写路由的push方法
 */
const routerPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return routerPush.call(this, location).catch(error => error)
}


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        redirect: '/overview',
        children: [

            {
                path: '/account', component: account, children: [
                    {path: '/userInfo', component:userInfo },
                    {path: '/examInfo', component:examInfo },
                    {path: "/scoreAnalysis",component: score_analysis}

                ],
                redirect: '/userInfo'
            },
            {path: '/overview', component: overview},
            {path: '/qiantai', component: qiantai},
            {path: '/yizhu', component: yizhu},
            {path: '/yishi', component: yishi},
            {path: "/case", component: _case},
            {path: "/exam", component: exam},
            {path: "/examDetail", component: examDetail,name:"examDetail"}
            // {
            //   path: "/api",component: api
            // }


        ]
    },
    {
        path: '/login',
        name: 'login',
        component: login,
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


// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        window.localStorage.clear()
        return next()
    } else {
        return next()
    }
})
export default router
