import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import ArticleList from '@/components/ArticleList'
import Article from '@/components/Article'

Vue.use(Router)

export default new Router({
	mode: "history",
	routes: [{
		path: '/',
		name: 'Home',
		component: Home
	}, {
		path: '/c/:category',
		name: 'ArticleList',
		component: ArticleList
	}, {
		path: '/article/:category/:article_slug',
		name: 'Article',
		component: Article
	}, {
		path: '/f/:article_slug',
		name: 'Article',
		component: Article
	}]
})