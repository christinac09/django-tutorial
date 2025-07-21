export interface User {
    id: number
    username: string
    email: string
    role: string
}

export interface UserForm {
    username: string
    email: string
    password: string
}

export interface Question {
    question: string
    answer: string[]
    incorrect: string[]
    quiz: number
}

export interface Quiz {
    id: number
    title: string
    creator: string
    //questions: Question[]
}