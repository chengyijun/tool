<template>
    <div>
        <input type="file" @change="getFiles">
        <input type="button" value="上传" @click="upload">
        {{message}}
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Test",
        data() {
            return {
                formData: null,
                message: null
            }
        },
        methods: {
            getFiles(event) {
                console.log(event.target.files);
                let files = event.target.files
                this.formData = new FormData()
                this.formData.append('file', files[0])
            },

            upload(event) {
                axios({
                    method: 'post',
                    url: '/api/test/',
                    data: this.formData
                }).then(msg => {
                    console.log(msg.data)
                    this.message = msg.data.message
                }).catch(err => {
                    console.log(err)
                })
            }
        }
    }
</script>

<style>

</style>