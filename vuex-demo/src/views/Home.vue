<template>
    <div class="home">
        <test></test>
    </div>
</template>

<script>
    // @ is an alias to /src
    import Test from '/src/components/Test'

    export default {
        name: 'home',
        components: {
            Test
        }
    }
</script>
