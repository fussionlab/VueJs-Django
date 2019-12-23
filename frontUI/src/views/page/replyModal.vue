<template>
    <div class="form-group mt-4 fadeIn mb-3" v-if="visible">
     <button title="Close" class="btn btn-danger btn-sm float-right mb-1" @click='close()'>X</button>
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
