<template >
    <div class="list">
        <template v-for="(message, index) in mockMessages"  ::key="index">
            <UiCard :message="message" />
        </template>
    </div>
</template>
<script>
import UiCard from './ui-kit/UiCard.vue';

export default {
    components: { UiCard },
    data() {
        return {
            mockMessages : [
                {
                    value : '564-100',
                    from : 'MTS'
                },
                {
                    value : '564-100',
                    from : 'MGTS'
                },
                {
                    value : '564-100',
                    from : 'Tele2'
                },
            ]
        }
    }
}
</script>
<style lang="">
    
</style>