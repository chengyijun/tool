import {createRouter, createWebHistory} from 'vue-router'import Home from '../views/Home.vue'const routes = [    {        path: '/',        name: 'Home',        meta: {            title: '首页2'        },        component: Home,        // 路由的独享守卫 当进入该路由的时候被调用        // beforeEnter: (to, from, next) => {        //     console.log('从主页跳转走之前被调用');        //     console.log('to', to)        //     console.log('from', from)        //     // to: 即将跳转到的目标页面        //     // from: 当前页面        //     // document.title = to.matched[0].meta.title        //     next()        // }    },    {        path: '/about',        name: 'About',        meta: {            title: '关于2'        },        // route level code-splitting        // this generates a separate chunk (about.[hash].js) for this route        // which is lazy-loaded when the route is visited.        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')    }]const router = createRouter({    history: createWebHistory(process.env.BASE_URL),    routes})// 导航守卫// 其实就是一个hook 回调函数 当router跳转时候 调用该函数// router.beforeEach((to, from, next) => {//     console.log('to', to)//     console.log('from', from)//     // to: 即将跳转到的目标页面//     // from: 当前页面//     document.title = to.matched[0].meta.title////     next()// })export default router