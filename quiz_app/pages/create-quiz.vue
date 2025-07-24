<template>
  <div>
    <input type="text" placeholder="title" v-model="title" />
    <CreateQuestion v-for="question in questions" :type="question.type" />
    <select name="" id="" v-model="currentType">
      <option value="mc">Multiple Choice</option>
      <option value="tf">True or False</option>
      <option value="n">Numerical</option>
      <option value="dd" disabled>DropDown</option>
    </select>
    <button @click="addBlankQuestion(currentQuesCount, currentType)">
      Add Question
    </button>
    <p>Number of Questions: {{ currentQuesCount }}</p>
  </div>
</template>

<script setup lang="ts">
const title = ref("");
//const type = "tf";
const currentType = ref("");
const currentQuesCount = ref(0);
interface QuestionInstance {
  id: number;
  type: string;
}
const questions = ref<QuestionInstance[]>([]);
function addBlankQuestion(id: number, type: string) {
  currentQuesCount.value++;
  questions.value.push({ id: id, type: type });
  console.log(questions.value);
}
function deleteQuestion() {}
</script>

<style scoped></style>
