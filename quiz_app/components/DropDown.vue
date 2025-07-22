<template>
  <div>
    <h2>{{ question.question }}</h2>
    <div>
      <ul class="space-y-3">
        <li v-for="(answer, index) in question.answer">
          <label for="">Blank {{ index + 1 }}: </label>
          <select name="" id="" v-model="selectedAnswers[index]">
            <option value="" disabled>Please select an answer</option>
            <option
              v-for="choice in shuffle([
                answer,
                ...(question.incorrect[index] || []),
              ])"
              :value="choice"
              :key="index"
            >
              {{ choice }}
            </option>
          </select>
        </li>
      </ul>
      <button type="submit" @click="selectAnswer()">Submit</button>
    </div>
  </div>
</template>

<script setup lang="ts">
//example
/* const question = <Question>{
  question: "djfajfjl [BLANK-1] jdslajfasldjfslkd [BLANK-2] jdfsalfjslfjd",
  answer: ["a1", "a2"],
  incorrect: [
    ["i1", "i1"],
    ["i2", "i2"],
  ],
  quiz: 1,
};
 */

const props = defineProps<{
  question: Question;
}>();

const selectedAnswers = ref<string>([]);
const { question } = toRefs(props);
const emit = defineEmits<{
  (e: "answerSelected", choice: string[]): void;
}>();

onMounted(() => {
  selectedAnswers.value = question.value.answer.map(() => "");
});

function selectAnswer(choice: string[]) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
