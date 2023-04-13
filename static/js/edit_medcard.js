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

/*********************************************************************************************/
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

/* EXTRA CLASSES CONST */
const class_modal_header = document.querySelector('#classModalLabel');
const class_type_modal_inpt = document.querySelector('#class-type-modal');
const class_age_modal_inpt = document.querySelector('#class-age-modal');
const class_hours_modal_inpt = document.querySelector('#class-hours-modal');
const class_close_modal_btn = document.querySelector('#class-close-modal');
const class_commit_modal_btn = document.querySelector('#class-commit-modal');

/* PAST ILLNESSES CONST */
const past_illness_modal_header = document.querySelector('#pastIllnessModalLabel');
const past_illness_diagnosis_modal_inpt = document.querySelector('#pastIllnessDiagnosis-modal');
const past_illness_start_date_modal_dtpkr = document.querySelector('#pastIllnessStartDate-modal');
const past_illness_end_date_modal_dtpkr = document.querySelector('#pastIllnessEndDate-modal');
const past_illness_close_modal_btn = document.querySelector('#pastIllness-close-modal');
const past_illness_commit_modal_btn = document.querySelector('#pastIllness-commit-modal');

/* HOSPITALIZATION CONST */
const hospitalization_modal_header = document.querySelector('#hospitalizationModalLabel');
const hospitalization_diagnosis_modal_txt = document.querySelector('#hospitalizationDiagnosis-modal');
const hospitalization_start_date_modal_dtpkr = document.querySelector('#hospitalizationStartDate-modal');
const hospitalization_end_date_modal_dtpkr = document.querySelector('#hospitalizationEndDate-modal');
const hospitalization_founding_modal_inpt = document.querySelector('#hospitalizationFounding-modal');
const hospitalization_close_modal_btn = document.querySelector('#hospitalization-close-modal');
const hospitalization_commit_modal_btn = document.querySelector('#hospitalization-commit-modal');

/* SPA TREATMENT CONST */
const spa_treatment_modal_header = document.querySelector('#spaTreatmentModalLabel');
const spa_treatment_diagnosis_modal_txt = document.querySelector('#spaTreatmentDiagnosis-modal');
const spa_treatment_start_date_modal_dtpkr = document.querySelector('#spaTreatmentStartDate-modal');
const spa_treatment_end_date_modal_dtpkr = document.querySelector('#spaTreatmentEndDate-modal');
const spa_treatment_founding_modal_inpt = document.querySelector('#spaTreatmentFoundingSpecialization-modal');
const spa_treatment_climatic_zone_modal_slct = document.querySelector('#spaTreatmentClimaticZone-modal');
const spa_treatment_close_modal_btn = document.querySelector('#spaTreatment-close-modal');
const spa_treatment_commit_modal_btn = document.querySelector('#spaTreatment-commit-modal');

/* MEDICAL CERTIFICATES CONST */
const medical_certificate_modal_header = document.querySelector('#medicalCertificateModalLabel');
const medical_certificate_disease_modal_inpt = document.querySelector('#medicalCertificateDisease-modal');
const medical_certificate_start_date_modal_dtpkr = document.querySelector('#medicalCertificateStartDate-modal');
const medical_certificate_end_date_modal_dtpkr = document.querySelector('#medicalCertificateEndDate-modal');
const medical_certificate_infection_contact_modal_chk = document.querySelector('#medicalCertificateInfectionContact-modal');
const medical_certificate_sport_exemption_date_modal_dpkr = document.querySelector('#medicalCertificateSportExemptionDate-modal');
const medical_certificate_vac_exemption_date_modal_dpkr = document.querySelector('#medicalCertificateVacExemptionDate-modal');
const medical_certificate_doctor_modal_inpt = document.querySelector('#medicalCertificateDoctor-modal');
const medical_certificate_cert_date_modal_dtpkr = document.querySelector('#medicalCertificateCertDate-modal');
const medical_certificate_close_modal_btn = document.querySelector('#medicalCertificate-close-modal');
const medical_certificate_commit_modal_btn = document.querySelector('#medicalCertificate-commit-modal');

/*********************************************************************************************/
/* DISPENSARY CONST */
const dispensary_modal_header = document.querySelector('#dispensaryModalLabel');
const dispensary_diagnosis_modal_inpt = document.querySelector('#dispensaryDiagnosis-modal');
const dispensary_specialist_modal_inpt = document.querySelector('#dispensarySpecialist-modal');
const dispensary_start_date_modal_dtpkr = document.querySelector('#dispensaryStartDate-modal');
const dispensary_end_date_modal_dtpkr = document.querySelector('#dispensaryEndDate-modal');
const dispensary_end_reason_modal_txt = document.querySelector('#dispensaryEndReason-modal');
const dispensary_close_modal_btn = document.querySelector('#dispensary-close-modal');
const dispensary_commit_modal_btn = document.querySelector('#dispensary-commit-modal');

/* VISIT SPECIALIST CONTROL CONST*/
const visit_specialist_control_modal_header = document.querySelector('#visitSpecialistControlModalLabel');
const visit_specialist_control_assigned_date_modal_dtpkr = document.querySelector('#visitSpecialistControlAssignedDate-modal');
const visit_specialist_control_fact_date_modal_dtpkr = document.querySelector('#visitSpecialistControlFactDate-modal');
const visit_specialist_control_close_modal_btn = document.querySelector('#visit-specialist-control-close-modal');
const visit_specialist_control_commit_modal_btn = document.querySelector('#visit-specialist-control-commit-modal');
const visit_specialist_control_add_btn = document.querySelector('#add-visit-specialist-control-btn');

/*********************************************************************************************/
/* DEWORMING CONST */
const deworming_modal_header = document.querySelector('#dewormingModalLabel');
const deworming_date_modal_dtpkr = document.querySelector('#dewormingDate-modal');
const deworming_result_modal_txt = document.querySelector('#dispensaryResult-modal');
const deworming_close_modal_btn = document.querySelector('#deworming-close-modal');
const deworming_commit_modal_btn = document.querySelector('#deworming-commit-modal');

