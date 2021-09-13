<template>
<h1> s</h1>
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

    this.axios.get('http://to.me/todo/githubToken/'+codeForAuth).then((response) =>{this.GetUser(response.data)});
    //axios.post('https://github.com/login/oauth/access_token?client_id=${this.client_id}&client_secret=${this.client_secret}&code={codeForAuth}')
    // var config = {
    //   headers: {
    //     'Access-Control-Allow-Origin': '*'
    //   },
    //   proxy: {
    //     host: 'http://github/'
    //   }
    // };
    // this.axios.post('https://github.com/login/oauth/access_token?client_id=' +this.client_id+'&client_secret=' +this.client_secret+'&code=' +codeForAuth , config)
    // .then((response) => {
    //   console.log(response);
    // }, (error) => {
    //   console.log(error);
    // });


    //this.$router.push('todo')  ;



  },
  methods:{
    GetUser:function (token){
      this.axios.get('http://to.me/todo/githubAuth/'+token).then((response) => {
        this.username = response.data ;
        console.log(this.username);
        this.$router.push({name : 'todo' ,params : {username : this.username} });
      });
      // this.$router.push('todo')
    }
  }

}
</script>

<style scoped>

</style>