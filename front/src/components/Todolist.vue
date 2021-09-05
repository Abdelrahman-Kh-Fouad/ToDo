<template>

     <div class="row mx-1 px-5 pb-3 w-80" >
            <div class="col mx-auto">
                    <!-- Todo Items -->
                    
                    <!--<Todoitem v-for =" item in TODOdata" :todoitem =' item' ></Todoitem>-->
                    <div class="row px-3 align-items-center todo-item rounded" v-for="todoitem in this.$root.list" :key="todoitem">
                                                    

                        <div class="col px-1 m-1 d-flex align-items-center">
                            <input  type="text" class="form-control form-control-lg border-0 edit-todo-input bg-transparent rounded px-3" readonly :value= "todoitem.text" :title= "todoitem.text" />

                            <input  type="text" class="form-control form-control-lg border-0 edit-todo-input rounded px-3 d-none" :value= "todoitem.text" />
                        </div>
                        
                        
                        <div class="col-auto m-1 p-0 px-3 d-none"></div>
                        <div class="col-auto m-1 p-0 todo-actions">
                            <div class="row d-flex align-items-center justify-content-end">

                                
                                <h5 class="m-0 p-0 px-2">
                                    <i class="fa fa-trash-o text-danger btn m-0 p-0" data-toggle="tooltip" data-placement="bottom" title="Delete todo" @click= "deleteItem(todoitem._id)"></i>
                                </h5>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
  
</template>

<script>
import axios from 'axios';
export default {
  name: 'Todolist',
   data: function () {
        return {

            deleteItem : function(_id){
                console.log(_id);
                axios.delete(this.$root.Url +'/'+_id); 
                this.$root.refresh();
            }
        }
    },
    methods : {
        
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
   @import '../assets/style.css';
</style>
