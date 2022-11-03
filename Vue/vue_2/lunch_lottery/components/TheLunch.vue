<template>

<div>

<h1> 점심 메뉴</h1>
<button @click="pickLunchMenu">Pick One</button>
<p> {{ lunch }} </p>
<hr>

</div>

</template>

<script>
import _ from 'lodash'

export default {
    name: 'MyLunch',
    data: function () {
        return {
            luncharr: ["짜장면","국밥","햄버거"],
            lunch: null
        }
    },
    methods: {
        pickLunchMenu: function() {
            this.lunch=_.sample(this.luncharr)
            this.$emit('lunch-send', this.lunch)
        },
    }
}
</script>

<style>

</style>