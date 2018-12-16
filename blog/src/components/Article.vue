<template>
  <div>
    <section class="hero is-primary is-bold">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">
            {{title}}
          </h1>
          <h2 class="subtitle">
            {{author}}
          </h2>
          <h2 class="subtitle">{{date}}</h2>
        </div>
      </div>
    </section>
    <section class="content container">
      <h3 v-if="!contentRetrieved || !infoRetrieved">Loading...</h3>
      <vue-markdown :source="article_content"></vue-markdown>
    </section>
  </div>  
</template>

<script>
import VueMarkdown from 'vue-markdown';
import axios from 'axios';
export default {
  name: "Article",
  components: {
    VueMarkdown
  },
  props : [],
  category: "",

  beforeMount() {
    var self = this;
    var route_split = this.$route.path.split("/");
    if(route_split[1] == "article"){
      this.category = route_split[2];
      this.slug = route_split[3];      
    }

    if(route_split[1] == "f"){
      this.category = "flatpages";
      this.slug = route_split[2];
    }


    var final_md_path = this.$store.state.url_prefix+this.category+"/"+self.slug+".md";
    var final_json_path = this.$store.state.url_prefix+this.category+"/"+self.slug+".json";

    var json_req = axios.get(final_json_path)
      .then(function(response){
        self.title = response.data.title;
        self.author = response.data.author;
        self.date = response.data.date;
        self.infoRetrieved = true;
      });    

    var md_req = axios.get(final_md_path)
      .then(function(response){
        self.article_content = response.data;
        self.contentRetrieved = true;
      });

    return;
  },

  data: function() {
    //this.getArticleFromSlug(this.$route.params.article_slug);
    return {
      title:"",
      image:"",
      author:"",
      date:"",
      article_content:"",
      contentRetrieved: false,
      infoRetrieved: false
    }

  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
section.content {
  padding-top: 20px;
}
</style>
