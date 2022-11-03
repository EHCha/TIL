<template>
  <div id="app">
    <TheLunch @lunch-send="getMenu"/>
    
    <TheLotto v-if="lunchMenu" :lunch-menu="lunchMenu"/>
    <!-- v-if="lunchMenu가 True 일때" -->
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch.vue'
import TheLotto from './components/TheLotto.vue'


export default {
  name: 'App',
  data: function() {
    return {
      lunchMenu: null
    }
  },

  components: {
    TheLotto,
    TheLunch,
  },

  methods: {
    getMenu: function(lunch) {
      this.lunchMenu = lunch
      console.log(lunch)
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
