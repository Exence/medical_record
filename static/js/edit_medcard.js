const medcard_num = document.querySelector('#general-button').value;
/* ALLERGY CONST */
const allergy_commit_modal_btn = document.querySelector('#allergy-commit-modal');
const allergy_close_modal_btn = document.querySelector('#allergy-close-modal');
const allergy_modal_header = document.querySelector('#allergyModalLabel');
const allergen = document.querySelector('#allergen-modal');
const allergy_type = document.querySelector('#allergyType-modal');
const start_age = document.querySelector('#allergyStartAge-modal');
const reaction_type = document.querySelector('#allergyReactionType-modal');
const diagnosis_date = document.querySelector('#allergyDiagnosisDate-modal');
const note = document.querySelector('#allergyNote-modal');

/* PARENTS CONST */
const parent_modal_header = document.querySelector('#parentModalLabel');
const parent_surname_inpt = document.querySelector('#surname-modal');
const parent_name_inpt = document.querySelector('#name-modal');
const parent_patronymic_inpt = document.querySelector('#patronymic-modal');
const parent_birthday_year_dtpkr = document.querySelector('#birthday_year');
const parent_edu_slct = document.querySelector('#education-modal');
const parent_phone_inpt = document.querySelector('#phone-modal');
const parent_close_modal_btn = document.querySelector('#parent-close-modal');
const parent_commit_modal_btn = document.querySelector('#parent-commit-modal');

/* EXTRA CLASSES CONST*/
const class_modal_header = document.querySelector('#classModalLabel');
const class_type_modal_inpt = document.querySelector('#class-type-modal');
const class_age_modal_inpt = document.querySelector('#class-age-modal');
const class_hours_modal_inpt = document.querySelector('#class-hours-modal');
const class_close_modal_btn = document.querySelector('#class-close-modal');
const class_commit_modal_btn = document.querySelector('#class-commit-modal');

/* DELETE WINDOW CONST*/
const delete_modal_header = document.querySelector('#deleteModalLabel');
const delete_commit_modal_btn = document.querySelector('#delete_modal_commit');
const close_delete_modal_btn = document.querySelector('#delete_close_modal');


/* ALLERGY */
allergy_commit_modal_btn.addEventListener('click', () => {
    var allergy = {
            "allergen": allergen.value,
            "allergy_type": allergy_type.value,
            "start_age": start_age.value,
            "reaction_type": reaction_type.value,
            "diagnosis_date": diagnosis_date.value,
            "note": note.value
        };

    switch (allergy_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/allergy/add",
                data: JSON.stringify({"json_data": allergy}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let allergy_block = document.querySelector('#allergy-block');
                    allergy_block.innerHTML += 
                    '<div name="div-'+ allergy["allergen"].replace(/ /g,'') +'" class="col-12 mb-3"></div>';
                    allergy_block = document.getElementsByName('div-'+ allergy["allergen"].replace(/ /g,''))[0];
                    allergy_block.innerHTML = '<p> <strong>Аллерген: </strong> <u><mark>'+ allergy["allergen"] +'</mark></u>, \
                    тип: <u><mark>'+ allergy["allergy_type"] +'</mark></u>, возраст начала: <u><mark>'+ allergy["start_age"] +'</mark></u>,\
                    тип реакции: <u><mark>'+ allergy["reaction_type"] +'</mark></u>, дата постановки диагноза: <u><mark>'+ allergy["diagnosis_date"] +'</mark></u>';
                    if (allergy["note"]) {
                        allergy_block.innerHTML += '</br><small>Примечание: <em>'+ allergy["note"] +'</em></small>'
                    }
                    allergy_block.innerHTML += '<div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#allergyModal" id="btn-update-'+ allergy["allergen"].replace(/ /g,'') +'" value="' + allergy["allergen"] + '///' + allergy["allergy_type"] + '///' + allergy["start_age"] + '///' + allergy["reaction_type"] + '///' + allergy["diagnosis_date"] + '///' + allergy["note"] + '" onclick="update_allergy(' + allergy["allergen"] + ')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" id="btn-delete-'+ allergy["allergen"].replace(/ /g,'') +'"  onclick="delete_allergy(\'' + allergy["allergen"] + '\')">Удалить</button>\
                    </div>'
                }
            });
            break;

        case 'update': 
            const allergen_name = allergy_close_modal_btn.value;
            allergy["prev_allergen"] = allergen_name;
            allergy["medcard_num"] = medcard_num;
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/allergy/update",
                data: JSON.stringify({"json_data": allergy}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let allergy_div = document.getElementsByName('div-' + allergen_name.replace(/ /g,''))[0]
                    allergy_div.innerHTML = '';
                    allergy_div.innerHTML = 
                    '<p> <strong>Аллерген: </strong> <u><mark>'+ allergy["allergen"] +'</mark></u>, \
                    тип: <u><mark>'+ allergy["allergy_type"] +'</mark></u>, возраст начала: <u><mark>'+ allergy["start_age"] +'</mark></u>,\
                    тип реакции: <u><mark>'+ allergy["reaction_type"] +'</mark></u>, дата постановки диагноза: <u><mark>'+ allergy["diagnosis_date"] +'</mark></u>';
                    if (allergy["note"]) {
                        allergy_div.innerHTML += '<small>Примечание: <em>'+ allergy["note"] +'</em></small>'
                    }
                    allergy_div.innerHTML += '<div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#allergyModal" id="btn-update-'+ allergy["allergen"].replace(/ /g,'') +'" value="' + allergy["allergen"] + '///' + allergy["allergy_type"] + '///' + allergy["start_age"] + '///' + allergy["reaction_type"] + '///' + allergy["diagnosis_date"] + '///' + allergy["note"] + '" onclick="update_allergy(\'' + allergy["allergen"] + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" id="btn-delete-'+ allergy["allergen"].replace(/ /g,'') +'" onclick="delete_allergy(\'' + allergy["allergen"] + '\')">Удалить</button>\
                    </div>';
                    allergy_div.setAttribute('name', 'div-' + allergy["allergen"].replace(/ /g,''));
                    allergy_div.setAttribute('id', 'div-' + allergy["allergen"].replace(/ /g,''));
                    
                }
            });
            break;
        default:
            break;
    }    
})

