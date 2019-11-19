<template>
  <div class="wrap">
    <div class="edit">
      <textarea rows="10" cols="100" class="editor"></textarea>
    </div>
  </div>
</template>
<script>
  export default{
    name:'bookedit',
    data(){
      return{
      }
    }
  }
</script>

<style>
  .mark{width: 800px; height: 400px; margin: 0 auto;}
  .edit,.show{float: right; width: 395px; height: 400px; border: 1px soild #666;}
</style>
