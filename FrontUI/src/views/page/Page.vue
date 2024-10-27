<template>
  <div class="blog">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb container">
        <li class="breadcrumb-item"><a href="/">Home</a></li>
        <li class="breadcrumb-item"><a href="#">Blog</a></li>
        <li class="breadcrumb-item active" aria-current="page">
          {{ blogData.title }}
        </li>
      </ol>
    </nav>
    <div class="container">
      <div class="row">
        <div class="col-md-12 pt-1 pb-2">
          <h1>{{ blogData.title }}</h1>
        </div>
        <div class="col-md-12">
<<<<<<< HEAD
          <p class="m-2">{{ blogData.content }}</p>
=======
          <div class="p-5" v-html="contentWarp(blogData.content)"></div>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
          <div class="mt-5 mb-3 ml-3">
          <span class="text-md-right btn btn-default" v-on:click="LikeClick(blogData.id, likeValue() )"><i class="fa fa-heart"></i></span>
          </div>
         <section class="link-holder m-1 rounded">
           <ul class="clear-fix"> 
             <li>
               <h4 role="presentation">created</h4>
<<<<<<< HEAD
               <div class=" created-at">
                 <a >
                   <b class="btn-sm rounded-circle m-sm-1 bg-warning text-white font-weight-light">C</b>
=======
               <div class="created-at">
                 <a >
                   <b class="btn-md rounded-circle m-sm-1 bg-warning text-white font-weight-light p-1">C</b>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
                 </a>
                   <span v-bind:title="blogData.created_on">{{formatDate(blogData.created_on )}}</span>
              </div>
             </li>
             <li>
               <a>
                  <h4 role="presentation">last {{commentLastDate() > replyLastDate()?'comment':replyLastDate()=== undefined?'comment':'reply'}}</h4>
                  <div class="last-reply">
<<<<<<< HEAD
                    <a class="trigger-user-card " data-user-card="ToddBroeker"> <b class="btn-sm rounded-circle m-sm-1 bg-info text-white font-weight-light">R</b></a>
=======
                    <a class="trigger-user-card " data-user-card="ToddBroeker"> <b class="btn-sm rounded-circle m-sm-1 bg-info text-white font-weight-light p-1">R</b></a>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
                  <span >{{commentLastDate() > replyLastDate()?formatDate(commentLastDate()):replyLastDate()=== undefined?formatDate(commentLastDate()):commentLastDate()=== undefined?'No reply':formatDate(replyLastDate())}}</span>
                  </div>
                </a>
              </li>
              <li>
                <span class="number">{{blogComment.length}}</span>
                <h4 role="presentation">comments </h4>
              </li>
              <li>
                <span class="number">{{blogReply.length}}</span>
                <h4 role="presentation">replies</h4>
              </li>
              <span v-for="count in blogHitView" :key="count.id">
              <li class="secondary">
                <span class="number"  >{{count.viewcount}}</span>
                <h4 role="presentation">views</h4>
              </li>
              <li class="secondary">
                <span class="number"  >{{count.hitcount}}</span>
                <h4 role="presentation">likes</h4>
              </li>
              </span>
           </ul>
         </section>
        </div>
        <div class="col-md-12">
          <div class="comment">
            <!--Comments-->
            <div class="card card-comments mb-3 wow fadeIn">
              <div class="card-header font-weight-bold">
                {{ blogComment.length }} comments
              </div>
              <div class="card-body">
                <div
                  class="media d-block d-md-flex mt-4"
                  v-for="(c, Index) in blogComment"
                  :key="Index"
                >
                  <div :class="'avatar ' + AvatarColorChange(c.author.substring(0,1))"><h2 class="text-center pt-1 mt-md-1 mt-sm-2 mt-lg-1">{{c.author.substring(0,1).toUpperCase()}}</h2></div>
                  <div class="media-body text-center text-md-left ml-md-3 ml-0">
                    <h5 class="font-weight-bold"> {{ c.author }} <span class="relative-date float-right font-weight-lighter">{{formatDate(c.created_on)}}</span></h5>
                    <p>{{ c.body }} </p>
                    
                    
                    <div class="text-right pt-1">
<<<<<<< HEAD
                      <a id="reply" v-on:click="showModal(Index)">Replay</a>
                    </div>
                    <hr />
                    <div class="media d-block d-md-flex mt-3" v-for="reply in replyFilter(c.id)" :key="reply.id">
                    <div :class="'avatar ' + AvatarColorChange(reply.author.substring(0,1))"><h2 class="text-center pt-1 mt-md-1 mt-sm-2 mt-lg-1">{{reply.author.substring(0,1).toUpperCase()}}</h2></div>
