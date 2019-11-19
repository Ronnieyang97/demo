<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h5 class="panel-title">books</h5>
          </div>
          <div class="panel-body">
            <bookshow></bookshow>
          </div>
        </div>
      </div>
      <div class="col-md-7">
          <div class="panel-body">
            <bookedit></bookedit>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
  import bookshow from './bookshow'
  import bookedit from './bookedit'
  export default{
      name:'mybook',
      data(){
          return{
          }
      },
      components:{
        bookshow,
        bookedit
      }
  }
</script>
<style scoped>

</style>
