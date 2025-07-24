<template>
  <div>
    <h2>Step 1: Enter Your Text</h2>
    <textarea v-model="rawText" rows="4" cols="60"></textarea>

    <h2>Step 2: Convert to Editable Text</h2>
    <button @click="prepareText">Convert to Fill-in-the-Blank</button>

    <div v-if="segments.length">
      <h2>Step 3: Select a word to blank out</h2>
      <p>
        <span
          v-for="(segment, i) in segments"
          :key="i"
          @click="addBlank(i)"
          :style="{
            cursor: 'pointer',
            backgroundColor: segment.blank ? '#eef' : '',
          }"
        >
          <template v-if="segment.blank">
            <input
              v-model="answers[i]"
              class="blank-input"
              placeholder="Blank"
            />
          </template>
          <template v-else>
            {{ segment.text }}
          </template>
          <span> </span>
        </span>
      </p>
    </div>
  </div>
</template>

<script setup>
const rawText = ref("The quick brown fox jumps over the lazy dog");
const segments = ref([]);
const answers = ref([]);

function prepareText() {
  const words = rawText.value.split(" ");
  segments.value = words.map((word) => ({ text: word, blank: false }));
  answers.value = Array(words.length).fill("");
}

function addBlank(index) {
  // switches word btwn blank and the word when clicked
  if (!segments.value[index].blank) {
    segments.value[index].blank = true;
    answers.value[index] = "";
  } else {
    segments.value[index].blank = false;
    answers.value[index] = "";
  }
}
</script>
