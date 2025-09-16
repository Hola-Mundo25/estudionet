<template>
    <div id="home_view">
    <HomeCarousel msg="Welcome to Your Vue.js App"/>
    <HomeMain/>
    </div>
</template>

<script>
  // @ is an alias to /src
import HomeCarousel from '@/components/HomeCarousel.vue';
import HomeMain from '@/components/HomeMain.vue';

export default {
    name: 'home_view',
    components: {
    HomeCarousel,
    HomeMain
}
}
</script>