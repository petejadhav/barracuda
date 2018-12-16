<template>
  <div class="container">
    <div v-for="article in articleList">
      <article-card v-bind:title="article.title" v-bind:image="article.image"
      v-bind:author="article.author" v-bind:date="article.date" v-bind:link="article.link" v-bind:route="article.slug">
      </article-card>
    </div>
  </div>
</template>

<script>
import ArticleCard from "./ArticleCard.vue";
export default {
  name: 'ArticleList',
  components: {ArticleCard},
  category: "blog",

  mounted: function() {
    console.log(this.$route);
    var full_path = this.$route.path;
    this.category = full_path.split("/")[2];
    this.$store.dispatch('loadCategoryIndex',this.category)
      .then(() => this.articleList = this.$store.state.category_index[this.category]['articles'])
  },

  /*computed:mapState({
    articleList(state){

    }
  }),*/

  data () {
    return {
      articleList: []
      /*articleList: [
        {
          title: "article 1",
          image: "https://upload.wikimedia.org/wikipedia/commons/a/af/Logo_des_Joutes_du_T%C3%A9m%C3%A9raire.png",
          author: "Pete Jadhav",
          date: "21 Aug 2018",
          link: "/article/qwerty"
        },
        {
          title: "article 2",
          image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Recordlogo.jpg/137px-Recordlogo.jpg",
          author: "Pete Jadhav",
          date: "21 Aug 2018",
          link: "/article/qwerty"
        }
      ]*/
    };
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