function add_allergy(){
    allergy_modal_header.innerHTML = 'Добавление данных об аллергии';
    allergy_commit_modal_btn.value = 'add';
    allergen.value = "";
    start_age.value = "";
    reaction_type.value = "";
    diagnosis_date.value = "";
    note.value = "";
}

function update_allergy(allergen_name){
    allergy_modal_header.innerHTML = 'Редактирование данных об аллергии';
    allergy_commit_modal_btn.value = 'update';
    allergy_close_modal_btn.value = allergen_name;
    const btn_caller = document.querySelector('#btn-update-' + allergen_name.replace(/ /g,''))
    allergy_data = btn_caller.value.split('///')
    allergen.value = allergy_data[0];
    allergy_type.value = allergy_data[1];
    start_age.value = allergy_data[2];
    reaction_type.value = allergy_data[3];
    diagnosis_date.value = allergy_data[4];
    note.value = allergy_data[5];
}

function delete_allergy(allergen_name){
    delete_modal_header.innerHTML = 'Удалить сведения об аллергии';
    close_delete_modal_btn.value = allergen_name;
    delete_commit_modal_btn.value = 'delete_allergy'
}


/*PARENTS*/
function parent_add_set_info(){
    parent_commit_modal_btn.value = 'add';
    parent_surname_inpt.value = "";
    parent_name_inpt.value = "";
    parent_patronymic_inpt.value = "";
    parent_birthday_year_dtpkr.value = "";
    parent_phone_inpt.value = "";
    
}

function father_add_btn_click(){
    parent_modal_header.innerHTML = 'Добавить сведения об отце';
    parent_close_modal_btn.value = 'father';
    parent_add_set_info();
}

function mother_add_btn_click() {
    parent_modal_header.innerHTML = 'Добавить сведения о матери';
    parent_close_modal_btn.value = 'mother';
    parent_add_set_info();
}

function parent_update_set_info(unsplit_data){
    parent_data = unsplit_data.split('///');
    parent_surname_inpt.value = parent_data[1];
    parent_name_inpt.value = parent_data[2];
    parent_patronymic_inpt.value = parent_data[3];
    parent_birthday_year_dtpkr.value = parent_data[4];
    parent_edu_slct.value = parent_data[5].trim();
    parent_phone_inpt.value = parent_data[6].slice(1,11);
    parent_commit_modal_btn.value = 'update';
    parent_close_modal_btn.value = parent_data[0];
}

function father_update_btn_click(){
    parent_modal_header.innerHTML = 'Редактирование сведений об отце';
    let father_update_btn = document.getElementsByName('update-father-btn')[0]
    parent_update_set_info(father_update_btn.value);
}