/* SANATION CONST */
const oral_sanation_modal_header = document.querySelector('#oralSanationModalLabel');
const oral_sanation_date_modal_dtpkr = document.querySelector('#oralSanationDate-modal');
const oral_sanation_dental_result_modal_txt = document.querySelector('#oralSanationDentalResult-modal')
const oral_sanation_result_modal_txt = document.querySelector('#oralSanationResult-modal');
const oral_sanation_close_modal_btn = document.querySelector('#oral-sanation-close-modal');
const oral_sanation_commit_modal_btn = document.querySelector('#oral-sanation-commit-modal');


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
    class_type_modal_inpt.value = "";
    class_age_modal_inpt.value = "";
    class_hours_modal_inpt.value = "";    
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


/* PAST ILLNESS */
function past_illness_add_set_info(){

    past_illness_modal_header.innerHTML = "Добавление сведений о перенесенном заболевании";
    past_illness_diagnosis_modal_inpt.value = "Ветряная оспа";
    past_illness_start_date_modal_dtpkr.value = "2022-01-01";
    past_illness_end_date_modal_dtpkr.value = "2022-01-21";
    past_illness_commit_modal_btn.value = 'add'; 
}

function update_past_illness(diagnosis, start_date){
    var past_illness = {
        "medcard_num": medcard_num,
        "diagnosis": diagnosis,
        "start_date": start_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/past_illness/get",
        data: JSON.stringify({"json_data": past_illness}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            past_illness_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            past_illness_commit_modal_btn.value = 'update';
            past_illness_close_modal_btn.value = past_illness.diagnosis + '///' + past_illness.start_date;
            past_illness_diagnosis_modal_inpt.value = past_illness.diagnosis;
            past_illness_start_date_modal_dtpkr.value = past_illness.start_date;
            past_illness_end_date_modal_dtpkr.value = data.past_illness.end_date;
        }
    });    
}

function delete_past_illness(diagnosis, start_date){
    delete_modal_header.innerHTML = 'Удалить сведения о перенесенном заболевании';
    close_delete_modal_btn.value = diagnosis + '///' + start_date;
    delete_commit_modal_btn.value = 'delete_past_illness'
}