=======
                      <a id="reply" v-on:click="showModal(Index)">Reply</a>
                    </div>
                    <hr />
                    <div class="media d-block d-md-flex mt-3 replay" v-for="reply in replyFilter(c.id)" :key="reply.id">
                    <div :class="'avatar ' + AvatarColorChange(reply.author.substring(0,1))"><h2 class="text-center">{{reply.author.substring(0,1).toUpperCase()}}</h2></div>
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
                    <div class="media-body text-center text-md-left ml-md-3 ml-0">
                        <h5 class="mt-0 font-weight-bold">{{reply.author}} <span class="relative-date float-right font-weight-lighter">{{formatDate(reply.created_on)}}</span></h5>
                        <p>{{reply.body}}</p>
                    
                    <hr />
                    </div>
                   </div>
                   <ReplyModal :ref="'modal_' + Index">
                     <form @submit.prevent="replyPost(c.id)">
                      <label for="user">Your Name</label>
                      <input type="text" class="form-control" name="user" v-model="replyUser" required />
                      <input type="hidden" :value="c.id" :id="'commentid'+Index" :ref="'commentId'+Index" />
                      <label for="quickReplyFormComment">Your comment</label>
                      <textarea
                        class="form-control"
                        id="quickReplyFormComment"
                        rows="5" v-model="replyBody"
                        required
                      ></textarea>
                      <div class="mt-2 mb-2 float-right">
                        <button class="btn btn-info btn-sm" type="submit">
                          Post
                        </button>
                      </div>
                     </form>
                     </ReplyModal>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--/.Comments-->

            <!--Reply-->
            <div class="card mb-3 wow fadeIn">
              <div class="card-header font-weight-bold">Leave a Comment</div>
              <div class="card-body">
                <!-- Default form reply -->
                <form @submit="commentPost">
                  <!-- Name -->
                  <label for="replyFormName">Your name</label>
                  <input type="text"  id="replyFormName" v-model="commentAuthor" class="form-control" required />
                  <!-- Comment -->
                  <div class="form-group">
                    <label for="replyFormComment">Your comment</label>
                    <textarea class="form-control" id="replyFormComment" rows="5" required  v-model="commentBody"></textarea>
                  </div>
                  <div class="form-group">
                    <button class="btn btn-info btn-md mr-2" >Post</button>
                    <button class="btn btn-warning">Cancel</button>
                  </div>
                </form>
                <!-- Default form reply -->
              </div>
            </div>
            <!--/.Reply-->
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios';
import moment from 'moment';
<<<<<<< HEAD
import ReplyModal from './replyModal';
=======
import ReplyModal from './replyModal.vue';
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
export default {
  
  name: "post",
  components:{
    ReplyModal
  },
  data() {
    return {
      blogData: {},
      blogComment:[],
      blogReply:[],
      blogHitView:{},
      commentBody:'',
      commentAuthor:'',
      replyUser:'',
      replyBody:'',
<<<<<<< HEAD
=======
      postId:0,
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
    };
  },
  mounted() {
    this.fetchBlogItems();
<<<<<<< HEAD
    this.fetchComment();
    this.formatDate();
    this.fetchHitLike();
    this.fetchReply();
=======
    setTimeout(()=>{
      this.fetchComment();
      this.fetchReply();
      this.fetchHitLike();
    },1000)
   
    this.formatDate();
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
    
  },
  computed: {
   
  },
  methods: {
<<<<<<< HEAD
    fetchBlogItems() {
      axios
        .get("http://localhost:8000/api/blog/" + this.$route.params.id + "/")
        .then(response => {
          this.blogData = response.data;
        });
    },
    fetchComment() {
      axios
        .get("http://localhost:8000/api/comment/?post=" + this.$route.params.id)
        .then(response => {
          this.blogComment = response.data;
=======
    // sam( data ){return (window.location.pathname.substring(window.location.pathname.indexOf('/',1)+1, (window.location.pathname).toString().length))}
    
    fetchBlogItems() {
      axios
        .get("http://localhost:8080/api/blog/" + this.$route.params.id + "/")
        .then(response => {
          this.blogData = response.data;
          this.postId = response.data.id;
        });
    },
    fetchComment() {  
      axios
        .get("http://localhost:8080/api/comment/?post=" + this.postId)
        .then(response => {
          this.blogComment = response.data;
          
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
        });
    },
    fetchHitLike(){
       axios
<<<<<<< HEAD
        .get("http://localhost:8000/api/hitlike/?post=" + this.$route.params.id)
=======
        .get("http://localhost:8080/api/hitlike/?post=" + this.postId)
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
        .then(response => {
          this.blogHitView = response.data;
        });
    },
    fetchReply(){
<<<<<<< HEAD
       axios
        .get("http://localhost:8000/api/replycomment/?post="+this.$route.params.id)
        .then(response => {
          this.blogReply = response.data;
=======
      console.log(this.postId)
       axios
        .get("http://localhost:8080/api/replycomment/?post="+this.postId)
        .then(response => {
          this.blogReply = response.data;
          
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
        });
    },
    LikeClick: function(id,likes) {
      const likecount = parseInt(likes) + 1; 
<<<<<<< HEAD
      axios.put("http://localhost:8000/api/hitlike/"+ id +"/",{hitcount: likecount,post:id})
=======
      axios.put("http://localhost:8080/api/hitlike/"+ id +"/",{hitcount: likecount,post:id})
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
      .then( this.fetchHitLike())
      .catch((response) => console.log('error', response));
    }, 
    // Comment Post //
    commentPost:function(e){
      e.preventDefault();
<<<<<<< HEAD
        const item ={author:this.commentAuthor, body:this.commentBody, post:this.$route.params.id};
        axios.post("http://localhost:8000/api/comment/",item).then(location.reload()).catch(res => console.log('error', res))
=======
        const item ={author:this.commentAuthor, body:this.commentBody, post:this.postId};
        axios.post("http://localhost:8080/api/comment/", item).then(location.reload()).catch(res => console.log('error', res))
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
      
    },   
    // Reply Filter //
    replyFilter: function(id) {
      return this.blogReply.filter(el => {
        return el.comment === id;
      })
    },
    //Reply Post
    replyPost:function(e){
<<<<<<< HEAD
       const item = {author:this.replyUser, body:this.replyBody, comment:e, post:this.$route.params.id}
       axios.post("http://localhost:8000/api/replycomment/",item).then(location.reload()).catch(res => console.log('error', res))
=======
       const item = {author:this.replyUser, body:this.replyBody, comment:e, post:this.postId}
       axios.post("http://localhost:8080/api/replycomment/",item).then(location.reload()).catch(res => console.log('error', res))
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
    },
     showModal(index) {
      let modal_id = "modal_" + index;
      this.$refs[modal_id][0].show();
    },
    // Formate Date //
    formatDate(value) {
      if (value) {
        return moment(String(value)).format('MMM DD')
      }
    },
    // LastDate Post
    commentLastDate() {
      var c = this.blogComment.length - 1;
      if(this.blogComment[c])
        return  this.blogComment[c].created_on;
    },
    replyLastDate(){
      var r = this.blogReply.length -1;
      if(this.blogReply[r])
        return this.blogReply[r].created_on;
    },
    likeValue(){
      var l =this.blogHitView.length -1
      if(this.blogHitView[l])
        return this.blogHitView[l].hitcount
    },
<<<<<<< HEAD
=======
    contentWarp(content){
      return content
        .split('\n')
        .map(line => `<p>${line}</p>`)
        .join(''); // Join to produce a single HTML string
    },
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
    //Avatar BG Colors
    AvatarColorChange(textExtract){
      const text = textExtract.toUpperCase();
      if(text ==='A'|text === 'B'){ return 'bg-color-1'; }
      else if(text === 'C' | text === 'D'){ return 'bg-color-2'; }
      else if(text === 'E' | text === 'F'){ return 'bg-color-3'; }
      else if(text === 'G' | text === 'H'){ return 'bg-color-4'; }
      else if(text === 'I' | text === 'J'){ return 'bg-color-5'; }
      else if(text === 'K' | text === 'L'){ return 'bg-color-6'; }
      else if(text === 'M' | text === 'N'){ return 'bg-color-7'; }
      else if(text === 'O' | text === 'P'){ return 'bg-color-8'; }
      else if(text === 'Q' | text === 'R'){ return 'bg-color-9'; }
      else if(text === 'S' | text === 'T'){ return 'bg-color-10'; }
      else if(text === 'U' | text === 'V'){ return 'bg-color-11'; }
      else if(text === 'W' | text === 'X'){ return 'bg-color-12'; }
      else if(text === 'Y' | text === 'Z'){ return 'bg-color-13'; }
      
    }
  }
};

</script>
<style lang="scss" >
<<<<<<< HEAD
.blog {
 @import '../../assets/scss/page';
}
=======

 @use '../../assets/scss/page';
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
</style>
