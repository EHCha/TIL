<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData"/>
    <div>appParentData: {{appParentData}}</div>
    <div>appChildData: {{appChildData}}</div>
    <hr>
    <AppParent :app-data="appData" @send-parent-data="getParentData" @send-child-data-to-app="getChildData"/>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  data: function() {
    return {
      appParentData: null,
      appChildData: null,
      appData: null,
    }
  },


  components: {
    AppParent,
  },
  methods: {
    getChildData: function(child2) {
      this.appChildData = child2
    },
    getParentData: function(parent) {
      this.appParentData = parent
    },
  }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
