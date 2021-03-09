import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    // 状态变量
    state: {
        counter: 13,
        token: null
    },
    // 状态改变 封装了改变状态变量的操作方法
    mutations: {
        setToken(state, payload) {
            state.token = payload.token
        },
        /*
        countPlus(state, x) {
            console.log('abel', x)
            state.counter += x
        }
       */
        countPlus(state, payload) {
            console.log(payload.x)
            state.counter += payload.x
        }
    },
    // 状态改变 （异步）  action也只能操作mutations进行提交
    actions: {
        aSetToken(context, payload) {
            context.commit('setToken', payload)
        },
        // aCountPlus(context, payload) {
        //     setTimeout(() => {
        //         context.commit('countPlus', payload)
        //     }, 1000)
        // }
        aCountPlus(context, payload) {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    context.commit('countPlus', payload)
                    resolve('里面完事了')
                }, 1000)
            })
        }
    },
    // 计算属性
    getters: {
        powerCounter(state) {
            return state.counter * state.counter
        }
    },
    // 分模块
    modules: {
        a: {
            state: {
                name: 'abeltest'
            },
            mutations: {},
            actions: {},
            getters: {}
        },
        b: {
            state: {
                name: 'tank'
            },
            mutations: {},
            actions: {},
            getters: {}
        }

    }
})