past_illness_commit_modal_btn.addEventListener('click', () =>{
    var past_illness = {
        "medcard_num": medcard_num,
        "diagnosis": past_illness_diagnosis_modal_inpt.value,
        "start_date": past_illness_start_date_modal_dtpkr.value,
        "end_date": past_illness_end_date_modal_dtpkr.value
    }
    switch (past_illness_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/past_illness/add",
                data: JSON.stringify({"json_data": past_illness}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let past_illness_div = document.querySelector('#past-illnesses-main-div')
                    past_illness_div.innerHTML += '<div name="div-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date + '" class="col-12 mb-3">\
                    <p><strong>' + past_illness.diagnosis  + '</strong> с <u><mark>' + past_illness.start_date + '</mark></u> по <u><mark>' + past_illness.end_date + '</mark></u> </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#pastIllnessModal" name="update-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date + '-btn" onclick="update_past_illness(\'' + past_illness.diagnosis + '\', \'' + past_illness.start_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date + '-btn" onclick="delete_past_illness(\'' + past_illness.diagnosis + '\', \'' + past_illness.start_date + '\')">Удалить</button>\
                    </div>\
                </div>'
                }
            });
            break;

            case 'update':
                let old_past_illness_data = past_illness_close_modal_btn.value.split('///');
                past_illness["old_diagnosis"] = old_past_illness_data[0];
                past_illness["old_start_date"] = old_past_illness_data[1];
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/past_illness/update",
                    data: JSON.stringify({"json_data": past_illness}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let past_illness_div = document.getElementsByName('div-past-illness-' + past_illness.old_diagnosis.replace(/ /g, '') + '-' + past_illness.old_start_date)[0]
                        past_illness_div.innerHTML = '<p><strong>' + past_illness.diagnosis  + '</strong> с <u><mark>' + past_illness.start_date + '</mark></u> по <u><mark>' + past_illness.end_date + '</mark></u> </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#pastIllnessModal" name="update-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date + '-btn" onclick="update_past_illness(\'' + past_illness.diagnosis + '\', \'' + past_illness.start_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date + '-btn" onclick="delete_past_illness(\'' + past_illness.diagnosis + '\', \'' + past_illness.start_date + '\')">Удалить</button>\
                        </div>';
                        past_illness_div.setAttribute('name', 'div-past-illness-' + past_illness.diagnosis.replace(/ /g, '') + '-' + past_illness.start_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})

/* HOSPITALIZATION */
function hospitalization_add_set_info(){

    hospitalization_modal_header.innerHTML = "Добавление сведений о госпитализации";
    hospitalization_diagnosis_modal_txt.value = "";
    hospitalization_start_date_modal_dtpkr.value = new Date();
    hospitalization_end_date_modal_dtpkr.value = new Date();
    hospitalization_founding_modal_inpt.value = ""
    hospitalization_commit_modal_btn.value = 'add'; 
}

function update_hospitalization(start_date){
    var hospitalization = {
        "medcard_num": medcard_num,
        "start_date": start_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/hospitalization/get",
        data: JSON.stringify({"json_data": hospitalization}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            hospitalization_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            hospitalization_commit_modal_btn.value = 'update';
            hospitalization_close_modal_btn.value = data.hospitalization.start_date;
            hospitalization_diagnosis_modal_txt.value = data.hospitalization.diagnosis;
            hospitalization_start_date_modal_dtpkr.value = data.hospitalization.start_date;
            hospitalization_end_date_modal_dtpkr.value = data.hospitalization.end_date;
            hospitalization_founding_modal_inpt.value = data.hospitalization.founding;
        }
    });    
}

function delete_hospitalization(start_date){
    delete_modal_header.innerHTML = 'Удалить сведения о перенесенном заболевании';
    close_delete_modal_btn.value = start_date;
    delete_commit_modal_btn.value = 'delete_hospitalization'
}

hospitalization_commit_modal_btn.addEventListener('click', () =>{
    var hospitalization = {
        "medcard_num": medcard_num,
        "diagnosis": hospitalization_diagnosis_modal_txt.value,
        "start_date": hospitalization_start_date_modal_dtpkr.value,
        "end_date": hospitalization_end_date_modal_dtpkr.value,
        "founding": hospitalization_founding_modal_inpt.value
    }
    switch (hospitalization_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/hospitalization/add",
                data: JSON.stringify({"json_data": hospitalization}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let hospitalization_div = document.querySelector('#hospitalizations-main-div')
                    hospitalization_div.innerHTML += '<div name="div-hospitalization-' + hospitalization.start_date + '" class="col-12 mb-3">\
                    <p>С <u><mark>' + hospitalization.start_date + '</mark></u> по <u><mark>' + hospitalization.end_date + '</mark></u> <br>\
                    <strong>Диагноз, вид вмешательства: </strong><u><mark>' + hospitalization.diagnosis + '</mark></u> <br>\
                    <strong>Учреждение: </strong><u><mark>' + hospitalization.founding + '</mark></u></p>\
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                    <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#hospitalizationModal" name="update-hospitalization-' + hospitalization.start_date + '-btn" onclick="update_hospitalization(\'' + hospitalization.start_date + '\')">Редактировать</button>\
                    <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-hospitalization-' + hospitalization.start_date + '-btn" onclick="delete_hospitalization(\'' + hospitalization.start_date + '\')">Удалить</button>\
                </div>\
                </div>'
                }
            });
            break;

            case 'update':
                hospitalization["old_start_date"] = hospitalization_close_modal_btn.value;
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/hospitalization/update",
                    data: JSON.stringify({"json_data": hospitalization}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let hospitalization_div = document.getElementsByName('div-hospitalization-' + hospitalization.old_start_date)[0]
                        hospitalization_div.innerHTML = '<p>С <u><mark>' + hospitalization.start_date + '</mark></u> по <u><mark>' + hospitalization.end_date + '</mark></u> <br>\
                        <strong>Диагноз, вид вмешательства: </strong><u><mark>' + hospitalization.diagnosis + '</mark></u> <br>\
                        <strong>Учреждение: </strong><u><mark>' + hospitalization.founding + '</mark></u></p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#hospitalizationModal" name="update-hospitalization-' + hospitalization.start_date + '-btn" onclick="update_hospitalization(\'' + hospitalization.start_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-hospitalization-' + hospitalization.start_date + '-btn" onclick="delete_hospitalization(\'' + hospitalization.start_date + '\')">Удалить</button>\
                    </div>';
                        hospitalization_div.setAttribute('name', 'div-hospitalization-' + hospitalization.start_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})

/* SPA TREATMENT */
function spa_treatment_add_set_info(){

    spa_treatment_modal_header.innerHTML = "Добавление сведений о санаторно-курортном лечении";
    spa_treatment_diagnosis_modal_txt.value = "";
    spa_treatment_start_date_modal_dtpkr.value = "2023-01-01";
    spa_treatment_end_date_modal_dtpkr.value = "2023-01-01";
    spa_treatment_founding_modal_inpt.value = ""
    spa_treatment_commit_modal_btn.value = 'add'; 
}

function update_spa_treatment(start_date){
    var spa_treatment = {
        "medcard_num": medcard_num,
        "start_date": start_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/spa_treatment/get",
        data: JSON.stringify({"json_data": spa_treatment}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            spa_treatment_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            spa_treatment_commit_modal_btn.value = 'update';
            spa_treatment_close_modal_btn.value = data.spa_treatment.start_date;
            spa_treatment_diagnosis_modal_txt.value = data.spa_treatment.diagnosis;
            spa_treatment_start_date_modal_dtpkr.value = data.spa_treatment.start_date;
            spa_treatment_end_date_modal_dtpkr.value = data.spa_treatment.end_date;
            spa_treatment_founding_modal_inpt.value = data.spa_treatment.founding_specialization;
            spa_treatment_climatic_zone_modal_slct.value = data.spa_treatment.climatic_zone;
        }
    });    
}

function delete_spa_treatment(start_date){
    delete_modal_header.innerHTML = 'Удалить сведения о санаторно-курортном лечении';
    close_delete_modal_btn.value = start_date;
    delete_commit_modal_btn.value = 'delete_spa_treatment'
}

spa_treatment_commit_modal_btn.addEventListener('click', () =>{
    var spa_treatment = {
        "medcard_num": medcard_num,
        "diagnosis": spa_treatment_diagnosis_modal_txt.value,
        "start_date": spa_treatment_start_date_modal_dtpkr.value,
        "end_date": spa_treatment_end_date_modal_dtpkr.value,
        "founding_specialization": spa_treatment_founding_modal_inpt.value,
        "climatic_zone": spa_treatment_climatic_zone_modal_slct.value
    }
    switch (spa_treatment_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/spa_treatment/add",
                data: JSON.stringify({"json_data": spa_treatment}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-spa-treatment-' + spa_treatment.start_date + '" class="col-12 mb-3">\
                    <p>С <u><mark>' + spa_treatment.start_date + '</mark></u> по '
                    if (spa_treatment.end_date){
                        innerHTML += '<u><mark>' + spa_treatment.end_date + '</mark></u>'
                    } else {
                        innerHTML += '<u><mark>настоящее время</mark></u>'
                    }
                    innerHTML += '<br>\
                    <strong>Диагноз, вид вмешательства: </strong><u><mark>' + spa_treatment.diagnosis + '</mark></u> <br>\
                    <strong>Специализация учреждения: </strong><u><mark>' + spa_treatment.founding_specialization + '</mark></u><br>\
                    <strong>Климатическая зона учреждения: </strong><u><mark>' + spa_treatment.climatic_zone + '</mark></u>\
                </p>\
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                    <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#spaTreatmentModal" name="update-spa-treatment-' + spa_treatment.start_date + '-btn" onclick="update_spa_treatment(\'' + spa_treatment.start_date + '\')">Редактировать</button>\
                    <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-spa-treatment-' + spa_treatment.start_date + '-btn" onclick="delete_spa_treatment(\'' + spa_treatment.start_date + '\')">Удалить</button>\
                </div>\
                </div>'
                    let spa_treatment_div = document.querySelector('#spa-treatments-main-div')
                    spa_treatment_div.innerHTML += innerHTML
                }
            });
            break;

            case 'update':
                spa_treatment["old_start_date"] = spa_treatment_close_modal_btn.value;
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/spa_treatment/update",
                    data: JSON.stringify({"json_data": spa_treatment}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>С <u><mark>' + spa_treatment.start_date + '</mark></u> по '
                            if (spa_treatment.end_date){
                                innerHTML += '<u><mark>' + spa_treatment.end_date + '</mark></u>'
                            } else {
                                innerHTML += '<u><mark>настоящее время</mark></u>'
                            }
                            innerHTML += '<br>\
                            <strong>Диагноз, вид вмешательства: </strong><u><mark>' + spa_treatment.diagnosis + '</mark></u> <br>\
                            <strong>Специализация учреждения: </strong><u><mark>' + spa_treatment.founding_specialization + '</mark></u><br>\
                            <strong>Климатическая зона учреждения: </strong><u><mark>' + spa_treatment.climatic_zone + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#spaTreatmentModal" name="update-spa-treatment-' + spa_treatment.start_date + '-btn" onclick="update_spa_treatment(\'' + spa_treatment.start_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-spa-treatment-' + spa_treatment.start_date + '-btn" onclick="delete_spa_treatment(\'' + spa_treatment.start_date + '\')">Удалить</button>\
                        </div>';
                        let spa_treatment_div = document.getElementsByName('div-spa-treatment-' + spa_treatment.old_start_date)[0]
                        spa_treatment_div.innerHTML = innerHTML;
                        spa_treatment_div.setAttribute('name', 'div-spa-treatment-' + spa_treatment.start_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})

/* MEDICAL CERTIFICATES */
function medical_certificate_add_set_info(){
    medical_certificate_modal_header.innerHTML = 'Добавление медицинской справки';
    medical_certificate_disease_modal_inpt.value = "ОРВИ";
    medical_certificate_start_date_modal_dtpkr.value = "2023-01-01";
    medical_certificate_end_date_modal_dtpkr.value = "2023-01-12";
    medical_certificate_sport_exemption_date_modal_dpkr.value = null;
    medical_certificate_vac_exemption_date_modal_dpkr.value = null;
    medical_certificate_doctor_modal_inpt.value = "Иванов Иван Иванович";
    medical_certificate_cert_date_modal_dtpkr.value = "2023-01-13"
    medical_certificate_commit_modal_btn.value = "add";
}

function update_medical_certificate(disease, cert_date){
    var medical_certificate = {
        "medcard_num": medcard_num,
        "disease": disease,
        "cert_date": cert_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/medical_certificate/get",
        data: JSON.stringify({"json_data": medical_certificate}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            medical_certificate_modal_header.innerHTML = 'Редактирование медицинской справки';
            medical_certificate_disease_modal_inpt.value = data.medical_certificate.disease;
            medical_certificate_start_date_modal_dtpkr.value = data.medical_certificate.start_date;
            medical_certificate_end_date_modal_dtpkr.value = data.medical_certificate.end_date;
            medical_certificate_sport_exemption_date_modal_dpkr.value = data.medical_certificate.sport_exemption_date;
            medical_certificate_vac_exemption_date_modal_dpkr.value = data.medical_certificate.vac_exemption_date;
            medical_certificate_doctor_modal_inpt.value = data.medical_certificate.doctor;
            medical_certificate_cert_date_modal_dtpkr.value = data.medical_certificate.cert_date;
            if (data.medical_certificate.infection_contact){
                medical_certificate_infection_contact_modal_chk.checked = true
            } else {
                medical_certificate_infection_contact_modal_chk.checked = false
            }
            medical_certificate_close_modal_btn.value = data.medical_certificate.disease + '///' + data.medical_certificate.cert_date;
            medical_certificate_commit_modal_btn.value = "update";
        }
    });
}

medical_certificate_commit_modal_btn.addEventListener('click', () => {
    var medical_certificate = {
        "medcard_num": medcard_num,
        "disease": medical_certificate_disease_modal_inpt.value,
        "cert_date": medical_certificate_cert_date_modal_dtpkr.value,
        "start_date": medical_certificate_start_date_modal_dtpkr.value,
        "end_date": medical_certificate_end_date_modal_dtpkr.value,
        "sport_exemption_date": medical_certificate_sport_exemption_date_modal_dpkr.value,
        "vac_exemption_date": medical_certificate_vac_exemption_date_modal_dpkr.value,
        "doctor": medical_certificate_doctor_modal_inpt.value
    };

    if (medical_certificate_infection_contact_modal_chk.checked){
        medical_certificate["infection_contact"] = true;
    } else {
        medical_certificate["infection_contact"] = false;
    }
    switch (medical_certificate_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/medical_certificate/add",
                data: JSON.stringify({"json_data": medical_certificate}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    let medical_certificates_div = document.querySelector('#medical-certificates-main-div')
                    let innerHTML = '<div name="div-medical-certificate-' + medical_certificate.disease.replace(/ /g,'') + '-' + medical_certificate.cert_date + '" class="col-12 mb-3">\
                    <p>С <u><mark>' + medical_certificate.start_date + '</mark></u> по <u><mark>' + medical_certificate.end_date + '</mark></u> перенес: <strong>' + medical_certificate.disease  + '</strong> </br>\
                    В контакте с инфекционными больными <u><mark>';
                    if (!medical_certificate.infection_contact){
                        innerHTML += 'не';
                    };
                    innerHTML += 'был </mark></u></br>'
                    if (medical_certificate.sport_exemption_date){
                        innerHTML += 'Освобождение от занятий по физкультуре до: <u><mark>' + medical_certificate.sport_exemption_date + '</mark></u> </br>';
                    };
                    if (medical_certificate.vac_exemption_date){
                         innerHTML += 'Освобождение от профилактических прививок до: <u><mark>' + medical_certificate.vac_exemption_date + '</mark></u> </br>';
                    };
                        innerHTML += 'Справка от <u><mark>' + medical_certificate.cert_date + '</mark></u>, врач: <u><mark>' + medical_certificate.doctor + '</mark></u></p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#medicalCertificateModal" name="update-medical-certificate-' + medical_certificate.disease.replace(/ /g, '') + '-' + medical_certificate.cert_date + '-btn" onclick="update_medical_certificate(\'' + medical_certificate.disease + '\', \'' + medical_certificate.cert_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-medical-certificate-' + medical_certificate.disease.replace(/ /g, '') + '-' + medical_certificate.cert_date + '-btn" onclick="delete_medical_certificate(\'' + medical_certificate.disease + '\', \'' + medical_certificate.cert_date + '\')">Удалить</button>\
                    </div>\
                    </div>';
                    
                    medical_certificates_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                old_data = medical_certificate_close_modal_btn.value.split('///')
                medical_certificate["old_disease"] = old_data[0];
                medical_certificate["old_cert_date"] = old_data[1];
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/medical_certificate/update",
                    data: JSON.stringify({"json_data": medical_certificate}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let medical_certificates_div = document.getElementsByName('div-medical-certificate-' + medical_certificate.old_disease.replace(/ /g,'') + '-' + medical_certificate.old_cert_date)[0]
                        let innerHTML = '<p>С <u><mark>' + medical_certificate.start_date + '</mark></u> по <u><mark>' + medical_certificate.end_date + '</mark></u> перенес: <strong>' + medical_certificate.disease  + '</strong> </br>\
                        В контакте с инфекционными больными <u><mark>';
                        if (!medical_certificate.infection_contact){
                            innerHTML += 'не';
                        };
                        innerHTML += 'был </mark></u></br>'
                        if (medical_certificate.sport_exemption_date){
                            innerHTML += 'Освобождение от занятий по физкультуре до: <u><mark>' + medical_certificate.sport_exemption_date + '</mark></u> </br>';
                        };
                        if (medical_certificate.vac_exemption_date){
                             innerHTML += 'Освобождение от профилактических прививок до: <u><mark>' + medical_certificate.vac_exemption_date + '</mark></u> </br>';
                        };
                            innerHTML += 'Справка от <u><mark>' + medical_certificate.cert_date + '</mark></u>, врач: <u><mark>' + medical_certificate.doctor + '</mark></u></p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#medicalCertificateModal" name="update-medical-certificate-' + medical_certificate.disease.replace(/ /g, '') + '-' + medical_certificate.cert_date + '-btn" onclick="update_medical_certificate(\'' + medical_certificate.disease + '\', \'' + medical_certificate.cert_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-medical-certificate-' + medical_certificate.disease.replace(/ /g, '') + '-' + medical_certificate.cert_date + '-btn" onclick="delete_medical_certificate(\'' + medical_certificate.disease + '\', \'' + medical_certificate.cert_date + '\')">Удалить</button>\
                        </div>';
                        
                        medical_certificates_div.innerHTML = innerHTML;
                        medical_certificates_div.setAttribute('name', 'div-medical-certificate-' + medical_certificate.disease.replace(/ /g,'') + '-' + medical_certificate.cert_date)
                    }
                });
                break;
    
        default:
            break;
    }
})

function delete_medical_certificate(disease, cert_date){
    delete_modal_header.innerHTML = 'Удалить медицинскую справку';
    close_delete_modal_btn.value = disease + '///' + cert_date;
    delete_commit_modal_btn.value = 'delete_medical_certificate'
}


/* DISPENSARY */
function dispensary_add_set_info(){

    dispensary_modal_header.innerHTML = "Добавление сведений о санаторно-курортном лечении";
    dispensary_diagnosis_modal_inpt.value = "";
    dispensary_specialist_modal_inpt.value = "";
    dispensary_start_date_modal_dtpkr.value = "2023-01-01";
    dispensary_end_date_modal_dtpkr.value = "2023-01-01";
    dispensary_end_reason_modal_txt.value = "";
    dispensary_commit_modal_btn.value = 'add'; 
}

function update_dispensary(start_date){
    var dispensary = {
        "medcard_num": medcard_num,
        "start_date": start_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/dispensary/get",
        data: JSON.stringify({"json_data": dispensary}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            dispensary_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            dispensary_commit_modal_btn.value = 'update';
            dispensary_close_modal_btn.value = data.dispensary.start_date;
            dispensary_diagnosis_modal_inpt.value = data.dispensary.diagnosis;
            dispensary_specialist_modal_inpt.value = data.dispensary.specialist;
            dispensary_start_date_modal_dtpkr.value = data.dispensary.start_date;
            dispensary_end_date_modal_dtpkr.value = data.dispensary.end_date;
            dispensary_end_reason_modal_txt.value = data.dispensary.end_reason;
        }
    });    
}

function delete_dispensary(start_date){
    delete_modal_header.innerHTML = 'Удалить сведения о диспансерном наблюдении';
    close_delete_modal_btn.value = start_date;
    delete_commit_modal_btn.value = 'delete_dispensary'
}

dispensary_commit_modal_btn.addEventListener('click', () =>{
    var dispensary = {
        "medcard_num": medcard_num,
        "diagnosis": dispensary_diagnosis_modal_inpt.value,
        "start_date": dispensary_start_date_modal_dtpkr.value,
        "end_date": dispensary_end_date_modal_dtpkr.value,
        "specialist": dispensary_specialist_modal_inpt.value,
        "end_reason": dispensary_end_reason_modal_txt.value
    }
    switch (dispensary_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/dispensary/add",
                data: JSON.stringify({"json_data": dispensary}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-dispensary-' + dispensary.start_date + '" class="col-12 mb-3">\
                    <p><strong>' + dispensary.diagnosis + '</strong> с <u><mark>' + dispensary.start_date + '</mark></u> по'
                    if (dispensary.end_date){
                        innerHTML += '<u><mark>' + dispensary.end_date + '</mark></u>'
                        if (dispensary.end_reason){
                                innerHTML += '<br> Причина снятия: <u><mark>' + dispensary.end_reason + '</mark></u>'
                        }
                    } else {
                        innerHTML += '<u><mark>настоящее время</mark></u>'
                    }
                    innerHTML += '<br>Специалист: <u><mark>' + dispensary.specialist + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-info mt-2 btn-sm" data-bs-toggle="offcanvas" data-bs-target="#visitSpecialistControlOffcanvas" aria-controls="visitSpecialistControlOffcanvas" onclick="get_visit_specialist_control(\'' + dispensary.start_date + '\')">Контроль посещений специалиста</button>\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#dispensaryModal" name="update-dispensary-' + dispensary.start_date + '-btn" onclick="update_dispensary(\'' + dispensary.start_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-dispensary-' + dispensary.start_date + '-btn" onclick="delete_dispensary(\'' + dispensary.start_date + '\')">Удалить</button>\
                    </div>\
                    </div>'
                    let dispensary_div = document.querySelector('#dispensary-main-div')
                    dispensary_div.innerHTML += innerHTML
                }
            });
            break;

            case 'update':
                dispensary["old_start_date"] = dispensary_close_modal_btn.value;
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/dispensary/update",
                    data: JSON.stringify({"json_data": dispensary}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p><strong>' + dispensary.diagnosis + '</strong> с <u><mark>' + dispensary.start_date + '</mark></u> по'
                        if (dispensary.end_date){
                            innerHTML += '<u><mark>' + dispensary.end_date + '</mark></u>'
                            if (dispensary.end_reason){
                                    innerHTML += '<br> Причина снятия: <u><mark>' + dispensary.end_reason + '</mark></u>'
                            }
                        } else {
                            innerHTML += '<u><mark>настоящее время</mark></u>'
                        }
                        innerHTML += '<br>Специалист: <u><mark>' + dispensary.specialist + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-info mt-2 btn-sm" data-bs-toggle="offcanvas" data-bs-target="#visitSpecialistControlOffcanvas" aria-controls="visitSpecialistControlOffcanvas" onclick="get_visit_specialist_control(\'' + dispensary.start_date + '\')">Контроль посещений специалиста</button>\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#dispensaryModal" name="update-dispensary-' + dispensary.start_date + '-btn" onclick="update_dispensary(\'' + dispensary.start_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-dispensary-' + dispensary.start_date + '-btn" onclick="delete_dispensary(\'' + dispensary.start_date + '\')">Удалить</button>\
                        </div>';
                        let dispensary_div = document.getElementsByName('div-dispensary-' + dispensary.old_start_date)[0]
                        dispensary_div.innerHTML = innerHTML;
                        dispensary_div.setAttribute('name', 'div-dispensary-' + dispensary.start_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* VISIT SPECIALIST CONTROL */
function get_visit_specialist_control(start_dispanser_date){
    var visit_specialist_control = {
        "medcard_num": medcard_num,
        "start_dispanser_date": start_dispanser_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/visit_specialist_control/get_all",
        data: JSON.stringify({"json_data": visit_specialist_control}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            visit_specialist_control_add_btn.value = start_dispanser_date;
            let visit_specialist_control_div = document.querySelector('#visit-specialist-control-main-div')
            innerHTML = ""
            data.visit_specialist_control.forEach(element => {
                innerHTML += '<div name="div-visit-specialist-control-'+ element.assigned_date + '" class="col-12 mb-3">\
                <p>Назначено: <u><mark>' + element.assigned_date + '</u></mark> Явка: <u><mark>'
                if (element.fact_date) {
                    innerHTML += element.fact_date
                }  else {
                    innerHTML += 'еще не явился'
                } 
                innerHTML += '</u></mark> </p>\
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#visitSpecialistControlModal" name="update-visit-specialist-control-' + element.assigned_date + '-btn" onclick="update_visit_specialist_control(\'' + element.assigned_date + '\', \'' + element.fact_date +'\')">Редактировать</button>\
                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-visit-specialist-control-' + element.assigned_date + '-btn" onclick="delete_visit_specialist_control(\'' + element.assigned_date + '\')">Удалить</button>\
                </div>\
                </div>'
            });
            visit_specialist_control_div.innerHTML = innerHTML;
        }
    });
}

function visit_specialist_controls_add_set_info(){
    visit_specialist_control_modal_header.innerHTML = 'Добавить сведения о посещении специалиста';
    visit_specialist_control_commit_modal_btn.value = 'add';
}

function update_visit_specialist_control(assigned_date, fact_date){
    visit_specialist_control_modal_header.innerHTML = 'Редактировать сведения о посещении специалиста';
    visit_specialist_control_close_modal_btn.value = assigned_date
    visit_specialist_control_commit_modal_btn.value = 'update';
    visit_specialist_control_assigned_date_modal_dtpkr.value = assigned_date;
    visit_specialist_control_fact_date_modal_dtpkr.value = fact_date;
}


function delete_visit_specialist_control(assigned_date){
    delete_modal_header.innerHTML = 'Удалить сведения о контроле посещении специалиста';
    close_delete_modal_btn.value = assigned_date;
    delete_commit_modal_btn.value = 'delete_visit_specialist_control'
}

visit_specialist_control_commit_modal_btn.addEventListener('click', () => {
    var visit_specialist_control = {
        "medcard_num": medcard_num,
        "start_dispanser_date": visit_specialist_control_add_btn.value,
        "assigned_date": visit_specialist_control_assigned_date_modal_dtpkr.value,
        "fact_date": visit_specialist_control_fact_date_modal_dtpkr.value
    }
    switch (visit_specialist_control_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/visit_specialist_control/add",
                data: JSON.stringify({"json_data": visit_specialist_control}),
                contentType: "application/json",
                dataType: 'json',
                success: () =>{
                    let visit_specialist_control_div = document.querySelector('#visit-specialist-control-main-div');
                    visit_specialist_control_div.innerHTML += '<div name="div-visit-specialist-control-'+ visit_specialist_control.assigned_date + '" class="col-12 mb-3">\
                    <p>Назначено: <u><mark>' + visit_specialist_control.assigned_date + '</u></mark> Явка: ' + visit_specialist_control.fact_date + '</u></mark> </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                    <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#visitSpecialistControlModal" name="update-visit-specialist-control-' + visit_specialist_control.assigned_date + '-btn" onclick="update_visit_specialist_control(\'' + visit_specialist_control.start_dispanser_date + '///' + visit_specialist_control.assigned_date + '///' + visit_specialist_control.fact_date +'\')">Редактировать</button>\
                    <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-visit-specialist-control-' + visit_specialist_control.assigned_date + '-btn" onclick="delete_visit_specialist_control(\'' + visit_specialist_control.start_dispanser_date + '///' + visit_specialist_control.assigned_date + '\')">Удалить</button>\
                    </div>\
                    </div>'
                }
            });
            break;

            case 'update':
                visit_specialist_control["old_assigned_date"] = visit_specialist_control_close_modal_btn.value 
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/visit_specialist_control/update",
                    data: JSON.stringify({"json_data": visit_specialist_control}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () =>{
                        let visit_specialist_control_div = document.getElementsByTagName('div-visit-specialist-control-'+ visit_specialist_control.old_assigned_date)[0];
                        visit_specialist_control_div.innerHTML = '<p>Назначено: <u><mark>' + visit_specialist_control.assigned_date + '</u></mark> Явка: ' + visit_specialist_control.fact_date + '</u></mark> </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#visitSpecialistControlModal" name="update-visit-specialist-control-' + visit_specialist_control.assigned_date + '-btn" onclick="update_visit_specialist_control(\'' + visit_specialist_control.start_dispanser_date + '///' + visit_specialist_control.assigned_date + '///' + visit_specialist_control.fact_date +'\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-visit-specialist-control-' + visit_specialist_control.assigned_date + '-btn" onclick="delete_visit_specialist_control(\'' + visit_specialist_control.start_dispanser_date + '///' + visit_specialist_control.assigned_date + '\')">Удалить</button>\
                        </div>'
                        visit_specialist_control_div.setAttribute('name', 'div-visit-specialist-control-'+ visit_specialist_control.assigned_date)
                    }
                });
                break;
    
        default:
            break;
    }
})


/* DEWORMING */
function deworming_add_set_info(){

    deworming_modal_header.innerHTML = "";
    deworming_date_modal_dtpkr.value = "2023-03-01";
    deworming_result_modal_txt.value = "";
    deworming_commit_modal_btn.value = 'add'; 
}

function update_deworming(deworming_date){
    var deworming = {
        "medcard_num": medcard_num,
        "deworming_date": deworming_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/deworming/get",
        data: JSON.stringify({"json_data": deworming}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            deworming_modal_header.innerHTML = "Редактирование сведений о дегельминтизации";
            deworming_commit_modal_btn.value = 'update';
            deworming_close_modal_btn.value = data.deworming.deworming_date;
            deworming_date_modal_dtpkr.value = data.deworming.deworming_date;
            deworming_result_modal_txt.value = data.deworming.result;
        }
    });    
}

