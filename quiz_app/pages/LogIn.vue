<template>
  <div class="flex flex-col justify-around min-h-[50vh] p-5">
    <form @submit.prevent="" class="flex flex-col space-y-4">
      <input class="input mb-4 w-full" type="email" placeholder="Email" />
      <input class="input mb-4 w-full" type="password" placeholder="Password" />
      <button class="btn w-full" type="submit">Log In</button>
    </form>
    <p><NuxtLink to="/SignUp">Go to signup</NuxtLink></p>
  </div>
</template>

<script setup lang="ts">
import type { UserForm } from "../types/types";
import { reactive } from "vue";

const loginForm = reactive<UserForm>({
  email: "",
  password: "",
  username: "",
});
</script>
