<template>
<<<<<<< HEAD
    <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">Hornbill</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="p-2">
       <b-nav-item href="/blog">Blog</b-nav-item>
       <b-nav-item href="/about">About</b-nav-item>
     </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <!-- <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown> -->

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<script>
import {BNavbarNav, BNavItem, BNavbar, BNavForm,BFormInput, BNavItemDropdown,BDropdownItem, BNavbarBrand, BCollapse, BNavbarToggle, BButton} from 'bootstrap-vue';
export default {
    name:'Navi',
    components:{
        'b-navbar-brand':BNavbarBrand,
        'b-dropdown-item':BDropdownItem,
        'b-navbar':BNavbar,
        'b-nav-item':BNavItem,
        'b-collapse':BCollapse,
        'b-nav-item-dropdown':BNavItemDropdown,
        'b-nav-form':BNavForm,
        'b-navbar-toggle':BNavbarToggle,
        'b-button':BButton,
        'b-navbar-nav':BNavbarNav,
        'b-form-input':BFormInput,
    }
=======
<div class="bg-info">
<nav class="container  navbar navbar-expand-lg navbar-dark bg-info d-flex justify-content-between">
  <div>
  <a class="navbar-brand" href="#">Hornbill</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nav-collapse" aria-controls="nav-collapse" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  </div>
  <div class="collapse navbar-collapse" id="nav-collapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/blog">Blog</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about">About</a>
      </li>
    </ul>
  </div>
  <div>
  <ul class="navbar-nav ml-auto">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <em>User</em>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
          <a class="dropdown-item" href="#">Profile</a>
          <a class="dropdown-item" href="#">Sign Out</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
</div>
</template>
<script>

export default {
    name:'Navi',
   
>>>>>>> 990206a (Vite 3 , Vue 3 and Django)
}
</script>