function mother_update_btn_click(){
    parent_modal_header.innerHTML = 'Редактирование сведений о матери';
    let mother_update_btn = document.getElementsByName('update-mother-btn')[0];
    parent_update_set_info(mother_update_btn.value);
}

parent_commit_modal_btn.addEventListener('click', () => {
    var parent = {
        "surname": parent_surname_inpt.value,
        "name": parent_name_inpt.value,
        "patronymic": parent_patronymic_inpt.value,
        "birthday_year": parent_birthday_year_dtpkr.value,
        "education": parent_edu_slct.value,
        "phone_num": '8' + parent_phone_inpt.value,
        "header": parent_modal_header.innerHTML
    };
    switch (parent_commit_modal_btn.value) {
        case 'add':
            parent["parent_type"] = parent_close_modal_btn.value;
            parent["medcard_num"] = medcard_num;
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/parent/add",
                data: JSON.stringify({"json_data": parent}),
                contentType: "application/json",
                dataType: 'json',
                success: function(parent_data) {
                    parent["id"] = parent_data.id;
                    switch (parent.parent_type) {
                        case 'father':
                            father_div = document.getElementsByName('father-main-div')[0]
                            father_div.innerHTML = '<div name="div-father-' + parent.id + '" class="col-12 mb-3">\
                            <p><strong>Отец: </strong> <u><mark>' + parent.surname + ' ' +  parent.name + ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-father-btn" value="' + parent.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'" onclick="father_update_btn_click()">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-father-btn" value="' + parent.id + '" onclick="delete_parent(\'father\')">Удалить</button>\
                            </div>\
                            </div>'
                            break;
                        
                        case 'mother':
                            mother_div = document.getElementsByName('mother-main-div')[0]
                            mother_div.innerHTML = '<div name="div-mother-' + parent.id + '" class="col-12 mb-3">\
                            <p><strong>Мать: </strong> <u><mark>' + parent.surname + ' ' +  parent.name + ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-mother-btn" value="' + parent.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'" onclick="mother_update_btn_click()">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mother-btn" value="' + parent.id + '" onclick="delete_parent(\'mother\')">Удалить</button>\
                            </div>\
                            </div>'
                            break;
                    
                        default:
                            break;
                    }
                }
            });

            break;
        
        
        case 'update':
            parent["id"] = parent_close_modal_btn.value;
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/parent/update",
                data: JSON.stringify({"json_data": parent}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    switch (parent.header) {
                        case 'Редактирование сведений об отце':
                            father_div = document.getElementsByName('div-father-' + parent.id)[0]
                            father_div.innerHTML = '<p><strong>Отец: </strong> <u><mark>' + parent.surname + ' ' +  parent.name+ ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-father-btn" value="' + parent.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-father-btn" value="' + parent.id + '" onclick="delete_parent(\'father\')">Удалить</button>\
                            </div>'
                            break;
                        
                        case 'Редактирование сведений о матери':
                            mother_div = document.getElementsByName('div-mother-' + parent.id)[0]
                            mother_div.innerHTML = '<p><strong>Мать: </strong> <u><mark>' + parent.surname + ' ' +  parent.name+ ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-mother-btn" value="' + parent.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mother-btn" ' + parent.id + '" onclick="delete_parent(\'mother\')">Удалить</button>\
                            </div>'
                            break;
                    
                        default:
                            break;
                    }
                }
            });
            break;
    
        default:
            break;
    }
})

function delete_parent(parent_type){
    switch (parent_type) {
        case 'father':
            delete_modal_header.innerHTML = 'Удалить сведения об отце';
            let father_delete_btn = document.getElementsByName('delete-father-btn')[0];
            close_delete_modal_btn.value = father_delete_btn.value;
            break;
        
        case 'mother':
            delete_modal_header.innerHTML = 'Удалить сведения о матери';
            let mother_delete_btn = document.getElementsByName('delete-mother-btn')[0];
            close_delete_modal_btn.value = mother_delete_btn.value;
            break;

        default:
            break;
    }
        
    delete_commit_modal_btn.value = 'delete_parent'
}


/* EXTRA CLASSES */
function class_add_set_info(){
    class_modal_header.innerHTML = "Добавление сведений о доп. занятиях";
    class_commit_modal_btn.value = 'add';
    class_type_modal_inpt.value = "Музыка";
    class_age_modal_inpt.value = "3";
    class_hours_modal_inpt.value = "5";    
}

