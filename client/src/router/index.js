import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GraphView from '../views/GraphView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/graph',
    name: 'graph',
    component: GraphView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
