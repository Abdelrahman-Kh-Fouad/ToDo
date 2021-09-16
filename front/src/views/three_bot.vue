<template>
  <p1>as</p1>
</template>

<script>
import axios from "axios";

export default {
  name: "three_bot",
  data :function (){
    return{
      username : '',
    }
  },

  created() {
    let uri_args = window.location.search.substr(1);
    console.log('to.me/todo/call_back?'+uri_args)

    axios.get('https://to.me/todo/call_back?'+uri_args).then((response)=>{
      this.username = response;
      this.$router.push({name : 'todo' ,params : {username : this.username} });
    });


  }
}
</script>

<style scoped>

</style>