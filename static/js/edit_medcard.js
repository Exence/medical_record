const medcard_num = document.querySelector('#general-button').value;
const commit_allergy_modal_btn = document.querySelector('#allergy_modal_commit');
const close_allergy_modal_btn = document.querySelector('#allergy_close_modal');
const allergy_modal_header = document.querySelector('#allergyModalLabel');
const allergen = document.querySelector('#allergen-modal');
const allergy_type = document.querySelector('#allergyType-modal');
const start_age = document.querySelector('#allergyStartAge-modal');
const reaction_type = document.querySelector('#allergyReactionType-modal');
const diagnosis_date = document.querySelector('#allergyDiagnosisDate-modal');
const note = document.querySelector('#allergyNote-modal');

const delete_modal_header = document.querySelector('#deleteModalLabel');
const commit_delete_modal_btn = document.querySelector('#delete_modal_commit')
const close_delete_modal_btn = document.querySelector('#delete_close_modal')


commit_allergy_modal_btn.addEventListener('click', () => {
     var allergy = {
            "allergen": allergen.value,
            "allergy_type": allergy_type.value,
            "start_age": start_age.value,
            "reaction_type": reaction_type.value,
            "diagnosis_date": diagnosis_date.value,
            "note": note.value
        };
    if (commit_allergy_modal_btn.value === 'add'){
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
    } else {
        const allergen_name = close_allergy_modal_btn.value;
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
    }
    
})

function add_allergy(){
    allergy_modal_header.innerHTML = 'Добавление данных об аллергии';
    commit_allergy_modal_btn.value = 'add';
    allergen.value = "";
    start_age.value = "";
    reaction_type.value = "";
    diagnosis_date.value = "";
    note.value = "";
}

function update_allergy(allergen_name){
    allergy_modal_header.innerHTML = 'Редактирование данных об аллергии';
    commit_allergy_modal_btn.value = 'update';
    close_allergy_modal_btn.value = allergen_name;
    const btn_caller = document.querySelector('#btn-update-' + allergen_name.replace(/ /g,''))
    allergy_data = btn_caller.value.split('///')
    allergen.value = allergy_data[0];
    allergy_type.value = allergy_data[1];
    start_age.value = allergy_data[2];
    reaction_type.value = allergy_data[3];
    diagnosis_date.value = allergy_data[4];
    note.value = allergy_data[5];}

function delete_allergy(allergen_name){
    delete_modal_header.innerHTML = 'Удалить сведения об аллергии';
    close_delete_modal_btn.value = allergen_name;
    commit_delete_modal_btn.value = 'delete_allergy'
}





commit_delete_modal_btn.addEventListener('click', () => {    
    switch (commit_delete_modal_btn.value) {
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
    
        default:
            break;
    }

})
