<template>
<section class="main-section">
    <header class="main-header">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    </header>
    <nav class="main-nav">
    <button @click="navigateTo('home')" :class="{ active: currentPage === 'home' }">Inicio</button>
    <button @click="navigateTo('about')" :class="{ active: currentPage === 'about' }">Acerca de</button>
    <button @click="navigateTo('contact')" :class="{ active: currentPage === 'contact' }">Contacto</button>
    </nav>
    <div class="content">
    <component :is="currentComponent" />
    </div>
</section>
</template>

<script>
export default {
name: 'MainSection',
data() {
    return {
    title: 'Bienvenido a la Sección Principal',
    description: 'Esta es una breve descripción de la sección principal de nuestra aplicación.',
    currentPage: 'home', // Página por defecto
    };
},
computed: {
    currentComponent() {
    // Devuelve el componente basado en la página actual
    switch (this.currentPage) {
        case 'about':
        return 'AboutComponent';
        case 'contact':
        return 'ContactComponent';
        default:
        return 'HomeComponent';
    }
    },
},
methods: {
    navigateTo(page) {
    this.currentPage = page; // Cambia la página actual
    },
},
};
</script>

<style scoped>
.main-section {
max-width: 1200px;
margin: 0 auto;
padding: 20px;
}

.main-header {
text-align: center;
margin-bottom: 30px;
}

.main-header h1 {
font-size: 2.5em;
margin: 0;
}

.main-header p {
font-size: 1.2em;
color: #666;
}

.main-nav {
display: flex;
justify-content: center;
margin-bottom: 20px;
}

.main-nav button {
margin: 0 10px;
padding: 10px 20px;
font-size: 16px;
cursor: pointer;
border: none;
background-color: #eee;
transition: background-color 0.3s ease;
}

.main-nav button:hover {
background-color: #ddd;
}

.main-nav .active {
background-color: #007bff;
color: white;
}

.content {
padding: 20px;
background-color: #f9f9f9;
border-radius: 8px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>