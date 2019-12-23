<template>
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
}
</script>