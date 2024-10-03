const registerAPI = 'http://127.0.0.1:8000/auth/users/'
const loginAPI = 'http://127.0.0.1:8000/auth/token/login/'
const logoutAPI = 'http://127.0.0.1:8000/auth/token/logout/'

console.log(localStorage)
console.log(localStorage.getItem('authorization'))

async function register(event) {
    event.preventDefault()

    const form = event.target;
    const formData = Object.fromEntries(new FormData(form).entries())

    console.log(formData)

    const {email, password, repassword} = Object.fromEntries(new FormData(form).entries())
    console.log(email, password, repassword)

    try{
        const res = await fetch(registerAPI, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "email": email,
                "password": password,
                "re_password": repassword
            })
        })

        if (res.ok) {
            const data = await res.json()
            console.log(data)
        } else{
            const lol = await res.json()
            console.log(lol)
            throw new Error(res.statusText)
        }
    }
    catch (e){
        console.error(e)
    }
}

async function login(event) {
    event.preventDefault()

    const form = event.target;
    const formData = Object.fromEntries(new FormData(form).entries())

    console.log(formData)

    const {email, password} = Object.fromEntries(new FormData(form).entries())
    console.log(email, password)

    try {
        const res = await fetch(loginAPI, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        })

        if (res.ok) {
            const data = await res.json()
            console.log(data)
            localStorage.setItem('authorization', data['auth_token'])
            console.log('OK')
            console.log(localStorage)
        } else{
            const errors = await res.json()
            console.log(errors)
            throw new Error(res.statusText);
        }
    } catch (error) {
        console.error(error)
    }
}