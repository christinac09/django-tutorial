<template>
  <div>
    <h2>{{ question.question }}</h2>
    <div></div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();
</script>

<style scoped></style>
