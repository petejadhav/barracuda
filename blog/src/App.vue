<template>
  <div id="app">
    <!-- Header -->
    <Header></Header>
    <div class="container is-fullhd">
      <router-view/>
    </div>
    <!-- Footer -->
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },

  isLoaded: false,
  beforeMount() {
    //Get master JSON
    this.$store.dispatch('loadMaster').then(() => console.log(this.$store.state.master));
  },
}
</script>

<style lang="scss">

// Import a Google Font
@import url('https://fonts.googleapis.com/css?family=Nunito:400,700');

// Set your brand colors 
$purple: #8A4D76;
$pink: #FA7C91;
$brown: #757763;
$beige-light: #D0D1CD;
$beige-lighter: #EFF0EB;

// Update Bulma's global variables
$family-sans-serif: "Nunito", sans-serif;
$grey-dark: $brown;
$grey-light: $beige-light;
$primary: $purple;
$link: $pink;

// Update some of Bulma's component variables
$control-border-width: 2px;
$input-background-color: $beige-lighter;
$input-border-color: transparent;
$input-shadow: none;


@import '~bulma/bulma';

</style> 