import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {

  },
  mutations: {

  },
  actions: {
    GET ({ state, commit }, urlpack) {
      console.log('Requesting', urlpack.url)
      return Vue.http.get(urlpack.url, { params: urlpack.params })
    },
    POST ({ state, commit }, urlpack) {
      console.log('Requesting', urlpack.url, 'with POST')
      return Vue.http.post(urlpack.url, urlpack.body, { params: urlpack.params })
    }
  }
})
