<template >
    <div class="list">
        <template v-for="(message, index) in mockMessages"  ::key="index">
            <UiCard :message="message" />
        </template>
    </div>
</template>
<script>
import UiCard from './ui-kit/UiCard.vue';
import getMessages from '../API/index'
export default {
    components: { UiCard },
    data() {
        return {
            messages : []
        }
    },
    beforeMount() {
        getMessages().then((resp) => {
            this.messages = resp
        })
    }
}
</script>
<style lang="">
    
</style>