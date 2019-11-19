<template>
  <div class="input-group">
    <input type="text" class="form-control" placeholder="condition" aria-describedby="condition">
    <div class="btn-group" role="group" aria-label="...">
      <button type="button" class="btn btn-default">title</button>
      <button type="button" class="btn btn-default">author</button>
      <button type="button" class="btn btn-default">type</button>
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
  .editor{width: 200; height: 200px; border: 1px soild #666;}
</style>
