<template>
  <div id="nav">
    <!--<router-link to="/login">Login</router-link> | <router-link to="/register">Register</router-link>-->
  </div>
  <router-view/>
</template>


<script>
  export default {

    data:function (){
      return{



        state :''
      }
    },
    created(){
      if (window.localStorage.getItem('state')!=null)
        this.state = window.localStorage.getItem('state');


      console.log(window.location.href);
      if (window.location.href.length < 16){
        if (this.$root.state == '') {
          this.$router.push({name: 'login'});
        }
        else{
          this.$router.push({name : 'home'});

        }

      }
    }
  }
</script>>
<!--<style>-->
<!--    #app {-->
<!--      font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--      -webkit-font-smoothing: antialiased;-->
<!--      -moz-osx-font-smoothing: grayscale;-->
<!--      text-align: center;-->
<!--      color: #2c3e50;-->
<!--    }-->
<!--    -->
<!--    #nav {-->
<!--      padding: 20px;-->
<!--    }-->

<!--    #nav a {-->
<!--      font-weight: bold;-->
<!--      color: #2c3e50;-->
<!--    }-->

<!--    #nav a.router-link-exact-active {-->
<!--      color: #42b983;-->
<!--    }-->
<!--</style>-->
