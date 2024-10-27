<template>
<div>
  <!-- Sidebar -->
  <nav id="sidebar">
    <div class="sidebar-header">
      <h3>{{title}}</h3>
    </div>

    <ul class="list-unstyled components">
      <p>Dummy Heading</p>
      <li class="active">
        <a
          href="#homeSubmenu"
          data-toggle="collapse"
          aria-expanded="false"
          class="dropdown-toggle"
        >Home</a>
        <ul class="collapse list-unstyled" id="homeSubmenu">
          <li>
            <a href="#">Home 1</a>
          </li>
          <li>
            <a href="#">Home 2</a>
          </li>
          <li>
            <a href="#">Home 3</a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a
          href="#pageSubmenu"
          data-toggle="collapse"
          aria-expanded="false"
          class="dropdown-toggle"
        >Pages</a>
        <ul class="collapse list-unstyled" id="pageSubmenu">
          <li>
            <a href="#">Page 1</a>
          </li>
          <li>
            <a href="#">Page 2</a>
          </li>
          <li>
            <a href="#">Page 3</a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </nav>
  
    <slot></slot>
  </div>
  <!-- Page Content -->
</template>
<script>
export default {
  name: "SideBar",
  data() {
    return {
        title:'Dashboard'
    };
  },
  methods: {}
};
</script>
<style lang="scss" scoped>
#sidebar {
  /* don't forget to add all the previously mentioned styles here too */
  background: #0a6a7a;
  color: #fff;
  transition: all 0.3s;
  .sidebar-header {
    padding: 20px;
    background: #0a505b;
  }
  ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #47748b;
  }
  ul {
    p {
      color: #fff;
      padding: 10px;
    }
    li {
      a {
        padding: 10px;
        font-size: 1.1em;
        display: block;
      }
      a:hover {
        color: #7386d5;
        background: #fff;
      }
      .active > a,
      a[aria-expanded="true"] {
        color: #fff;
        background: #6d7fcc;
      }
    }
    ul a {
      font-size: 0.9em !important;
      padding-left: 30px !important;
      background: #6d7fcc;
    }
  }
}
</style>