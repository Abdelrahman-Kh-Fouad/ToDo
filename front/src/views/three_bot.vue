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
      this.username = response.data;
      console.log(this.name)
      this.$root.state = this.username;
     // window.localStorage.setItem('state' , this.username);
      this.$cookies.set("state" ,this.username);

      this.$router.push({name : 'home' });
    });


  }
}
</script>

<style scoped>

</style>