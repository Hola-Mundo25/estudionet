import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';

// Definición de las rutas
const routes = [
{
    path: '/',
    name: 'Home',
    component: Home
},
{
    path: '/about',
    name: 'About',
    component: About
}
];

// Crear el enrutador
const router = createRouter({
  history: createWebHistory(), // Usa el modo de historial del navegador
  routes, // Pasa las rutas definidas
});

export default router;