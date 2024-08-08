<template>
    <div id="home_view">
    <HomeCarousel msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
  // @ is an alias to /src
import HomeCarousel from '@/components/HomeCarousel.vue';

export default {
    name: 'home_view',
    components: {
    HomeCarousel
}
}
</script>