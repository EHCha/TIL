<template>
    <div>
    <h1>AppChild</h1>
    <input type="text" v-model="appChildData" @input="sendChildData">
    <div>appData: {{ appData }}</div>
    <div>appParentData: {{ appParentData }}</div>
    <div>appChildData: {{ appChildData }}</div>
    </div>
</template>

<script>
export default {
    name: 'AppChild',
    props: {
        appData: {
            type: String,
        },
        appParentData:{
            type: String,
        }
    },
    data: function() {
        return {
            appChildData: null,
        }
    },
    methods: {
        sendChildData: function() {
            this.$emit('send-child-data', this.appChildData)
        }
    }
}
</script>

<style>

</style>