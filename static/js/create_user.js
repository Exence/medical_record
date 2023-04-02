const LETTER_RU_EN_MATCH_PATTERN = new RegExp("^[а-яА-Яa-zA-Z\-]+$")
const LETTER_EN_MATCH_PATTERN = new RegExp("^[a-zA-Z\-]+$")

const form = document.querySelector('#validation-form')

form.addEventListener('submit', function (event) {
    if (!form.checkValidity()) {
        event.preventDefault()
    }
    form.classList.add('was-validated')
})

function login_validation()
{
    if (LETTER_EN_MATCH_PATTER.exec(document.querySelector('#login'))){
        return true
    }  
    return false
}
    
    

