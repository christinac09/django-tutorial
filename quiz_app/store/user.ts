import { ref, reactive, computed } from 'vue'
import { defineStore } from 'pinia'
import type {User} from '../types/types.ts'

export const useStore = defineStore('user', () => {
    const user = ref<User | null>(null)
    const isSignedIn = ref(false)
    
    async function signUp(email:string, password:string, username: string){
        //post - add new user to api

    }
    
    async function logIn(){
        //get - fetch from api
    }  

    function signOut() {
        isSignedIn.value = false
        user.value = null
      }
})