function update_class(class_type, class_age, class_hours){
    class_modal_header.innerHTML = "Редактирование сведений о доп. занятиях";
    class_commit_modal_btn.value = 'update';
    class_close_modal_btn.value = class_type + '///' + class_age;
    class_type_modal_inpt.value = class_type;
    class_age_modal_inpt.value = class_age;
    class_hours_modal_inpt.value = class_hours;
}

function delete_class(class_type, class_age){
    delete_modal_header.innerHTML = 'Удалить сведения о доп. занятиях';
    close_delete_modal_btn.value = class_type + '///' + class_age;
    delete_commit_modal_btn.value = 'delete_extra_class'
}

class_commit_modal_btn.addEventListener('click', () =>{
    var extra_class = {
        "medcard_num": medcard_num,
        "classes_type": class_type_modal_inpt.value,
        "age": class_age_modal_inpt.value,
        "hours_on_week": class_hours_modal_inpt.value
    }
    switch (class_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/extra_class/add",
                data: JSON.stringify({"json_data": extra_class}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let extra_classes_div = document.querySelector('#extra-classes-main-div')
                    extra_classes_div.innerHTML += '<div name="div-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '" class="col-12 mb-3">\
                    <p><strong>' + extra_class.classes_type + '</strong> в возрасте: <u><mark>' + extra_class.age + '</mark></u> по <u><mark>' + extra_class.hours_on_week + '</mark></u> ч/нед.</p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#classModal" name="update-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="update_class(\'' + extra_class.classes_type +'\', \'' + extra_class.age + '\', \'' + extra_class.hours_on_week + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="">Удалить</button>\
                    </div>\
                </div>'
                }
            });
            break;

            case 'update':
                let old_extra_classes_data = class_close_modal_btn.value.split('///');
                extra_class["old_classes_type"] = old_extra_classes_data[0];
                extra_class["old_age"] = old_extra_classes_data[1];
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/extra_class/update",
                    data: JSON.stringify({"json_data": extra_class}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let extra_classes_div = document.getElementsByName('div-class-' + extra_class.old_classes_type.replace(/ /g,'') + '-' + extra_class.old_age)[0];
                        extra_classes_div.innerHTML = '<p><strong>' + extra_class.classes_type + '</strong> в возрасте: <u><mark>' + extra_class.age + '</mark></u> по <u><mark>' + extra_class.hours_on_week + '</mark></u> ч/нед.</p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#classModal" name="update-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="update_class(\'' + extra_class.classes_type +'\', \'' + extra_class.age + '\', \'' + extra_class.hours_on_week + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="">Удалить</button>\
                        </div>';
                        extra_classes_div.setAttribute('name', 'div-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age) 
                    }
                });
                break;
    
        default:
            break;
    }
})



/* DELETE MODAL WINDOW*/
delete_commit_modal_btn.addEventListener('click', () => {    
    switch (delete_commit_modal_btn.value) {
        case 'delete_allergy':
            allergy = {
                "allergen": close_delete_modal_btn.value,
                "medcard_num": medcard_num
            };
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/allergy/delete",
                data: JSON.stringify({"json_data": allergy}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var allergy_div = document.getElementsByName('div-' + close_delete_modal_btn.value.replace(/ /g,''))[0];
                    allergy_div.remove();
                }
            });

            break;

        case 'delete_parent':
            parent = {
                "id": close_delete_modal_btn.value
            };
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/parent/delete",
                data: JSON.stringify({"json_data": parent}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    switch (delete_modal_header.innerHTML) {
                        case 'Удалить сведения об отце':
                            var parent_div = document.getElementsByName('father-main-div')[0];
                            parent_div.innerHTML = '<button type="button" class="btn btn-outline-primary my-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="add-father-btn" onclick="father_add_btn_click()">Добавить сведения об отце</button>'
                            break;

                        case 'Удалить сведения о матери':
                            var parent_div = document.getElementsByName('mother-main-div')[0];
                            parent_div.innerHTML = '<button type="button" class="btn btn-outline-primary my-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="add-mother-btn" onclick="mother_add_btn_click()">Добавить сведения о матери</button>'
                            break;
                    
                        default:
                            break;
                    }
                }
            });
            
            break;

        case 'delete_extra_class':
            extra_class_data = close_delete_modal_btn.value.split('///')
            extra_class = {
                "medcard_num": medcard_num,
                "classes_type": extra_class_data[0],
                "age": extra_class_data[1]
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/extra_class/delete",
                data: JSON.stringify({"json_data": extra_class}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var extra_classes_div = document.getElementsByName('div-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age)[0];
                    extra_classes_div.remove();
                }
            });
            
            break;
    
        default:
            break;
    }

})
