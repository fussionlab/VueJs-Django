<template>
<<<<<<< HEAD
    <div class="form-group mt-4 fadeIn mb-3" v-if="visible">
     <button title="Close" class="btn btn-danger btn-sm float-right mb-1" @click='close()'>X</button>
=======
    <div class="form-group mt-4 fadeIn mb-3 close-btn" v-if="visible">
     <button title="Close" class="btn btn-danger btn-sm float-right mb-1 w-1 h-1" @click='close()'>X</button>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
          <slot></slot>
    </div>
</template>

<script>
export default {
    name:"ReplyModal",

    data(){
        return {
            visible : false
        }
    },
    methods : {
        show(){
            this.visible = true
        },
        close(){
            this.visible = false
        }
    }
}
</script>
<<<<<<< HEAD
=======
<style lang="postcss" scoped>
    .close-btn{
        position: relative;
        button{
            width: 10%;
            height: 10%;
            font-size: 10px;
            position: absolute;
            right: 0;
            top: -10px;
        }
    }
</style>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
