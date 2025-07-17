<template>
  <div class="flex flex-col justify-around min-h-[50vh] p-5">
    <form @submit.prevent="" class="flex flex-col space-y-4">
      <input class="input mb-4 w-full" type="email" placeholder="Email" />
      <input class="input mb-4 w-full" type="password" placeholder="Password" />
      <input class="input mb-4 w-full" type="text" placeholder="Username" />
      <button class="btn w-full" type="submit">Sign Up</button>
    </form>
    <p><NuxtLink to="/LogIn">Go to login</NuxtLink></p>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from "vue";
import { useStore } from "../store/user";
</script>

<style scoped></style>
