const form = document.querySelector('#validation-form')
const father_btn = document.querySelector('#create-father-btn')
const father_input = document.querySelector('#father-input')
const mother_btn = document.querySelector('#create-mother-btn')
const mother_input = document.querySelector('#mother-input')
const modal_lable = document.querySelector('#parentModalLabel')
const modal_commit_btn = document.querySelector('#modal-commit')
const modal_only_letters_inputs = document.querySelectorAll('.only-letters-modal')
const birthday_year_input = document.querySelector('#birthday_year')
const phone_input = document.querySelector('#phone-modal')
const education_selector = document.querySelector('#education-modal')

form.addEventListener('submit', function (e) {
    if (!form.checkValidity()) {
        e.preventDefault()
    }
    form.classList.add('was-validated')
})

father_btn.addEventListener('click', () => {
    modal_lable.textContent = 'Внести данные об отце'
})

mother_btn.addEventListener('click', () => {
    modal_lable.textContent = 'Внести данные о матери'
})

modal_commit_btn.addEventListener('click', function(e){
    var check = true;
    modal_only_letters_inputs.forEach(input => {
        if (input.value.length === 0 || input.value.length > 139) {
            check = false;
            input.classList.add("is-invalid");
        }
    })

    if (birthday_year_input.value.length != 4){
        check = false;
        birthday_year_input.classList.add("is-invalid");
    }

    if (phone_input.value.length != 10){
        check = false;
        phone_input.classList.add("is-invalid");
    }

    if (!check){
        e.preventDefault()
    } else {
        result = "";
        modal_only_letters_inputs.forEach(input => {
            result += input.value + ";";
            input.value = "";
            input.classList.remove("is-valid");
        });
        result += birthday_year_input.value + ";" +  education_selector.value + ";8" + phone_input.value;
        birthday_year_input.value = "";
        birthday_year_input.classList.remove("is-valid");
        phone_input.value = "";
        phone_input.classList.remove("is-valid");
        if (modal_lable.textContent == 'Внести данные об отце'){
            father_input.value = result;
        } else {
            mother_input.value = result;
        }
    }   
    
})
