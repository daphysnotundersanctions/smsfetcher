<template>
    <div class="ui-card">
        <div class="ui-card__title">
            {{ message.from }}
        </div>
        <div class="ui-card__value">
            {{ message.value }} 
            <UiCopy :value="message.value" />
        </div>
    </div>
</template>
<script>
import UiCopy from './UiCopy.vue';

export default {
    name: "UiCard",
    props: {
        message: {
            type: Array,
            default: () => []
        }
    },
    components: { UiCopy }
}
</script>
<style>
.ui-card {
    border-radius: 5px;
    border: 1px solid greenyellow;
    width: 300px;
}
</style>