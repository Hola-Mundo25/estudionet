<template>
    
    <div class="bg-gray-800 text-gray-100 py-3.5 px-6 md:flex justify-between">
        
        <div class="flex item-center cursor-pointer">
            <span class="text-green text-xl mr-1">
                <i>lalal</i>
            </span>

            <h1 class="text-xl">matafuegos noble</h1>
        </div>

        <ul class="flex justify-end list-none p-0 m-0">
            <li class="md:mx-4" v-for="link in Links" :key="link.id">
                <a :href="link.link" class="text-xl hover:text-green-500 m-">{{link.name}}</a>
            </li>
        </ul>
    </div>

</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    setup() {
        let Links = [
            {name: "Home", link : "#"},
            {name: "Nosotros", link : "#"}
        ]
        return {Links}
    },
})
</script>
