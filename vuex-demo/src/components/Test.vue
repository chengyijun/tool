<template>
    <div>
        {{$store.state.counter}}
        {{$store.getters.powerCounter}}
        {{$store.state.a.name}}
        {{$store.state.token}}
        <button @click="countPlus(5)">+</button>
        <button @click="login">登录</button>

        <button @click="getProfile">获取档案</button>


    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Test",
        data() {
            return {}
        },
        methods: {
            getProfile() {
                axios({
                    method: 'get',
                    headers: {
                        "Authorization": this.$store.state.token
                    },
                    url: '/api/profile/'
                }).then(res => {
                    console.log(res.data);
                }).catch(err => {
                    console.log(err);
                })
            },
            login() {
                axios({
                    method: 'post',
                    url: '/api/login/',
                    data: {
                        username: 'abel',
                        password: '123'
                    }
                }).then(res => {
                    console.log(res.data);
                    // {code: 1, mesage: "登录成功！", token: "e5d5e19c59ec468a8db8e59426954d24", username: "abel"}
                    // 将token写入到store中
                    // this.$store.state.token = res.data.token
                    this.$store.dispatch('aSetToken', {
                        token: res.data.token
                    })
                    console.log('将token写入到store中')
                }).catch(err => {
                    console.log(err);
                })
            },
            countPlus(x) {
                // console.log(x)
                // this.$store.commit('countPlus', x)
                /*
                this.$store.commit({
                    type: 'countPlus',
                    x: x
                })
                */
                // this.$store.dispatch('aCountPlus', x)
                this.$store.dispatch('aCountPlus', {x: x}).then(res => {
                    console.log(res)
                })

            }
        }
    }
</script>

<style>

</style>