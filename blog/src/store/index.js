import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const state = {
	// single source of data
	master: {
		categories: [],
		flatpages: []
	},
	url_prefix: "/content/",
	category_index: {}
}

const actions = {
	// asynchronous operations
	loadMaster(context) {
		return axios.get(state.url_prefix + "master.json")
			.then((response) => context.commit('setMaster', {
				master: response.data
			}))
	},

	loadCategoryIndex(context, category) {
		return axios.get(state.url_prefix + category + "/index.json")
			.then((response) => context.commit('setCategoryIndex', {
				category: category,
				index: response.data
			}))
	},

}

const mutations = {
	// isolated data mutations
	setMaster(state, payload) {
		state.master = payload.master;
		state.isMasterLoaded = true;
	},

	setCategoryIndex(state, payload) {
		state.category_index[payload.category] = payload.index;
		console.log(state.category_index);
	}

}

const getters = {
	// reusable data accessors
}

const store = new Vuex.Store({
	state,
	actions,
	mutations,
	getters
})

export default store