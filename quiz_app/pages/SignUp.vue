<template>
  <div class="flex flex-col justify-around min-h-[50vh] p-5">
    <form @submit.prevent="handleSignup()" class="flex flex-col space-y-4">
      <input
        class="input mb-4 w-full"
        v-model="signupForm.email"
        type="email"
        placeholder="Email"
      />
      <input
        class="input mb-4 w-full"
        v-model="signupForm.password"
        type="password"
        placeholder="Password"
      />
      <input
        class="input mb-4 w-full"
        v-model="signupForm.username"
        type="text"
        placeholder="Username"
      />
      <button class="btn w-full" type="submit">Sign Up</button>
    </form>
    <p>
      <NuxtLink to="/LogIn">Already have an account? Try logging in</NuxtLink>
    </p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup lang="ts">
import type { UserForm } from "~/utils/types";
const signupForm = reactive<UserForm>({
  email: "",
  password: "",
  username: "",
});
const errorMessage = ref<string>("");
async function handleSignup() {
  const res = await $fetch("/api/submit", {
    method: "POST",
    body: {
      email: "admin@admin.com",
      password: "admin",
      username: "admin",
    },
  });
}
/* async function getData() {
  const { data } = await useFetch("http://127.0.0.1:8000/user/");
  console.log(data.value);
} */
/* onMounted(async () => {
  await handleSignup();
}); */
</script>

<style scoped></style>
