<template >
    <div class="list">
        <template v-for="(message, index) in mockMessages"  ::key="index">
            <UiCard :message="message" />
        </template>
    </div>
</template>
<script>
import UiCard from './ui-kit/UiCard.vue';
import axios from 'axios'
import getMessages from '../API/index'
export default {
    components: { UiCard },
    data() {
        return {
            mockMessages : []
        }
    },
    beforeMount() {
        axios.get('http://127.0.0.1:8000/')   
    }
}
</script>
<style lang="">
    
</style>