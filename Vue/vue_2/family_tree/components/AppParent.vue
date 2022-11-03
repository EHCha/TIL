<template>
    <div>
    
    <h1>AppParent</h1>
    <input type="text" v-model="appParentData" @input="sendParentData" />
    <div>appData: {{appData}}</div>
    
    <div>appChildData: {{upChildData}}</div>
    <hr>
    <AppChild :app-data="appData" 
    :app-parent-data="appParentData" 
    @send-child-data="getChild"
    />
    
    </div>
</template>



<script>
import AppChild from './AppChild.vue'

export default {
    name: 'AppParent',
    props: {
        appData:{
            type: String,
        }
    },
    components:{
        AppChild
    },
    data: function() {
        return {
            appParentData: null,
            upChildData: null,
        }
    },
    methods: {
        // getAppData: function(appData) {
        //     this.appParentData = appData
        // },
        getChild: function(child) {
            this.upChildData = child
            this.$emit('send-child-data-to-app', this.upChildData)
        },
        sendParentData: function() {
            this.$emit('send-parent-data', this.appParentData)
        }
    }
}
</script>

<style>

</style>