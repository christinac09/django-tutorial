<template>
  <div class="card bg-slate-400">
    <!-- use v-if and props -->
    <h2>{{ count }}</h2>
    <div v-if="type === 'mc'">
      <form action="">
        <input type="text" placeholder="Question" />
        <input type="text" placeholder="Correct Answer" />
        <!-- make correct ans more visible ig -->
        <input v-for="n in 3" type="text" placeholder="Wrong Answer" :key="n" />
      </form>
    </div>
    <div v-if="type === 'tf'">
      <form>
        <input type="text" placeholder="Question" />
        <input type="radio" id="True" name="tf" value="True" />
        <label for="True">True</label><br />
        <input type="radio" id="False" name="tf" value="False" />
        <label for="False">False</label><br /><br />
        <input type="submit" value="Submit" />
      </form>
    </div>
    <div v-if="type === 'n'">
      <form action="">
        <input type="text" placeholder="Question" />
        <input type="number" placeholder="Correct Answer" />
      </form>
    </div>
    <!-- <div v-if="type === 'dd'">        DO LATER
      <form action=""></form>
      <button @click="addDropdown">add dropdown</button>
      <div v-for="word in sentence">     sentence = ["word", "word", "", "word", ""]
        <p v-if="word.length > 0">{{word}}</p>
        <input v-if="word.length === 0" type="text">
      </div>
    </div> -->
    <button class="" @click="removeCard">Remove</button>
  </div>
</template>

<script setup lang="ts">
//prop for type of question
const props = defineProps<{
  type: string;
  count: number;
}>();
/* function addDropdown() {} */
function removeCard() {}
</script>

<style scoped></style>
