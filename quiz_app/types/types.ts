interface User {
    id: string // ???
    username: string
    email: string
    role: string
}

interface UserForm {
    username: string
    email: string
    password: string
}

export type {User, UserForm}