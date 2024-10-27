<template>
  <div id="app">
    <Navi />
    <RouterView />
    <Footers />
  </div>
</template>
<script>
import Navi from './components/navi.vue'
import Footers  from './components/footer.vue'
import { RouterView } from 'vue-router';  // Import RouterView

export default {
  name:'app',
  components:{
    Navi,
    Footers,
    RouterView
  }
}
</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

/* Background Colors */
.bg-color-1 { background-color: #581845; }
.bg-color-2 { background-color: #900C3F; }
.bg-color-3 { background-color: #C70039; }
.bg-color-4 { background-color: #FF5733; }
.bg-color-5 { background-color: #FFC300; }
.bg-color-6 { background-color: #33691e; }
.bg-color-7 { background-color: #3498db; }
.bg-color-8 { background-color: #DAF7A6; }
.bg-color-9 { background-color: #8e44ad; }
.bg-color-10 { background-color: #34495e; }
.bg-color-11 { background-color: #d35400; }
.bg-color-12 { background-color: #2e86c1; }
.bg-color-13 { background-color: #e91e63; }

/* Text Colors */
.color-1 { color: #581845 !important; }
.color-2 { color: #900C3F !important; }
.color-3 { color: #C70039 !important; }
.color-4 { color: #FF5733 !important; }
.color-5 { color: #FFC300 !important; }
.color-6 { color: #33691e !important; }
</style>

