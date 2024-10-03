const userAPI = "http://127.0.0.1:8000/auth/users/me/"
const userInfo = document.querySelector('.user-info')
const userNotAuth = document.querySelector('.not-auth')

console.log(localStorage)
console.log(localStorage.getItem('authorization'))


function authCheckFlag(){
    if (localStorage.getItem('authorization')) {
        console.log(localStorage)
        return true
    }
    return false
}

function getToken(){
    return 'Token ' + localStorage.getItem('authorization')
}


async function getInfo() {
    if (!authCheckFlag()){
        userNotAuth.classList.add('active')
    } else{
        console.log('lol')
        // window.location.replace = "login.html";

        try{
            const res = await fetch(userAPI, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': getToken()
                }
            })

            if (res.ok){
                const data = await res.json()

                console.log(data)

                const email = document.querySelector('#email')
                const bots = document.querySelector('#bots')

                email.textContent = data.email
                bots.textContent = 0

                userInfo.classList.add('active')


            } else{
                throw new Error(res.statusText)
            }
        }catch (e) {
            console.error(e)
        }
    }
}

getInfo()