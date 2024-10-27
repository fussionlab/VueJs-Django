<template>
  <div class="home container">
    <div class="row">
      <div class="col-md-12">
        <h1>Blog Posts</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 p-1" v-for="(p, index) in items" :key="index">
        <div class="card">
          <img src="../assets/1.jpg" alt="" class="w-100" />
          <div class="card-body">
            <h4 class="card-title">{{ p.title }}</h4>
            <p class="card-text" v-if="p.content.length>100">{{ p.content.substring(0, 100)+ '...' }}</p>
            <!-- <span class="btn-circle btn-success" v-if="p.completed">&check;</span>
      <span class="btn-circle btn-warning" v-else>&cross;</span> -->
<<<<<<< HEAD
            <a v-on:click="ViewClick(p.id, hitlike[p.id-1].viewcount)"   class="btn btn-primary text-light" >Read more</a>
=======
            <a v-on:click="ViewClick(p.id, hitlike[p.id-1].viewcount)"  :href="'blog/'+p.slug" class="btn btn-primary text-light" >Read more</a>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
          </div>
          <div class="card-footer">
            <input type="hidden"  name="PostID"  :value='p.id' />
            <ul>
              <span v-for='hl in hitLikeFilter(p.id)' :key="hl.id">
              <li class="btn btn-default">
<<<<<<< HEAD
                 <i v-bind:class="DataCon(hl.hitcount)>=1?'fa fa-heart text-danger':'fa fa-heart'"></i><span> {{ hl.hitcount }}</span> 
=======
                 <i v-bind:class="DataCon(hl.hitcount)>=1?'fa fa-heart text-danger':'fa fa-heart'"></i><span> {{ hl.hitcount}}</span> 
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
              </li>
              <li class="btn btn-default" >
                <i  v-bind:class="DataCon(hl.viewcount)>=1?'fa fa-eye text-primary':'fa fa-eye'" class=""></i> <span>{{ hl.viewcount }}</span>
              </li>
              </span>
              <li value="2" class="btn btn-default">
               <i   v-bind:class="commentFilter(p.id).length>=1? 'fa fa-comment text-success':'fa fa-comment'" ></i><span> {{commentFilter(p.id).length}}</span>
              </li>
              <!-- <li class="btn btn-default" v-on:click="likeClick(p.bloglikes, p.title, p.slug, p.content, p.author)">
                <i class="fa fa-heart "></i> {{ hitLikeFilter(p.id) }}
              </li> --> 
            </ul>
          </div>
        </div>
      </div>
    </div>
   <div class="sidebar"></div>
  </div>
</template>

<script>
import axios from "axios";
export default {
<<<<<<< HEAD
=======
  header :{
       headers: {
                  'Access-Control-Allow-Origin': '*',
                  'Access-Control-Allow-Headers': '*',
                  'Access-Control-Allow-Credentials': 'true'
                }
      },
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
  name: "home",
  data() {
    return {
      counter: 0,
      items: [],
      comments:[],
      hitlike:[],
<<<<<<< HEAD
=======
      postId:0
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
    };
  },
  
  computed: {
            
  },    
  mounted() {
    this.fetchItems();
    this.fetchCommentCount(); 
    this.fetchHitLike();
  },
  methods: {
    fetchItems() {
<<<<<<< HEAD
      axios.get("http://localhost:8000/api/blog/").then(response => {
=======
      axios.get("http://localhost:8080/api/blog/", this.header).then(response => {
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
        this.items = response.data;
      });
    },
    fetchCommentCount(){
<<<<<<< HEAD
      axios.get("http://localhost:8000/api/comment/")
=======
      axios.get("http://localhost:8080/api/comment/", this.header)
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
      .then(response => {
        this.comments = response.data;
      });
    },
    fetchHitLike(){
<<<<<<< HEAD
      axios.get("http://localhost:8000/api/hitlike/")
=======
      axios.get("http://localhost:8080/api/hitlike/", this.header)
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
      .then(response => {
        this.hitlike = response.data;
      });
    },
    ViewClick: function(id,views) {
      const likecount = views + 1; 
<<<<<<< HEAD
      axios.put("http://localhost:8000/api/hitlike/"+ id +"/",{viewcount: likecount,post:id})
=======
      axios.put("http://localhost:8080/api/hitlike/"+ id +"/",{viewcount: likecount,post:id}, this.header)
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
      .then(this.$router.push({ path: `/blog/${id}` }))
      .catch((response) => console.log('error', response));
    },    
    commentFilter: function(id) {
      return this.comments.filter(el => {
        return el.post === id;
      })
    },
    hitLikeFilter:function(hitlikeData){
      return this.hitlike.filter(el => {
        return el.post === hitlikeData;
     })
    },
    DataCon:(data)=>{
      return parseInt(data);
    },
    
       
  }
};
</script>
<style lang="scss">
.col-md-6 {
  h4 {
    color: indigo;
  }
  .btn-circle {
    width: 40px;
    height: 40px;
    padding: 0.5rem;
    border-radius: 50%;
  }
  .btn {
    color: grey;
    span {
      color: grey;
    }
    .card {
      .card-footer {
        ul {
          list-style: none;
        }
        li{
          span{
            color: var(--dark)
          }
        }
        span{
          li:nth-of-type(2){
          order: 3
        }
        
        }
      }
    }
  }
}
</style>
