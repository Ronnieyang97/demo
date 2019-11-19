<template>
  <div id="app">
    <navi></navi>

    <router-view/>
  </div>
</template>

<script>
import 'jquery/dist/jquery.js'

import 'bootstrap/dist/css/bootstrap.css'


import navi from './components/navi'
export default {
  name: 'App',
  components: {navi}
}
</script>



<style>

</style>
