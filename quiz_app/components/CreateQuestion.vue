<template>
  <div>
    <!-- use v-if and props -->
    <div v-if="type === 'mc'">
      <form action="">
        <input type="text" placeholder="Question" />
        <input type="text" placeholder="Correct Answer" />
        <!-- make this more visible ig -->
        <input v-for="n in 3" type="text" placeholder="Wrong Answer" :key="n" />
      </form>
    </div>
    <div v-if="type === 'tf'">
      <form action="">
        <input type="text" placeholder="Question" />
        <input type="text" placeholder="Correct Answer" />
      </form>
    </div>
    <div v-if="type === 'n'">
      <form action="">
        <input type="text" placeholder="Question" />
        <input type="number" placeholder="Correct Answer" />
      </form>
    </div>
    <div v-if="type === 'dd'"></div>
  </div>
</template>

<script setup lang="ts">
//prop for type of question
const props = defineProps<{
  type: string;
}>();
</script>

<style scoped></style>
