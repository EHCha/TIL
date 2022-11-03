<template>
    <div>
    <h1>{{ lunchMenu }} 먹고 로또</h1>
    
    <button @click="getLottoNumber">Get Lucky Numbers</button>
    <br>
    
    <p> {{ number }}</p>
    </div>
</template>

<script>

import _ from 'lodash'

export default {
    name: 'MyLotto',
    props: {
        lunchMenu:{
            type: String,
            default: '',
        } 
    },
    data: function () {
        return {
            number: ''
        }
    },
    methods: {
        getLottoNumber: function() {
            // const numbers = _.range(1, 46)
            // this.number = _.sampleSize(numbers, 6)
            this.number= _.sampleSize(_.range(1, 46), 6)
            }
        }
    }

</script>

<style>

</style>