<template>
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Book</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li v-for="(item,index) in routes" :class="{active:index==trigger}"  @click="trig(index)">
          <router-link :to="item.url">
            {{item.title}}
          </router-link></li>
      </ul>
      <form class="navbar-form navbar-right">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
</template>

<script>
  export default{
      name:'navi',
      data(){
          return{
              routes:[
                {url:'/#', title:'首页'},
                {url:'/mybook', title:'搜索'}
              ],
              trigger:0

          }
      },
      methods:{
        trig(index){
          this.trigger = index
        }
      },
      created(){
        for(var i=0;i < this.routes.length;i++){
          if(this.routes[i].url == this.$route.path){
            this.trigger = i;
            return 0;
          }
        }
      }
  }
</script>
<style scoped>

</style>
