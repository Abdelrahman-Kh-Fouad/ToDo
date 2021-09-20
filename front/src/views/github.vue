<template>
  <p1></p1>
</template>

<script>


export default {

  name: "github",
  data :function (){
    return{
      username : '',
      client_id : '4ebb67bce288c83e5459',
      client_secret :'48efba84350d8e5111647a5d01f0f741456ae316'
    }
  },

  created() {
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    let codeForAuth = params.get("code");

    this.axios.get('https://to.me/todo/githubToken/'+codeForAuth).then((response) =>{this.GetUser(response.data)});

  },
  methods:{

    GetUser:function (token){
      this.axios.get('https://to.me/todo/githubAuth/'+token).then((response) => {
        this.username = response.data ;
        console.log(this.username);
        this.$root.state = this.username;
        //window.localStorage.setItem('state' , this.username);
        this.$cookies.set("state" ,this.username);

        this.$router.push({name : 'home' });
      });
      // this.$router.push('todo')
    }
  }

}
</script>

<style scoped>

</style>