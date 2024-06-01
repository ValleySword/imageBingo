import { createRouter, createWebHistory } from 'vue-router';

import Home from './pages/Home.vue';
import Search from './pages/Search.vue';
import BingoRule from './pages/bingo/BingoRule.vue';
import BingoGame3 from './pages/bingo/BingoGame3.vue';
import BingoGame5 from './pages/bingo/BingoGame5.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/search', component: Search },
  { path: '/bingoRule', component: BingoRule },
  { path: '/bingo3', component: BingoGame3 },
  { path: '/bingo5', component: BingoGame5 },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

// Vue.use(Router);

// export default new Router({
//   routes: [
//     // { path: '/', component: App },
//     { path: '/test', name: 'Test', component: Test },
//   ],
// });
