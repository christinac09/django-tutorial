<template>
  <div class="flex flex-col justify-around min-h-[50vh] p-5">
    <form @submit.prevent="handleLogin" class="flex flex-col space-y-4">
      <input
        class="input mb-4 w-full"
        v-model="loginForm.email"
        type="email"
        placeholder="Email"
      />
      <input
        class="input mb-4 w-full"
        v-model="loginForm.password"
        type="password"
        placeholder="Password"
      />
      <button class="btn w-full" type="submit">Log In</button>
    </form>
    <p>
      <NuxtLink to="/SignUp">Don't have an account? Try signing up</NuxtLink>
    </p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup lang="ts">
import { requestEndpoint } from "~/utils/functions";

const loginForm = reactive<UserForm>({
  email: "admin@admin.com",
  password: "admin",
  username: "",
});

const errorMessage = ref("");

async function handleLogin() {
  const token = await requestEndpoint("/api/token/", "POST", {
    email: "admin@admin.com",
    password: "admin",
  });
  console.log(token);
  // call function from pinia
}

onMounted(async () => {
  await handleLogin();
});
</script>
