const botCreateAPI = "http://127.0.0.1:8000/tg-bot-api/bots/";
const userAPI = "http://127.0.0.1:8000/auth/users/me/"
const templates = document.querySelector('.templates')
const userNotAuth = document.querySelector('.not-auth')
const popupCloseBtn = document.querySelector('.btn-close-popup')
const createSuccess = document.querySelector('.create-success')

console.log(localStorage)
console.log(localStorage.getItem('authorization'))

function togglePopup(){
    const overlay = document.getElementById('popupOverlay');
    overlay.classList.toggle('show');
}

function toggleSuccess(){
    createSuccess.classList.toggle('active')
}

function templateChoice(objButton){
    localStorage.setItem('template', objButton.id)
    togglePopup()
}

function getToken(){
    return 'Token ' + localStorage.getItem('authorization')
}

async function getMe() {
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

            localStorage.setItem('uId', data.id)
        } else{
            throw new Error(res.statusText)
        }

    } catch(e){
        console.error(e)
    }
}

async function createBot(event){
    event.preventDefault();

    const form = event.target;
    const token = Object.fromEntries(new FormData(form).entries()).token
    const template = localStorage.getItem('template')
    localStorage.removeItem('template')
    let uId = localStorage.getItem('uId')

    toggleSuccess()

    if (!(uId)){
        await getMe()
        uId = localStorage.getItem('uId')
    }

    // try {
    //     const res = await fetch(botCreateAPI, {
    //         method: "POST",
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'Authorization': getToken()
    //         },
    //         body: JSON.stringify({
    //             'token': token,
    //             'is_active': true,
    //             'template': template,
    //             'user': uId
    //         })
    //     })

    //     if (res.ok){
    //         const data = await res.json()

    //         console.log(data)
    //     } else{
    //         const errors = await res.json()
    //         console.log(errors)
    //         throw new Error(res.statusText)
    //     }
    // } catch (e){
    //     console.error(e)
    // }
}

function authCheckFlag(){
    if (localStorage.getItem('authorization')) {
        console.log(localStorage)
        templates.classList.add('active')
    } else{
        userNotAuth.classList.add('active')
    }
}

authCheckFlag()