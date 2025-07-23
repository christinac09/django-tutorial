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
              v-for="choice in choices[index]"
              :value="choice"
              :key="index"
            >
              <!-- can't put shuffle here bc it'll run everythime component rerenders, which is when user interacts w/ dropdown since it messes up the order -->
              {{ choice }}
            </option>
          </select>
        </li>
      </ul>
      <!-- <button type="submit" @click="selectAnswer()">Submit</button> -->
    </div>
    <p>selected: {{ selectedAnswers }}</p>
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
const choices = computed(() => {
  return props.question.answer.map((correct, index) =>
    shuffle([correct, ...props.question.incorrect[index]])
  );
}); //choices is a list of the list of shuffled choices for each dropdown - like question.incorrect, but w correct answers
const selectedAnswers = ref<string[]>([]);
onMounted(() => {
  selectedAnswers.value = props.question.answer.map(() => "");
});
/* const emit = defineEmits<{
  (e: "answerSelected", choice: string[]): void;
}>();



function selectAnswer(choice: string[]) {
  emit("answerSelected", choice);
} */
</script>

<style scoped></style>
