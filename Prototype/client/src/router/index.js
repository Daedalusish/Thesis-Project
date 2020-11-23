import Vue from 'vue'
import VueRouter from 'vue-router'
import Welcome from "../views/Welcome.vue"
import Search from "../views/Search.vue"
import Browse from "../views/Browse.vue"
import Survey from "../views/Survey.vue"
import Instruction from "../views/Instruction.vue"



//This handles the storage of all the possible routes in the page
Vue.use(VueRouter)

  const routes = [
  {
    path: '/Search',
    component: Search
  },
  {
    path: '/Welcome',
    component: Welcome
  },
  {
    path: '/Instruction',
    component: Instruction,
  },
  {
    path: '/Browse/:id',
    component: Browse
  },
  {
    path: '/Survey',
    component: Survey
  }
]
//router settings. Abstract sets it so the user cannot see the URL paths, and since it's all viewed in app.vue <router-view>, users cannot impact navigation using browser tools.
const router = new VueRouter({
  routes,
  mode: 'abstract'
})

export default router
