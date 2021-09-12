<template>

  <div className="container m-5 p-2 rounded mx-auto bg-light shadow">


    <!-- App title section -->
    <!--Here i want to be username name -->
    <div className="row m-1 p-4">
      <div className="col">
        <div className="p-1 h1 text-primary text-center mx-auto display-inline-block">
          <i className="fa fa-check bg-primary text-white rounded p-2"></i>
          <i>Todo</i>
        </div>
      </div>
    </div>

    <!-- Create todo section -->

    <div className="row m-1 p-3">
      <div className="col col-11 mx-auto">
        <div className="row bg-white rounded shadow-sm p-2 add-todo-wrapper align-items-center justify-content-center">
          <div className="col">
            <input type="text" v-model="currentTodo" name="uploaded-text" id="uploaded-text"
                   className="form-control form-control-lg border-0 add-todo-input bg-transparent rounded"
                   placeholder="Add new ..">
          </div>

          <div className="col-auto px-0 mx-0 mr-2">
            <input type="submit" className="btn btn-primary" value="Add" v-on:click="AddNewOne">
          </div>
        </div>
      </div>
    </div>

    <div className="p-2 mx-4 border-black-25 border-bottom"></div>


    <!-- View options section -->
    <!--
    <div class="row m-1 p-3 px-5 justify-content-end">
        <div class="col-auto d-flex align-items-center px-1 pr-3">
            <label class="text-secondary my-2 pr-2 view-opt-label">Sort</label>
            <select class="custom-select custom-select-sm btn my-2">
                <option value="added-date-asc" selected>Added date</option>
                <option value="due-date-desc">Due date</option>
            </select>
            <i class="fa fa fa-sort-amount-asc text-info btn mx-0 px-0 pl-1" data-toggle="tooltip" data-placement="bottom" title="Ascending"></i>
            <i class="fa fa fa-sort-amount-desc text-info btn mx-0 px-0 pl-1 d-none" data-toggle="tooltip" data-placement="bottom" title="Descending"></i>
        </div>
    </div>
    -->


    <!-- Todo list section -->

    <Todolist/>

  </div>


</template>

<script>
import Todolist from '../components/Todolist.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Todolist
  },
  data() {
    return {
      list: [],
      currentTodo: "",
      Url: 'http://to.me:5000' + '/todo',
      idForTodo: ''
    }
  },
  created: function () {
    console.log(this.Url);
    this.refresh();
  },
  methods: {
    refresh: function () {
      axios.get(this.Url)
          .then(response => (this.list = response.data));
      console.log(this.Url);
    },
    AddNewOne: function () {
      console.log(this.currentTodo);
      if (this.currentTodo == '')
        return;
      this.currentId = '';
      axios.post(this.Url + '/', {text: this.currentTodo})
          .then(response => (this.currentId = response.data))
          .catch(err => {
            console.log(err);
          });
      console.log(this.currentId);
      this.list.push({_id: this.currentId, text: this.currentTodo});
      this.currentTodo = '';
      console.log(this.list);

    },

  }
}
</script>

<style>
@import '../assets/style.css';

</style>