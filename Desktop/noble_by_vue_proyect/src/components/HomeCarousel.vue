<!-- src/components/Carousel.vue -->
<template>
    <div class="carousel">
      <div class="carousel-inner" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
        <div
        class="carousel-item"
        v-for="(image, index) in images"
        :key="index"
        :class="{ active: index === currentIndex }"
    >
        <img :src="image.src" :alt="image.alt" />
    </div>
    </div>
    <button class="carousel-control prev" @click="prevSlide">‹</button>
    <button class="carousel-control next" @click="nextSlide">›</button>
</div>
</template>

<script>
import { ref } from "vue";
// import CatApi from '@/services/CatApi';

export default {
    name: "CatCarousel",

    data() {
    return {
        images: [],
        }
    },

    methods : {

    setup(props) {
    const currentIndex = ref(0);

    const prevSlide = () => {
    currentIndex.value =
        currentIndex.value === 0 ? props.images.length - 1 : currentIndex.value - 1;
    };

    const nextSlide = () => {
    currentIndex.value =
        currentIndex.value === props.images.length - 1 ? 0 : currentIndex.value + 1;
    };

    return {
    currentIndex,
    prevSlide,
    nextSlide,
    };
}
}
}
</script>

<style scoped>
.carousel {
    position: relative;
    width: 100%;
    max-width: 600px;
    overflow: hidden;
    margin: auto;
}

.carousel-inner {
    display: flex;
    transition: transform 0.5s ease-in-out;
}

.carousel-item {
    min-width: 100%;
    transition: opacity 0.5s ease-in-out;
}

.carousel-item img {
    width: 100%;
    height: auto;
    display: block;
}

.carousel-control {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    z-index: 10;
}

.carousel-control.prev {
    left: 10px;
}

.carousel-control.next {
    right: 10px;
}
</style>  