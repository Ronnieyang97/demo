<template>
  <div id="app">
    <navi></navi>

    <router-view/>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import navi from './components/navi'
export default {
  name: 'App',
  components: {navi}
}
</script>

<style>

</style>
