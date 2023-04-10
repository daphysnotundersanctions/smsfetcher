<template >
    <div class="ui-copy" @click="copy(value)">
        <img src="../../assets/icons/copy.svg" alt="">        
    </div>
</template>
<script>
export default {
    name : "UiCopy",
    props : {
        value : {
            type : String || Number,
            require : true
        }
    },
    data () {
        return {
            copyState : false
        }
    },
    methods : {
        copy(value) {
            navigator.clipboard.writeText(value)
            .then(() => this.copyState = true && alert("Скопировано !"))
            .catch(error => alert(error))
        }
    }
}
</script>
<style>
.ui-copy {

}
</style>