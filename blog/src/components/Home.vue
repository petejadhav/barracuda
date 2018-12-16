<template>
  <div>
    <section class="hero is-medium is-primary is-bold">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">
            Prithviraj 'Pete' Jadhav
          </h1>
          <h2 class="subtitle">
            Wannabe Know-it-all
          </h2>
          <h2 class="subtitle">Entrepreneur - Data Scientist - Developer - Bard</h2>
        </div>
      </div>
    </section>
    <section class="hero is-medium is-dark is-bold">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="title">
            <a href="/resume" class="button is-light is-large">Resume</a>
            <a href="/work" class="button is-light is-large">Work</a>
            <a href="/blog" class="button is-light is-large">Blog</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section has-background-success is-bold">
      <div class="has-text-centered">
        <a href="http://facebook.com/petejadhav" class="button is-dark is-medium">Facebook</a>
        <a href="https://linkedin.com/in/petejadhav" class="button is-dark is-medium">LinkedIn</a>
        <a href="https://twitter.com/petejadhav" class="button is-dark is-medium">Twitter</a>
        <a href="https://github.com/petejadhav" class="button is-dark is-medium">GitHub</a>
        <!---<div class="box has-text-centered">  
        </div>  
        <div class="box has-text-centered">  
        </div>  
        <div class="box has-text-centered">  
        </div>-->  
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
