<template>
  <div>
    <input type="text" placeholder="title" v-model="title" />
    <CreateQuestion :type="type" />
  </div>
</template>

<script setup lang="ts">
const title = ref("");
const type = "mc";
</script>

<style scoped></style>