function delete_deworming(deworming_date){
    delete_modal_header.innerHTML = 'Удалить сведения о дегельминтизации';
    close_delete_modal_btn.value = deworming_date;
    delete_commit_modal_btn.value = 'delete_deworming'
}

deworming_commit_modal_btn.addEventListener('click', () =>{
    var deworming = {
        "medcard_num": medcard_num,
        "deworming_date": deworming_date_modal_dtpkr.value,
        "result": deworming_result_modal_txt.value
    };
    switch (deworming_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/deworming/add",
                data: JSON.stringify({"json_data": deworming}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-deworming-' + deworming.deworming_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + deworming.deworming_date + '</mark></u> \
                        Результат: <u><mark>' + deworming.result + '</mark></u> \
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#dewormingModal" name="update-deworming-' + deworming.deworming_date + '-btn" onclick="update_deworming(\'' + deworming.deworming_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-deworming-' + deworming.deworming_date + '-btn" onclick="delete_deworming(\'' + deworming.deworming_date + '\')">Удалить</button>\
                    </div>\
                    </div>'
                    let deworming_div = document.querySelector('#deworming-main-div')
                    deworming_div.innerHTML += innerHTML
                }
            });
            break;

            case 'update':
                deworming["old_deworming_date"] = deworming_close_modal_btn.value;
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/deworming/update",
                    data: JSON.stringify({"json_data": deworming}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + deworming.deworming_date + '</mark></u> \
                        Результат: <u><mark>' + deworming.result + '</mark></u> \
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#dewormingModal" name="update-deworming-' + deworming.deworming_date + '-btn" onclick="update_deworming(\'' + deworming.deworming_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-deworming-' + deworming.deworming_date + '-btn" onclick="delete_deworming(\'' + deworming.deworming_date + '\')">Удалить</button>\
                        </div>';
                        let deworming_div = document.getElementsByName('div-deworming-' + deworming.old_deworming_date)[0]
                        deworming_div.innerHTML = innerHTML;
                        deworming_div.setAttribute('name', 'div-deworming-' + deworming.deworming_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* ORAL SANATION */
function oral_sanation_add_set_info(){

    oral_sanation_modal_header.innerHTML = "Добавление сведений о санации полости рта";
    oral_sanation_date_modal_dtpkr.value = "2023-03-01";
    oral_sanation_dental_result_modal_txt.value = "28 гнилых зубов";
    oral_sanation_result_modal_txt.value = "Вылечены все";
    oral_sanation_commit_modal_btn.value = 'add'; 
}

function update_oral_sanation(sanation_date){
    var oral_sanation = {
        "medcard_num": medcard_num,
        "sanation_date": sanation_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/medical_record/child/" + medcard_num + "/oral_sanation/get",
        data: JSON.stringify({"json_data": oral_sanation}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            oral_sanation_modal_header.innerHTML = "Редактирование сведений о санации полости рта";
            oral_sanation_commit_modal_btn.value = 'update';
            oral_sanation_close_modal_btn.value = data.oral_sanation.sanation_date;
            oral_sanation_date_modal_dtpkr.value = data.oral_sanation.sanation_date;
            oral_sanation_dental_result_modal_txt.value = data.oral_sanation.dental_result;
            oral_sanation_result_modal_txt.value = data.oral_sanation.sanation_result;
        }
    });    
}

function delete_oral_sanation(sanation_date){
    delete_modal_header.innerHTML = 'Удалить сведения о санации полости рта';
    close_delete_modal_btn.value = sanation_date;
    delete_commit_modal_btn.value = 'delete_oral_sanation';
}

oral_sanation_commit_modal_btn.addEventListener('click', () =>{
    var oral_sanation = {
        "medcard_num": medcard_num,
        "sanation_date": oral_sanation_date_modal_dtpkr.value,
        "dental_result": oral_sanation_dental_result_modal_txt.value,
        "sanation_result": oral_sanation_result_modal_txt.value
    };
    switch (oral_sanation_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/oral_sanation/add",
                data: JSON.stringify({"json_data": oral_sanation}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-oral-sanation-' + oral_sanation.sanation_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + oral_sanation.sanation_date + '</mark></u> <br>\
                        Данные осмотра стоматологом: <u><mark>' + oral_sanation.dental_result + '</mark></u> <br>\
                        Результаты санации: <u><mark>' + oral_sanation.sanation_result + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#oralSanationModal" name="update-oral-sanation-' + oral_sanation.sanation_date + '-btn" onclick="update_oral_sanation(\'' + oral_sanation.sanation_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-oral-sanation-' + oral_sanation.sanation_date + '-btn" onclick="delete_oral_sanation(\'' + oral_sanation.sanation_date + '\')">Удалить</button>\
                    </div>\
                </div>'
                    let oral_sanation_div = document.querySelector('#oral-sanation-main-div')
                    oral_sanation_div.innerHTML += innerHTML
                }
            });
            break;

            case 'update':
                oral_sanation["old_sanation_date"] = oral_sanation_close_modal_btn.value;
                $.ajax({
                    type: "POST",
                    async: true,
                    url: "/medical_record/child/" + medcard_num + "/oral_sanation/update",
                    data: JSON.stringify({"json_data": oral_sanation}),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + oral_sanation.sanation_date + '</mark></u> <br>\
                        Данные осмотра стоматологом: <u><mark>' + oral_sanation.dental_result + '</mark></u> <br>\
                        Результаты санации: <u><mark>' + oral_sanation.sanation_result + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#oralSanationModal" name="update-oral-sanation-' + oral_sanation.sanation_date + '-btn" onclick="update_oral_sanation(\'' + oral_sanation.sanation_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-oral-sanation-' + oral_sanation.sanation_date + '-btn" onclick="delete_oral_sanation(\'' + oral_sanation.sanation_date + '\')">Удалить</button>\
                        </div>';
                        let oral_sanation_div = document.getElementsByName('div-oral-sanation-' + oral_sanation.old_sanation_date)[0]
                        oral_sanation_div.innerHTML = innerHTML;
                        oral_sanation_div.setAttribute('name', 'div-oral-sanation-' + oral_sanation.sanation_date) 
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

        case 'delete_past_illness':
            past_illness_data = close_delete_modal_btn.value.split('///')
            past_illness = {
                "medcard_num": medcard_num,
                "diagnosis": past_illness_data[0],
                "start_date": past_illness_data[1]
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/past_illness/delete",
                data: JSON.stringify({"json_data": past_illness}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var past_illness_div = document.getElementsByName('div-past-illness-' + past_illness.diagnosis.replace(/ /g,'') + '-' + past_illness.start_date)[0];
                    past_illness_div.remove();
                }
            });
            
            break;
        
        case 'delete_hospitalization':
            hospitalization = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/hospitalization/delete",
                data: JSON.stringify({"json_data": hospitalization}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var hospitalization_div = document.getElementsByName('div-hospitalization-' + hospitalization.start_date)[0];
                    hospitalization_div.remove();
                }
            });
            
            break;

        case 'delete_spa_treatment':
            spa_treatment = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/spa_treatment/delete",
                data: JSON.stringify({"json_data": spa_treatment}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var spa_treatment_div = document.getElementsByName('div-spa-treatment-' + spa_treatment.start_date)[0];
                    spa_treatment_div.remove();
                }
            });
            
            break;        

        case 'delete_medical_certificate':
            medical_certificate_data = close_delete_modal_btn.value.split('///')
            medical_certificate = {
                "medcard_num": medcard_num,
                "disease": medical_certificate_data[0],
                "cert_date": medical_certificate_data[1]
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/medical_certificate/delete",
                data: JSON.stringify({"json_data": medical_certificate}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var medical_certificate_div = document.getElementsByName('div-medical-certificate-' + medical_certificate.disease.replace(/ /g,'') + '-' + medical_certificate.cert_date)[0];
                    medical_certificate_div.remove();
                }
            });
            
            break;

        case 'delete_dispensary':
            dispensary = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/dispensary/delete",
                data: JSON.stringify({"json_data": dispensary}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var dispensary_div = document.getElementsByName('div-dispensary-' + dispensary.start_date)[0];
                    dispensary_div.remove();
                }
            });
            
            break; 
        
        case 'delete_visit_specialist_control':
            visit_specialist_control = {
                "medcard_num": medcard_num,
                "start_dispanser_date": visit_specialist_control_add_btn.value,
                "assigned_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/visit_specialist_control/delete",
                data: JSON.stringify({"json_data": visit_specialist_control}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var visit_specialist_control_div = document.getElementsByName('div-visit-specialist-control-'+ visit_specialist_control.assigned_date)[0];
                    visit_specialist_control_div.remove();
                }
            });
            
            break;     
         
        case 'delete_deworming':
            deworming = {
                "medcard_num": medcard_num,
                "deworming_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/deworming/delete",
                data: JSON.stringify({"json_data": deworming}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var deworming_div = document.getElementsByName('div-deworming-' + deworming.deworming_date)[0];
                    deworming_div.remove();
                }
            });
            
            break;     
        
        case 'delete_oral_sanation':
            oral_sanation = {
                "medcard_num": medcard_num,
                "sanation_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "POST",
                async: true,
                url: "/medical_record/child/" + medcard_num + "/oral_sanation/delete",
                data: JSON.stringify({"json_data": oral_sanation}),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var oral_sanation_div = document.getElementsByName('div-oral-sanation-' + oral_sanation.sanation_date)[0];
                    oral_sanation_div.remove();
                }
            });
            
            break;
            
            
        default:
            break;
    }

})
