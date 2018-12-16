<template>
	<nav class="navbar is-light" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start" >
          <router-link v-for="(category, i) in categories" class="navbar-item" :to="category.routerlink" :key="i">
            {{category.title}}
          </router-link>          
        </div>

        <div class="navbar-end" v-for="(flatpage, i) in flatpages">
          <router-link class="navbar-item" :to="flatpage.routerlink" :key="i">
            {{flatpage.title}}
          </router-link> 
        </div>
      </div>
    </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Header',

  computed:mapState({

    categories(state){ 
      var cats = state.master.categories.map(function(x){
        return {
          "title":x.toUpperCase(),
          "routerlink": "/c/"+x,
        };
      })
      cats.push({"title":"Home", "routerlink":"/"})
      cats.reverse();
      return cats;
    },

    flatpages(state){
      return state.master.flatpages.map(function(x){
        return {
          "title":x.title.toUpperCase(),
          "routerlink": "/f/"+x.title.toLowerCase().split(" ").join("_"),
          "link":x.link
        };
      })
    }

  }),

  data () {
    return {
      /*categories:[],
      flatpages:[]*/
    }
  }
}
</script>

<style lang="scss">
</style>