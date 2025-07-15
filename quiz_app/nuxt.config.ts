// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  modules: ['@nuxt/eslint'],
  runtimeConfig: {
    // The private keys which are only available server-side
    //apiSecret: '123',
    // Keys within public are also exposed client-side
    public: {
      apiBase: process.env.API_BASE_URL
    }
  }
})
