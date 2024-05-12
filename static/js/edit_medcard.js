const medcard_num = document.querySelector('#update-child-btn').value;
/* CHILD CONST*/
const child_surname_modal_inpt = document.querySelector('#surname');
const child_name_modal_inpt = document.querySelector('#name');
const child_patronymic_modal_inpt = document.querySelector('#patronymic');
const child_kindergarten_name_modal_slct = document.querySelector('#kindergarten_name');
const child_birthday_modal_inpt = document.querySelector('#birthday');
const child_modal_rd = document.getElementsByName('sex')[0];
const child_male_modal_rd = document.querySelector('#flexRadioSex1');
const child_female_modal_rd = document.querySelector('#flexRadioSex2');
const child_group_num_modal_slct = document.querySelector('#group_num');
const child_address_modal_inpt = document.querySelector('#address');
const child_clinic_modal_slct = document.querySelector('#clinic');
const child_entering_date_modal_dtpk = document.querySelector('#entering_date');
const child_family_characteristics_modal_slct = document.querySelector('#family_characteristics');
const child_family_microclimate_modal_slct = document.querySelector('#family_microclimate');
const child_rest_and_class_opportunities_modal_slct = document.querySelector('#rest_and_class_opportunities');
const child_case_history_modal_txt = document.querySelector('#case_history');
const child_close_modal_btn = document.querySelector('#child-close-modal');
const child_commit_modal_btn = document.querySelector('#child-commit-modal');


/*********************************************************************************************/
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
const oral_sanation_dental_result_modal_txt = document.querySelector('#oralSanationDentalResult-modal');
const oral_sanation_result_modal_txt = document.querySelector('#oralSanationResult-modal');
const oral_sanation_close_modal_btn = document.querySelector('#oral-sanation-close-modal');
const oral_sanation_commit_modal_btn = document.querySelector('#oral-sanation-commit-modal');

/*********************************************************************************************/
/* PREVACCINATION CHECKUP CONST */
const prevaccination_checkup_modal_header = document.querySelector('#prevaccinationCheckupModalLabel');
const prevaccination_checkup_examination_date_modal_dtpkr = document.querySelector('#prevaccinationCheckupExaminationDate-modal');
const prevaccination_checkup_diagnosis_modal_inpt = document.querySelector('#prevaccinationCheckupDiagnosis-modal');
const prevaccination_checkup_report_modal_slct = document.querySelector('#prevaccinationCheckupReport-modal');
const prevaccination_checkup_vac_name_modal_slct = document.querySelector('#prevaccinationCheckupVacName-modal');
const prevaccination_checkup_no_vac_date_modal_dtpkr = document.querySelector('#prevaccinationCheckupNoVacDate-modal');
const prevaccination_checkup_doctor_modal_inpt = document.querySelector('#prevaccinationCheckupDoctor-modal');
const prevaccination_checkup_close_modal_btn = document.querySelector('#prevaccination-checkup-close-modal');
const prevaccination_checkup_commit_modal_btn = document.querySelector('#prevaccination-checkup-commit-modal');

/* PROF VACCINATIONS CONST */
const prof_vaccination_modal_header = document.querySelector('#profVaccinationModalLabel');
const prof_vaccination_vac_name_modal_slct = document.querySelector('#profVaccinationVacName-modal');
const prof_vaccination_vac_type_modal_slct = document.querySelector('#profVaccinationVacType-modal');
const prof_vaccination_date_modal_dtpk = document.querySelector('#profVaccinationDate-modal');
const prof_vaccination_serial_modal_inpt = document.querySelector('#profVaccinationSerial-modal');
const prof_vaccination_dose_modal_inpt = document.querySelector('#profVaccinationDose-modal');
const prof_vaccination_introduction_method_modal_slct = document.querySelector('#profVaccinationIntroductionMethod-modal');
const prof_vaccination_reaction_modal_slct = document.querySelector('#profVaccinationReaction-modal');
const prof_vaccination_doctor_modal_inpt = document.querySelector('#profVaccinationDoctor-modal');
const prof_vaccination_close_modal_btn = document.querySelector('#prof-vaccination-close-modal');
const prof_vaccination_commit_modal_btn = document.querySelector('#prof-vaccination-commit-modal');

/* EPID VACCINATIONS CONST */
const epid_vaccination_modal_header = document.querySelector('#epidVaccinationModalLabel');
const epid_vaccination_vac_name_modal_slct = document.querySelector('#epidVaccinationVacName-modal');
const epid_vaccination_vac_type_modal_slct = document.querySelector('#epidVaccinationVacType-modal');
const epid_vaccination_date_modal_dtpk = document.querySelector('#epidVaccinationDate-modal');
const epid_vaccination_serial_modal_inpt = document.querySelector('#epidVaccinationSerial-modal');
const epid_vaccination_dose_modal_inpt = document.querySelector('#epidVaccinationDose-modal');
const epid_vaccination_introduction_method_modal_slct = document.querySelector('#epidVaccinationIntroductionMethod-modal');
const epid_vaccination_reaction_modal_slct = document.querySelector('#epidVaccinationReaction-modal');
const epid_vaccination_doctor_modal_inpt = document.querySelector('#epidVaccinationDoctor-modal');
const epid_vaccination_close_modal_btn = document.querySelector('#epid-vaccination-close-modal');
const epid_vaccination_commit_modal_btn = document.querySelector('#epid-vaccination-commit-modal');


/* GG INJECTIONS CONST */
const gg_injection_modal_header = document.querySelector('#ggInjectionModalLabel');
const gg_injection_date_modal_dtpk = document.querySelector('#ggInjectionDate-modal');
const gg_injection_reason_modal_txt = document.querySelector('#ggInjectionReason-modal');
const gg_injection_serial_modal_inpt = document.querySelector('#ggInjectionSerial-modal');
const gg_injection_dose_modal_inpt = document.querySelector('#ggInjectionDose-modal');
const gg_injection_reaction_modal_slct = document.querySelector('#ggInjectionReaction-modal');
const gg_injection_doctor_modal_inpt = document.querySelector('#ggInjectionDoctor-modal');
const gg_injection_close_modal_btn = document.querySelector('#gg-injection-close-modal');
const gg_injection_commit_modal_btn = document.querySelector('#gg-injection-commit-modal');

/* MANTOUX TEST CONST */
const mantoux_test_modal_header = document.querySelector('#mantouxTestModalLabel');
const mantoux_test_date_modal_dtpk = document.querySelector('#mantouxTestDate-modal');
const mantoux_test_result_modal_slct = document.querySelector('#mantouxTestResult-modal');
const mantoux_test_close_modal_btn = document.querySelector('#mantoux-test-close-modal');
const mantoux_test_commit_modal_btn = document.querySelector('#mantoux-test-commit-modal');

/* TUB VAC CONST */
const tub_vac_modal_header = document.querySelector('#tubVacModalLabel');
const tub_vac_date_modal_dtpk = document.querySelector('#tubVacDate-modal');
const tub_vac_serial_modal_inpt = document.querySelector('#tubVacSerial-modal');
const tub_vac_dose_modal_inpt = document.querySelector('#tubVacDose-modal');
const tub_vac_doctor_modal_inpt = document.querySelector('#tubVacDoctor-modal');
const tub_vac_close_modal_btn = document.querySelector('#tub-vac-close-modal');
const tub_vac_commit_modal_btn = document.querySelector('#tub-vac-commit-modal');

/*********************************************************************************************/
/* MEDICAL EXAMINATION CONST*/
const medical_examination_modal_header = document.querySelector('#medicalExaminationModalLabel');
const medical_examination_period_modal_slct = document.querySelector('#medicalExaminationPeriod-modal');
const medical_examination_date_modal_dtpk = document.querySelector('#medicalExaminationDate-modal');
const medical_examination_height_modal_inpt = document.querySelector('#medicalExaminationHeight-modal');
const medical_examination_weight_modal_inpt = document.querySelector('#medicalExaminationWeight-modal');
const medical_examination_complaints_modal_txt = document.querySelector('#medicalExaminationComplaints-modal');
const medical_examination_pediatrician_modal_txt = document.querySelector('#medicalExaminationPediatrician-modal');
const medical_examination_orthopaedist_modal_txt = document.querySelector('#medicalExaminationOrthopaedist-modal');
const medical_examination_ophthalmologist_modal_txt = document.querySelector('#medicalExaminationOphthalmologist-modal');
const medical_examination_otolaryngologist_modal_txt = document.querySelector('#medicalExaminationOtolaryngologist-modal');
const medical_examination_dermatologist_modal_txt = document.querySelector('#medicalExaminationDermatologist-modal');
const medical_examination_neurologist_modal_txt = document.querySelector('#medicalExaminationNeurologist-modal');
const medical_examination_speech_therapist_modal_txt = document.querySelector('#medicalExaminationSpeechTherapist-modal');
const medical_examination_denta_surgeon_modal_txt = document.querySelector('#medicalExaminationDentaSurgeon-modal');
const medical_examination_psychologist_modal_txt = document.querySelector('#medicalExaminationPsychologist-modal');
const medical_examination_other_doctors_modal_txt = document.querySelector('#medicalExaminationOtherDoctors-modal');
const medical_examination_blood_test_modal_txt = document.querySelector('#medicalExaminationBloodTest-modal');
const medical_examination_urine_analysis_modal_txt = document.querySelector('#medicalExaminationUrineAnalysis-modal');
const medical_examination_feces_analysis_modal_txt = document.querySelector('#medicalExaminationFecesAnalysis-modal');
const medical_examination_general_diagnosis_modal_txt = document.querySelector('#medicalExaminationGeneralDiagnosis-modal');
const medical_examination_physical_development_modal_txt = document.querySelector('#medicalExaminationPhysicalDevelopment-modal');
const medical_examination_mental_development_modal_txt = document.querySelector('#medicalExaminationMentalDevelopment-modal');
const medical_examination_health_group_modal_slct = document.querySelector('#medicalExaminationHealthGroup-modal');
const medical_examination_sport_group_modal_slct = document.querySelector('#medicalExaminationSportGroup-modal');
const medical_examination_med_and_ped_conclusion_modal_txt = document.querySelector('#medicalExaminationMedAndPedConclusion-modal');
const medical_examination_recommendations_modal_txt = document.querySelector('#medicalExaminationRecommendations-modal');
const medical_examination_close_modal_btn = document.querySelector('#medical-examination-close-modal');
const medical_examination_commit_modal_btn = document.querySelector('#medical-examination-commit-modal');

/*********************************************************************************************/
/* ONGOING MEDICAL SUPERVISION CONST*/
const oms_modal_header = document.querySelector('#omsModalLabel');
const oms_examination_date_modal_dtpk = document.querySelector('#omsExaminationDate-modal');
const oms_examination_data_modal_txt = document.querySelector('#omsExaminationData-modal');
const oms_diagnosis_modal_txt = document.querySelector('#omsDiagnosis-modal');
const oms_prescription_modal_txt = document.querySelector('#omsPrescription-modal');
const oms_doctor_modal_inpt = document.querySelector('#omsDoctor-modal');
const oms_close_modal_btn = document.querySelector('#oms-close-modal');
const oms_commit_modal_btn = document.querySelector('#oms-commit-modal');

/*********************************************************************************************/
/* SCREENING CONST*/
const screening_modal_header = document.querySelector('#screeningModalLabel');
const screening_examination_date_modal_dtpk = document.querySelector('#screeningExaminationDate-modal');
const screening_questionnaire_test_modal_slct = document.querySelector('#screeningQuestionnaireTest-modal');
const screening_height_modal_inpt = document.querySelector('#screeningHeight-modal');
const screening_weight_modal_inpt = document.querySelector('#screeningWeight-modal');
const screening_physical_development_modal_slct = document.querySelector('#screeningPhysicalDevelopment-modal');
const screening_blood_pressures_modal_inpt = document.querySelector('#screeningBloodPressures-modal');
const screening_carriage_modal_slct = document.querySelector('#screeningCarriage-modal');
const screening_foot_condition_modal_slct = document.querySelector('#screeningFooCondition-modal');
const screening_sight_od_modal_inpt = document.querySelector('#screeningSightOd-modal');
const screening_sight_os_modal_inpt = document.querySelector('#screeningSightOs-modal');
const screening_visual_acuity_modal_slct = document.querySelector('#screeningVisualAcuity-modal');
const screening_malinovsky_test_modal_slct = document.querySelector('#screeningMalinovskyTest-modal');
const screening_binocular_vision_modal_slct = document.querySelector('#screeningBinocularVision-modal');
const screening_hearing_acuteness_modal_slct = document.querySelector('#screeningHearingAcuteness-modal');
const screening_dynammetry_left_modal_inpt = document.querySelector('#screeningDynammetryRight-modal');
const screening_dynammetry_right_modal_inpt = document.querySelector('#screeningDynammetryLeft-modal');
const screening_physical_fitness_modal_slct = document.querySelector('#screeningPhysicalFitness-modal');
const screening_protein_in_urine_modal_slct = document.querySelector('#screeningProteinInUrine-modal');
const screening_glucose_in_urine_modal_slct = document.querySelector('#screeningGlucoseInUrine-modal');
const screening_biological_age_modal_slct = document.querySelector('#screeningBiologicalAge-modal');
const screening_speech_defects_modal_chck = document.querySelector('#screeningSpeechDefects-modal');
const screening_kern_test_modal_inpt = document.querySelector('#screeningKernTest-modal');
const screening_neurotic_disorders_modal_chck = document.querySelector('#screeningNeuroticDisorders-modal');
const screening_thinking_and_speech_disorders_modal_chck = document.querySelector('#screeningThinkingAndSpeechDisorders-modal');
const screening_motor_development_disorders_modal_chck = document.querySelector('#screeningMotorDevelopmentDisorders-modal');
const screening_attention_and_memory_disorders_modal_chck = document.querySelector('#screeningAttentionAndMemoryDisorders-modal');
const screening_social_contacts_disorders_modal_chck = document.querySelector('#screeningSocialContactsDisorders-modal');
const screening_close_modal_btn = document.querySelector('#screening-close-modal');
const screening_commit_modal_btn = document.querySelector('#screening-commit-modal');

/*********************************************************************************************/
/* DELETE WINDOW CONST*/
const delete_modal_header = document.querySelector('#deleteModalLabel');
const delete_commit_modal_btn = document.querySelector('#delete_modal_commit');
const close_delete_modal_btn = document.querySelector('#delete_close_modal');


/* CHILD */
function update_child(){
    $.ajax({
        type: "GET",
        async: true,
        url: "/api/v1/children/" + medcard_num,
        success: function(child){
            child_surname_modal_inpt.value = child.surname;
            child_name_modal_inpt.value = child.name;
            child_patronymic_modal_inpt.value = child.patronymic;
            child_kindergarten_name_modal_slct.value = child_kindergarten_name_modal_slct.querySelector(`option[number="${child.kindergarten_num}"]`).value;
            child_birthday_modal_inpt.value = child.birthday;
            if (child.sex === 'М'){
                child_male_modal_rd.checked = true;
            } else {
                child_female_modal_rd.checked = true;
            }
            child_group_num_modal_slct.value = child.group_num;
            child_address_modal_inpt.value = child.address;
            child_clinic_modal_slct.value = child.clinic.id;
            child_entering_date_modal_dtpk.value = child.entering_date;
            child_family_characteristics_modal_slct.value = child.family_characteristics.trim();
            child_family_microclimate_modal_slct.value = child.family_microclimate;
            child_rest_and_class_opportunities_modal_slct.value = child.rest_and_class_opportunities;
            child_case_history_modal_txt.value = child.case_history;
        }
    });  
}

child_commit_modal_btn.addEventListener('click', () => {
    var child = {
        "surname": child_surname_modal_inpt.value,
        "name": child_name_modal_inpt.value,
        "patronymic": child_patronymic_modal_inpt.value,
        "kindergarten_num": child_kindergarten_name_modal_slct[child_kindergarten_name_modal_slct.selectedIndex].getAttribute('number'),
        "birthday": child_birthday_modal_inpt.value,
        "sex": child_modal_rd.value[0],
        "group_num": child_group_num_modal_slct.value,
        "address": child_address_modal_inpt.value,
        "clinic_id": child_clinic_modal_slct.value,
        "entering_date": child_entering_date_modal_dtpk.value,
        "family_characteristics": child_family_characteristics_modal_slct.value,
        "family_microclimate": child_family_microclimate_modal_slct.value,
        "rest_and_class_opportunities": child_rest_and_class_opportunities_modal_slct.value,
        "case_history": child_case_history_modal_txt.value
    } 
    $.ajax({
        type: "PUT",
        async: true,
        url: "/api/v1/children/" + medcard_num,
        data: JSON.stringify(child),
        contentType: "application/json",
        dataType: 'json',
        success: (response) => {
            let general_div = document.querySelector('#general-main-div');
            general_div.innerHTML = '<strong>' + child.surname + ' ' + child.name + ' ' + child.patronymic + '</strong> <u><mark>' + child.birthday + ' г.р.</mark></u>, пол: <u><mark>' + child.sex + '</mark></u>,\
            характеристика образовательного учреждения: <u><mark>ДДУ</mark></u>,\
            дом. адрес (или адрес интернатного учреждения): <u><mark>' + child.address + '</mark></u>, обслуживающая поликлиника: <u><mark>' + response.clinic.name + '</mark></u>,\
            месяц, год поступления: <u><mark>' + child.entering_date + '</mark></u>';
            let anamnes_div = document.querySelector('#anamnes-main-div');
            innerHTML = '<p>Характеристика семьи: <u><mark>' + child.family_characteristics + '</mark></u>, микроклимат в семье: <u><mark>' + child.family_microclimate + '</mark></u>, \
            наличие у ребенка места для отдыха и занятий: <u><mark>' + child.rest_and_class_opportunities + '</mark></u>. </br>';
            if (child.case_history){
                innerHTML += '<div class="col-12">\
                    <label for="case_history" class="form-label"><strong>Семейный анамнез:</strong></label>\
                    <p>' + child.case_history + '</p>\
                    </div>'
            }
            innerHTML += '<small><i>*Для внесения изменений в данный блок нажмите на кнопку "Редактировать" в разделе "ОБЩИЕ СВЕДЕНИЯ О РЕБЕНКЕ"</i></small></p> ';
            anamnes_div.innerHTML = innerHTML;
        }
    });
})

/* ALLERGY */
allergy_commit_modal_btn.addEventListener('click', () => {
    var allergy = {
            "medcard_num": medcard_num,
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
                url: "/api/v1/children/" + medcard_num + "/allergyes/",
                data: JSON.stringify(allergy),
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
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#allergyModal" id="btn-update-'+ allergy["allergen"].replace(/ /g,'') +'" value="' + allergy["allergen"] + '///' + allergy["allergy_type"] + '///' + allergy["start_age"] + '///' + allergy["reaction_type"] + '///' + allergy["diagnosis_date"] + '///' + allergy["note"] + '" onclick="update_allergy(\'' + allergy["allergen"] + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" id="btn-delete-'+ allergy["allergen"].replace(/ /g,'') +'"  onclick="delete_allergy(\'' + allergy["allergen"] + '\')">Удалить</button>\
                    </div>'
                }
            });
            break;

        case 'update': 
            const allergen_name = allergy_close_modal_btn.value;
            allergy["prev_allergen"] = allergen_name;
            $.ajax({
                type: "PUT",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/allergyes/",
                data: JSON.stringify(allergy),
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
var isFather = true; // For check parent type

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
    isFather = true;
    parent_add_set_info();
}

function mother_add_btn_click() {
    parent_modal_header.innerHTML = 'Добавить сведения о матери';
    isFather = false;
    parent_add_set_info();
}

function parent_update_set_info(unsplit_data){
    parent_data = unsplit_data.split('///');
    parent_close_modal_btn.value = parent_data[0]; 
    parent_surname_inpt.value = parent_data[1];
    parent_name_inpt.value = parent_data[2];
    parent_patronymic_inpt.value = parent_data[3];
    parent_birthday_year_dtpkr.value = parent_data[4];
    parent_edu_slct.value = parent_data[5].trim();
    parent_phone_inpt.value = parent_data[6].slice(1,11);
    parent_commit_modal_btn.value = 'update';
}

function father_update_btn_click(){
    parent_modal_header.innerHTML = 'Редактирование сведений об отце';
    const father_update_btn = document.getElementsByName('update-father-btn')[0]
    isFather = true;
    parent_update_set_info(father_update_btn.value);
}

function mother_update_btn_click(){
    parent_modal_header.innerHTML = 'Редактирование сведений о матери';
    const mother_update_btn = document.getElementsByName('update-mother-btn')[0];
    isFather = false;
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
        "header": parent_modal_header.innerHTML,
        "parent_type": isFather? 'father' : 'mother'
    };
    switch (parent_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/parents/",
                data: JSON.stringify(parent),
                contentType: "application/json",
                dataType: 'json',
                success: function(parent_data) {
                    switch (parent.parent_type) {
                        case 'father':
                            const father_div = document.getElementsByName('father-main-div')[0]
                            father_div.innerHTML = '<div name="div-father-' + parent_data.id + '" class="col-12 mb-3">\
                            <p><strong>Отец: </strong> <u><mark>' + parent.surname + ' ' +  parent.name + ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-father-btn" value="' + parent_data.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'" onclick="father_update_btn_click()">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-father-btn" onclick="delete_parent(\'father\')">Удалить</button>\
                            </div>\
                            </div>'
                            break;
                        
                        case 'mother':
                            const mother_div = document.getElementsByName('mother-main-div')[0]
                            mother_div.innerHTML = '<div name="div-mother-' + parent_data.id + '" class="col-12 mb-3">\
                            <p><strong>Мать: </strong> <u><mark>' + parent.surname + ' ' +  parent.name + ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-mother-btn" value="' + parent_data.id + '///' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'" onclick="mother_update_btn_click()">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mother-btn" onclick="delete_parent(\'mother\')">Удалить</button>\
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
            parent['id'] = parent_close_modal_btn.value;
            $.ajax({
                type: "PUT",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/parents/",
                data: JSON.stringify(parent),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    switch (parent.header) {
                        case 'Редактирование сведений об отце':
                            const father_div = document.getElementsByName('div-father-' + parent.id)[0]
                            father_div.innerHTML = '<p><strong>Отец: </strong> <u><mark>' + parent.surname + ' ' +  parent.name+ ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-father-btn" value="' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-father-btn" onclick="delete_parent(\'father\')">Удалить</button>\
                            </div>'
                            break;
                        
                        case 'Редактирование сведений о матери':
                            const mother_div = document.getElementsByName('div-mother-' + parent.id)[0]
                            mother_div.innerHTML = '<p><strong>Мать: </strong> <u><mark>' + parent.surname + ' ' +  parent.name+ ' ' +  parent.patronymic+ ', ' +  parent.birthday_year + 'г.р.</mark></u>, образование: <u><mark>' +  parent.education + '</mark></u> </br>\
                            <strong>тел.: </strong> <u><mark>' + parent.phone_num + '</mark></u>\
                            </p>\
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                                <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#parentModal" name="update-mother-btn" value="' + parent.surname + '///' + parent.name + '///' + parent.patronymic + '///' + parent.birthday_year + '///' + parent.education + '///' + parent.phone_num +'">Редактировать</button>\
                                <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mother-btn" onclick="delete_parent(\'mother\')">Удалить</button>\
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
            close_delete_modal_btn.value = 'father';
            break;
        
        case 'mother':
            delete_modal_header.innerHTML = 'Удалить сведения о матери';
            close_delete_modal_btn.value = 'mother';
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
            console.log(extra_class);
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/extra_classes/",
                data: JSON.stringify(extra_class),
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
                let prev_extra_classes_data = class_close_modal_btn.value.split('///');
                extra_class["prev_classes_type"] = prev_extra_classes_data[0];
                extra_class["prev_age"] = prev_extra_classes_data[1];
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/extra_classes/",
                    data: JSON.stringify(extra_class),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let extra_classes_div = document.getElementsByName('div-class-' + extra_class.prev_classes_type.replace(/ /g,'') + '-' + extra_class.prev_age)[0];
                        extra_classes_div.innerHTML = '<p><strong>' + extra_class.classes_type + '</strong> в возрасте: <u><mark>' + extra_class.age + '</mark></u> по <u><mark>' + extra_class.hours_on_week + '</mark></u> ч/нед.</p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#classModal" name="update-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="update_class(\'' + extra_class.classes_type +'\', \'' + extra_class.age + '\', \'' + extra_class.hours_on_week + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age + '-btn" onclick="delete_class(\'' + extra_class.classes_type +'\', \'' + extra_class.age + '\')">Удалить</button>\
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
        url: "/api/v1/children/" + medcard_num + "/past_illnesses/one",
        data: JSON.stringify(past_illness),
        contentType: "application/json",
        dataType: 'json',
        success: function(past_illness){
            past_illness_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            past_illness_commit_modal_btn.value = 'update';
            past_illness_close_modal_btn.value = past_illness.diagnosis + '///' + past_illness.start_date;
            past_illness_diagnosis_modal_inpt.value = past_illness.diagnosis;
            past_illness_start_date_modal_dtpkr.value = past_illness.start_date;
            past_illness_end_date_modal_dtpkr.value = past_illness.end_date;
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
        "end_date": past_illness_end_date_modal_dtpkr.value || null
    }
    switch (past_illness_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/past_illnesses/",
                data: JSON.stringify(past_illness),
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
                let prev_past_illness_data = past_illness_close_modal_btn.value.split('///');
                past_illness["prev_diagnosis"] = prev_past_illness_data[0];
                past_illness["prev_start_date"] = prev_past_illness_data[1];
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/past_illnesses/",
                    data: JSON.stringify(past_illness),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let past_illness_div = document.getElementsByName('div-past-illness-' + past_illness.prev_diagnosis.replace(/ /g, '') + '-' + past_illness.prev_start_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/hospitalizations/one",
        data: JSON.stringify(hospitalization),
        contentType: "application/json",
        dataType: 'json',
        success: function(hospitalization){
            hospitalization_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            hospitalization_commit_modal_btn.value = 'update';
            hospitalization_close_modal_btn.value = hospitalization.start_date;
            hospitalization_diagnosis_modal_txt.value = hospitalization.diagnosis;
            hospitalization_start_date_modal_dtpkr.value = hospitalization.start_date;
            hospitalization_end_date_modal_dtpkr.value = hospitalization.end_date;
            hospitalization_founding_modal_inpt.value = hospitalization.founding;
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
        "end_date": hospitalization_end_date_modal_dtpkr.value || null,
        "founding": hospitalization_founding_modal_inpt.value
    }
    switch (hospitalization_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/hospitalizations/",
                data: JSON.stringify(hospitalization),
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
                hospitalization["prev_start_date"] = hospitalization_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/hospitalizations/",
                    data: JSON.stringify(hospitalization),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let hospitalization_div = document.getElementsByName('div-hospitalization-' + hospitalization.prev_start_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/spa_treatments/one",
        data: JSON.stringify(spa_treatment),
        contentType: "application/json",
        dataType: 'json',
        success: function(spa_treatment){
            spa_treatment_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            spa_treatment_commit_modal_btn.value = 'update';
            spa_treatment_close_modal_btn.value = spa_treatment.start_date;
            spa_treatment_diagnosis_modal_txt.value = spa_treatment.diagnosis;
            spa_treatment_start_date_modal_dtpkr.value = spa_treatment.start_date;
            spa_treatment_end_date_modal_dtpkr.value = spa_treatment.end_date;
            spa_treatment_founding_modal_inpt.value = spa_treatment.founding_specialization;
            spa_treatment_climatic_zone_modal_slct.value = spa_treatment.climatic_zone;
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
        "end_date": spa_treatment_end_date_modal_dtpkr.value || null,
        "founding_specialization": spa_treatment_founding_modal_inpt.value,
        "climatic_zone": spa_treatment_climatic_zone_modal_slct.value
    }
    switch (spa_treatment_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/spa_treatments/",
                data: JSON.stringify(spa_treatment),
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
                spa_treatment["prev_start_date"] = spa_treatment_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/spa_treatments/",
                    data: JSON.stringify(spa_treatment),
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
                        let spa_treatment_div = document.getElementsByName('div-spa-treatment-' + spa_treatment.prev_start_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/medical_certificates/one",
        data: JSON.stringify(medical_certificate),
        contentType: "application/json",
        dataType: 'json',
        success: function(medical_certificate){
            medical_certificate_modal_header.innerHTML = 'Редактирование медицинской справки';
            medical_certificate_disease_modal_inpt.value = medical_certificate.disease;
            medical_certificate_start_date_modal_dtpkr.value = medical_certificate.start_date;
            medical_certificate_end_date_modal_dtpkr.value = medical_certificate.end_date;
            medical_certificate_sport_exemption_date_modal_dpkr.value = medical_certificate.sport_exemption_date;
            medical_certificate_vac_exemption_date_modal_dpkr.value = medical_certificate.vac_exemption_date;
            medical_certificate_doctor_modal_inpt.value = medical_certificate.doctor;
            medical_certificate_cert_date_modal_dtpkr.value = medical_certificate.cert_date;
            if (medical_certificate.infection_contact){
                medical_certificate_infection_contact_modal_chk.checked = true
            } else {
                medical_certificate_infection_contact_modal_chk.checked = false
            }
            medical_certificate_close_modal_btn.value = medical_certificate.disease + '///' + medical_certificate.cert_date;
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
        "infection_contact": medical_certificate_infection_contact_modal_chk.checked,
        "sport_exemption_date": medical_certificate_sport_exemption_date_modal_dpkr.value || null,
        "vac_exemption_date": medical_certificate_vac_exemption_date_modal_dpkr.value || null,
        "doctor": medical_certificate_doctor_modal_inpt.value
    };
    switch (medical_certificate_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/medical_certificates/",
                data: JSON.stringify(medical_certificate),
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
                prev_data = medical_certificate_close_modal_btn.value.split('///')
                medical_certificate["prev_disease"] = prev_data[0];
                medical_certificate["prev_cert_date"] = prev_data[1];
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/medical_certificates/",
                    data: JSON.stringify(medical_certificate),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        let medical_certificates_div = document.getElementsByName('div-medical-certificate-' + medical_certificate.prev_disease.replace(/ /g,'') + '-' + medical_certificate.prev_cert_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/dispensaryes/one",
        data: JSON.stringify(dispensary),
        contentType: "application/json",
        dataType: 'json',
        success: function(dispensary){
            dispensary_modal_header.innerHTML = "Редактирование сведений о перенесенном заболевании";
            dispensary_commit_modal_btn.value = 'update';
            dispensary_close_modal_btn.value = dispensary.start_date;
            dispensary_diagnosis_modal_inpt.value = dispensary.diagnosis;
            dispensary_specialist_modal_inpt.value = dispensary.specialist;
            dispensary_start_date_modal_dtpkr.value = dispensary.start_date;
            dispensary_end_date_modal_dtpkr.value = dispensary.end_date;
            dispensary_end_reason_modal_txt.value = dispensary.end_reason;
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
                url: "/api/v1/children/" + medcard_num + "/dispensaryes/",
                data: JSON.stringify(dispensary),
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
                dispensary["prev_start_date"] = dispensary_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/dispensaryes/",
                    data: JSON.stringify(dispensary),
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
                        let dispensary_div = document.getElementsByName('div-dispensary-' + dispensary.prev_start_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/visit_specialist_controls/all",
        data: JSON.stringify(visit_specialist_control),
        contentType: "application/json",
        dataType: 'json',
        success: function(visit_specialist_control){
            visit_specialist_control_add_btn.value = start_dispanser_date;
            let visit_specialist_control_div = document.querySelector('#visit-specialist-control-main-div')
            innerHTML = ""
            visit_specialist_control.forEach(element => {
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
        "fact_date": visit_specialist_control_fact_date_modal_dtpkr.value || null
    }
    switch (visit_specialist_control_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/visit_specialist_controls/",
                data: JSON.stringify(visit_specialist_control),
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
                visit_specialist_control["prev_assigned_date"] = visit_specialist_control_close_modal_btn.value || null
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/visit_specialist_controls/",
                    data: JSON.stringify(visit_specialist_control),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () =>{
                        let visit_specialist_control_div = document.getElementsByTagName('div-visit-specialist-control-'+ visit_specialist_control.prev_assigned_date)[0];
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
        url: "/api/v1/children/" + medcard_num + "/dewormings/one",
        data: JSON.stringify(deworming),
        contentType: "application/json",
        dataType: 'json',
        success: function(deworming){
            deworming_modal_header.innerHTML = "Редактирование сведений о дегельминтизации";
            deworming_commit_modal_btn.value = 'update';
            deworming_close_modal_btn.value = deworming.deworming_date;
            deworming_date_modal_dtpkr.value = deworming.deworming_date;
            deworming_result_modal_txt.value = deworming.result;
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
                url: "/api/v1/children/" + medcard_num + "/dewormings/",
                data: JSON.stringify(deworming),
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
                deworming["prev_deworming_date"] = deworming_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/dewormings/",
                    data: JSON.stringify(deworming),
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
                        let deworming_div = document.getElementsByName('div-deworming-' + deworming.prev_deworming_date)[0]
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
        url: "/api/v1/children/" + medcard_num + "/oral_sanations/one",
        data: JSON.stringify(oral_sanation),
        contentType: "application/json",
        dataType: 'json',
        success: function(oral_sanation){
            oral_sanation_modal_header.innerHTML = "Редактирование сведений о санации полости рта";
            oral_sanation_commit_modal_btn.value = 'update';
            oral_sanation_close_modal_btn.value = oral_sanation.sanation_date;
            oral_sanation_date_modal_dtpkr.value = oral_sanation.sanation_date;
            oral_sanation_dental_result_modal_txt.value = oral_sanation.dental_result;
            oral_sanation_result_modal_txt.value = oral_sanation.sanation_result;
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
                url: "/api/v1/children/" + medcard_num + "/oral_sanations/",
                data: JSON.stringify(oral_sanation),
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
                oral_sanation["prev_sanation_date"] = oral_sanation_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/oral_sanations/",
                    data: JSON.stringify(oral_sanation),
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
                        let oral_sanation_div = document.getElementsByName('div-oral-sanation-' + oral_sanation.prev_sanation_date)[0]
                        oral_sanation_div.innerHTML = innerHTML;
                        oral_sanation_div.setAttribute('name', 'div-oral-sanation-' + oral_sanation.sanation_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})



/* PREVACCINATION CHECKUP */
function prevaccination_checkup_add_set_info(){

    prevaccination_checkup_modal_header.innerHTML = "Добавление сведений об осмотре";
    prevaccination_checkup_examination_date_modal_dtpkr.value = "";
    prevaccination_checkup_diagnosis_modal_inpt.value = "";
    prevaccination_checkup_no_vac_date_modal_dtpkr.value = "";
    prevaccination_checkup_doctor_modal_inpt.value = "";
    prevaccination_checkup_commit_modal_btn.value = 'add'; 
}

function update_prevaccination_checkup(examination_date){
    var prevaccination_checkup = {
        "medcard_num": medcard_num,
        "examination_date": examination_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/prevaccination_checkups/one",
        data: JSON.stringify(prevaccination_checkup),
        contentType: "application/json",
        dataType: 'json',
        success: function(prevaccination_checkup){
            prevaccination_checkup_modal_header.innerHTML = "Редактирование сведений об осмотре";
            prevaccination_checkup_commit_modal_btn.value = 'update';
            prevaccination_checkup_close_modal_btn.value = prevaccination_checkup.examination_date;
            prevaccination_checkup_examination_date_modal_dtpkr.value = prevaccination_checkup.examination_date;
            prevaccination_checkup_diagnosis_modal_inpt.value = prevaccination_checkup.diagnosis;
            prevaccination_checkup_report_modal_slct.value = prevaccination_checkup.report;
            prevaccination_checkup_vac_name_modal_slct.value = prevaccination_checkup.vac_name_id;
            prevaccination_checkup_no_vac_date_modal_dtpkr.value = prevaccination_checkup.no_vac_date;
            prevaccination_checkup_doctor_modal_inpt.value = prevaccination_checkup.doctor;            
        }
    });    
}

function delete_prevaccination_checkup(examination_date){
    delete_modal_header.innerHTML = 'Удалить сведения об осмотре';
    close_delete_modal_btn.value = examination_date;
    delete_commit_modal_btn.value = 'delete_prevaccination_checkup';
}

prevaccination_checkup_commit_modal_btn.addEventListener('click', () =>{    
    var prevaccination_checkup = {
        "medcard_num": medcard_num,
        "examination_date": prevaccination_checkup_examination_date_modal_dtpkr.value,
        "diagnosis": prevaccination_checkup_diagnosis_modal_inpt.value,
        "report": prevaccination_checkup_report_modal_slct.value,
        "vac_name_id": prevaccination_checkup_vac_name_modal_slct.value,
        "no_vac_date": prevaccination_checkup_no_vac_date_modal_dtpkr.value || null,
        "doctor":  prevaccination_checkup_doctor_modal_inpt.value
    };
    switch (prevaccination_checkup_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/prevaccination_checkups/",
                data: JSON.stringify(prevaccination_checkup),
                contentType: "application/json",
                dataType: 'json',
                success: function(prevaccination_checkup_data) {
                    const vac_name = prevaccination_checkup_vac_name_modal_slct.options[prevaccination_checkup_vac_name_modal_slct.selectedIndex].textContent;
                    innerHTML = '<div name="div-prevaccination-checkup-' + prevaccination_checkup.examination_date + '" class="col-12 mb-3">\
                    <p><strong>' + vac_name + '</strong> Дата осмотра: <u><mark>' + prevaccination_checkup.examination_date + '</mark></u>, Возраст: <u><mark>' + prevaccination_checkup_data.age + '</mark></u>\
                    Диагноз: <u><mark>' + prevaccination_checkup.diagnosis + '</mark></u>, Заключение: <u><mark>' + prevaccination_checkup.report + '</mark></u> <br>'
                    if (prevaccination_checkup.no_vac_date){
                        innerHTML += '<strong>Мед. отвод до: </strong><u><mark>' + prevaccination_checkup.no_vac_date + '</mark></u> <br></br>'
                    }
                    innerHTML += 'Врач: <u><mark>' + prevaccination_checkup.doctor + '</mark></u></p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#prevaccinationCheckupModal" name="update-prevaccination-checkup-' + prevaccination_checkup.examination_date + '-btn" onclick="update_prevaccination_checkup(\'' + prevaccination_checkup.examination_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-prevaccination-checkup-' + prevaccination_checkup.examination_date + '-btn" onclick="delete_prevaccination_checkup(\'' + prevaccination_checkup.examination_date + '\')">Удалить</button>\
                    </div>\
                    </div>';
                    let prevaccination_checkup_div = document.querySelector('#prevaccination-checkup-main-div');
                    prevaccination_checkup_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                prevaccination_checkup["prev_examination_date"] = prevaccination_checkup_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/prevaccination_checkups/",
                    data: JSON.stringify(prevaccination_checkup),
                    contentType: "application/json",
                    dataType: 'json',
                    success: function(prevaccination_checkup_data){                        
                        const vac_name = prevaccination_checkup_vac_name_modal_slct.options[prevaccination_checkup_vac_name_modal_slct.selectedIndex].textContent;
                        innerHTML = '<p><strong>' + vac_name + '</strong> Дата осмотра: <u><mark>' + prevaccination_checkup.examination_date + '</mark></u>, Возраст: <u><mark>' + prevaccination_checkup_data.age + '</mark></u>\
                        Диагноз: <u><mark>' + prevaccination_checkup.diagnosis + '</mark></u>, Заключение: <u><mark>' + prevaccination_checkup.report + '</mark></u> <br>'
                        if (prevaccination_checkup.no_vac_date){
                            innerHTML += '<strong>Мед. отвод до: </strong><u><mark>' + prevaccination_checkup.no_vac_date + '</mark></u> <br></br>'
                        }
                        innerHTML += 'Врач: <u><mark>' + prevaccination_checkup.doctor + '</mark></u></p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#prevaccinationCheckupModal" name="update-prevaccination-checkup-' + prevaccination_checkup.examination_date + '-btn" onclick="update_prevaccination_checkup(\'' + prevaccination_checkup.examination_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-prevaccination-checkup-' + prevaccination_checkup.examination_date + '-btn" onclick="delete_prevaccination_checkup(\'' + prevaccination_checkup.examination_date + '\')">Удалить</button>\
                        </div>';
                        let prevaccination_checkup_div = document.getElementsByName('div-prevaccination-checkup-' + prevaccination_checkup.prev_examination_date)[0]
                        prevaccination_checkup_div.innerHTML = innerHTML;
                        prevaccination_checkup_div.setAttribute('name', 'div-prevaccination-checkup-' + prevaccination_checkup.examination_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* PROF VACCINATION */
function prof_vaccination_add_set_info(){

    prof_vaccination_modal_header.innerHTML = "Добавление сведений об прививке";
    prof_vaccination_date_modal_dtpk.value = "2023-04-14";
    prof_vaccination_serial_modal_inpt.value = "АА2548";
    prof_vaccination_dose_modal_inpt.value = "15.2";
    prof_vaccination_doctor_modal_inpt.value = "Иванов Иван Иванович";
    prof_vaccination_commit_modal_btn.value = 'add'; 
}

function update_prof_vaccination(vac_name_id, vac_type){
    var prof_vaccination = {
        "medcard_num": medcard_num,
        "vac_name_id": vac_name_id,
        "vac_type": vac_type
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/prof_vaccinations/one",
        data: JSON.stringify(prof_vaccination),
        contentType: "application/json",
        dataType: 'json',
        success: function(prof_vaccination_data){
            prof_vaccination_modal_header.innerHTML = "Редактирование сведений об осмотре";
            prof_vaccination_commit_modal_btn.value = 'update';
            prof_vaccination_close_modal_btn.value = vac_name_id + '///' + vac_type;
            prof_vaccination_vac_name_modal_slct.value = prof_vaccination.vac_name_id;
            prof_vaccination_vac_type_modal_slct.value = prof_vaccination_data.vac_type;
            prof_vaccination_date_modal_dtpk.value = prof_vaccination_data.vac_date;
            prof_vaccination_serial_modal_inpt.value = prof_vaccination_data.serial;
            prof_vaccination_dose_modal_inpt.value = prof_vaccination_data.dose;
            prof_vaccination_introduction_method_modal_slct.value = prof_vaccination_data.introduction_method;
            prof_vaccination_reaction_modal_slct.value = prof_vaccination_data.reaction;
            prof_vaccination_doctor_modal_inpt.value = prof_vaccination_data.doctor;
        }
    });    
}

function delete_prof_vaccination(vac_name_id, vac_type){
    delete_modal_header.innerHTML = 'Удалить сведения о прививке';
    close_delete_modal_btn.value = vac_name_id + '///' + vac_type;
    delete_commit_modal_btn.value = 'delete_prof_vaccination';
}

prof_vaccination_commit_modal_btn.addEventListener('click', () =>{    
    var prof_vaccination = {
        "medcard_num": medcard_num,
        "vac_name_id": prof_vaccination_vac_name_modal_slct.value,
        "vac_type": prof_vaccination_vac_type_modal_slct.value,
        "vac_date": prof_vaccination_date_modal_dtpk.value,
        "serial":  prof_vaccination_serial_modal_inpt.value,
        "dose": prof_vaccination_dose_modal_inpt.value,
        "introduction_method": prof_vaccination_introduction_method_modal_slct.value,
        "reaction": prof_vaccination_reaction_modal_slct.value,
        "doctor": prof_vaccination_doctor_modal_inpt.value 
    };
    switch (prof_vaccination_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/vaccinations/",
                data: JSON.stringify(prof_vaccination),
                contentType: "application/json",
                dataType: 'json',
                success: (vac) => {
                    innerHTML = '<div name="div-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'') + '" class="col-12 mb-3">\
                    <p><strong>' + vac.vac_name.name + '</strong> <strong>' + prof_vaccination.vac_type + '</strong> Дата: <u><mark>' + prof_vaccination.vac_date + '</mark></u>, \
                        серия: <u><mark>' + prof_vaccination.serial + '</mark></u>, доза: <u><mark>' + prof_vaccination.dose + '</mark></u>, \
                        способ введения: <u><mark>' + prof_vaccination.introduction_method + '</mark></u>, реакция: <u><mark>' + prof_vaccination.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + prof_vaccination.doctor + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#profVaccinationModal" name="update-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="update_prof_vaccination(\'' + prof_vaccination.vac_name_id + '\', \'' + prof_vaccination.vac_type + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="delete_prof_vaccination(\'' + prof_vaccination.vac_name_id + '\', \'' + prof_vaccination.vac_type + '\')">Удалить</button>\
                        </div>\
                    </div>';
                    let prof_vaccination_div = document.querySelector('#prof-vaccination-main-div');
                    prof_vaccination_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                let pk_data = prof_vaccination_close_modal_btn.value.split('///');
                prof_vaccination["prev_vac_name_id"] = pk_data[0];
                prof_vaccination["prev_vac_type"] = pk_data[1];
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/vaccinations/",
                    data: JSON.stringify(prof_vaccination),
                    contentType: "application/json",
                    dataType: 'json',
                    success: (vac) => {
                        innerHTML = '<p><strong>' + vac.vac_name.name + '</strong> <strong>' + prof_vaccination.vac_type + '</strong> Дата: <u><mark>' + prof_vaccination.vac_date + '</mark></u>, \
                        серия: <u><mark>' + prof_vaccination.serial + '</mark></u>, доза: <u><mark>' + prof_vaccination.dose + '</mark></u>, \
                        способ введения: <u><mark>' + prof_vaccination.introduction_method + '</mark></u>, реакция: <u><mark>' + prof_vaccination.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + prof_vaccination.doctor + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#profVaccinationModal" name="update-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="update_prof_vaccination(\'' + prof_vaccination.vac_name_id + '\', \'' + prof_vaccination.vac_type + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="delete_prof_vaccination(\'' + prof_vaccination.vac_name_id + '\', \'' + prof_vaccination.vac_type + '\')">Удалить</button>\
                        </div>';
                        let prof_vaccination_div = document.getElementsByName('div-prof-vaccination-' + prof_vaccination.prev_vac_name_id + '-' + prof_vaccination.prev_vac_type.replace(/ /g,''))[0]
                        prof_vaccination_div.innerHTML = innerHTML;
                        prof_vaccination_div.setAttribute('name', 'div-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,'')) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* epid VACCINATION */
function epid_vaccination_add_set_info(){

    epid_vaccination_modal_header.innerHTML = "Добавление сведений об прививке";
    epid_vaccination_date_modal_dtpk.value = "2023-01-01";
    epid_vaccination_serial_modal_inpt.value = "";
    epid_vaccination_dose_modal_inpt.value = "";
    epid_vaccination_doctor_modal_inpt.value = "";
    epid_vaccination_commit_modal_btn.value = 'add'; 
}

function update_epid_vaccination(vac_name_id, vac_type){
    var epid_vaccination = {
        "medcard_num": medcard_num,
        "vac_name_id": vac_name_id,
        "vac_type": vac_type
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/epid_vaccinations/one",
        data: JSON.stringify(epid_vaccination),
        contentType: "application/json",
        dataType: 'json',
        success: function(epid_vaccination){
            epid_vaccination_modal_header.innerHTML = "Редактирование сведений об осмотре";
            epid_vaccination_commit_modal_btn.value = 'update';
            epid_vaccination_close_modal_btn.value = epid_vaccination.vac_name_id + '///' + epid_vaccination.vac_type;
            epid_vaccination_vac_name_modal_slct.value = epid_vaccination.vac_name_id;
            epid_vaccination_vac_type_modal_slct.value = epid_vaccination.vac_type;
            epid_vaccination_date_modal_dtpk.value = epid_vaccination.vac_date;
            epid_vaccination_serial_modal_inpt.value = epid_vaccination.serial;
            epid_vaccination_dose_modal_inpt.value = epid_vaccination.dose;
            epid_vaccination_introduction_method_modal_slct.value = epid_vaccination.introduction_method;
            epid_vaccination_reaction_modal_slct.value = epid_vaccination.reaction;
            epid_vaccination_doctor_modal_inpt.value = epid_vaccination.doctor;
        }
    });    
}

function delete_epid_vaccination(vac_name_id, vac_type){
    delete_modal_header.innerHTML = 'Удалить сведения о прививке';
    close_delete_modal_btn.value = vac_name_id + '///' + vac_type;
    delete_commit_modal_btn.value = 'delete_epid_vaccination';
}

epid_vaccination_commit_modal_btn.addEventListener('click', () =>{    
    var epid_vaccination = {
        "medcard_num": medcard_num,
        "vac_name_id": epid_vaccination_vac_name_modal_slct.value,
        "vac_type": epid_vaccination_vac_type_modal_slct.value,
        "vac_date": epid_vaccination_date_modal_dtpk.value,
        "serial":  epid_vaccination_serial_modal_inpt.value,
        "dose": epid_vaccination_dose_modal_inpt.value,
        "introduction_method": epid_vaccination_introduction_method_modal_slct.value,
        "reaction": epid_vaccination_reaction_modal_slct.value,
        "doctor": epid_vaccination_doctor_modal_inpt.value 
    };
    switch (epid_vaccination_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/vaccinations/",
                data: JSON.stringify(epid_vaccination),
                contentType: "application/json",
                dataType: 'json',
                success: (vac) => {
                    innerHTML = '<div name="div-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'') + '" class="col-12 mb-3">\
                    <p><strong>' + vac.vac_name.name + '</strong> <strong>' + epid_vaccination.vac_type + '</strong> Дата: <u><mark>' + epid_vaccination.vac_date + '</mark></u>, \
                        серия: <u><mark>' + epid_vaccination.serial + '</mark></u>, доза: <u><mark>' + epid_vaccination.dose + '</mark></u>, \
                        способ введения: <u><mark>' + epid_vaccination.introduction_method + '</mark></u>, реакция: <u><mark>' + epid_vaccination.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + epid_vaccination.doctor + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#epidVaccinationModal" name="update-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="update_epid_vaccination(\'' + epid_vaccination.vac_name_id + '\', \'' + epid_vaccination.vac_type + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="delete_epid_vaccination(\'' + epid_vaccination.vac_name_id + '\', \'' + epid_vaccination.vac_type + '\')">Удалить</button>\
                        </div>\
                    </div>';
                    let epid_vaccination_div = document.querySelector('#epid-vaccination-main-div');
                    epid_vaccination_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                let pk_data = epid_vaccination_close_modal_btn.value.split('///');
                epid_vaccination["prev_vac_name_id"] = pk_data[0];
                epid_vaccination["prev_vac_type"] = pk_data[1];
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/vaccinations/",
                    data: JSON.stringify(epid_vaccination),
                    contentType: "application/json",
                    dataType: 'json',
                    success: (vac) => {
                        innerHTML = '<p><strong>' + vac.vac_name.name + '</strong> <strong>' + epid_vaccination.vac_type + '</strong> Дата: <u><mark>' + epid_vaccination.vac_date + '</mark></u>, \
                        серия: <u><mark>' + epid_vaccination.serial + '</mark></u>, доза: <u><mark>' + epid_vaccination.dose + '</mark></u>, \
                        способ введения: <u><mark>' + epid_vaccination.introduction_method + '</mark></u>, реакция: <u><mark>' + epid_vaccination.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + epid_vaccination.doctor + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#epidVaccinationModal" name="update-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="update_epid_vaccination(\'' + epid_vaccination.vac_name_id + '\', \'' + epid_vaccination.vac_type + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'') + '-btn" onclick="delete_epid_vaccination(\'' + epid_vaccination.vac_name_id + '\', \'' + epid_vaccination.vac_type + '\')">Удалить</button>\
                        </div>';
                        let epid_vaccination_div = document.getElementsByName('div-epid-vaccination-' + epid_vaccination.prev_vac_name_id + '-' + epid_vaccination.prev_vac_type.replace(/ /g,''))[0]
                        epid_vaccination_div.innerHTML = innerHTML;
                        epid_vaccination_div.setAttribute('name', 'div-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,'')) 
                    }
                });
                break;
    
        default:
            break;
    }
})

/* GG INJECTION */
function gg_injection_add_set_info(){

    gg_injection_modal_header.innerHTML = "Добавление сведений о введении гамма-глобулина";
    gg_injection_date_modal_dtpk.value = "2023-04-14";
    gg_injection_reason_modal_txt.value = "Повышение иммунитета"
    gg_injection_serial_modal_inpt.value = "АА2548";
    gg_injection_dose_modal_inpt.value = "15.2";
    gg_injection_doctor_modal_inpt.value = "Иванов Иван Иванович";
    gg_injection_commit_modal_btn.value = 'add'; 
}

function update_gg_injection(vac_date){
    var gg_injection = {
        "medcard_num": medcard_num,
        "vac_date": vac_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/gg_injections/one",
        data: JSON.stringify(gg_injection),
        contentType: "application/json",
        dataType: 'json',
        success: function(gg_injection){
            gg_injection_modal_header.innerHTML = "Редактирование сведений о введении гамма-глобулина";
            gg_injection_commit_modal_btn.value = 'update';
            gg_injection_close_modal_btn.value = gg_injection.vac_date;
            gg_injection_reason_modal_txt.value = gg_injection.reason;
            gg_injection_date_modal_dtpk.value = gg_injection.vac_date;
            gg_injection_serial_modal_inpt.value = gg_injection.serial;
            gg_injection_dose_modal_inpt.value = gg_injection.dose;
            gg_injection_reaction_modal_slct.value = gg_injection.reaction;
            gg_injection_doctor_modal_inpt.value = gg_injection.doctor;
        }
    });    
}

function delete_gg_injection(vac_date){
    delete_modal_header.innerHTML = 'Удалить сведения о введении гамма-глобулина';
    close_delete_modal_btn.value = vac_date;
    delete_commit_modal_btn.value = 'delete_gg_injection';
}

gg_injection_commit_modal_btn.addEventListener('click', () =>{    
    var gg_injection = {
        "medcard_num": medcard_num,
        "vac_date": gg_injection_date_modal_dtpk.value,
        "reason": gg_injection_reason_modal_txt.value,
        "serial":  gg_injection_serial_modal_inpt.value,
        "dose": gg_injection_dose_modal_inpt.value,
        "reaction": gg_injection_reaction_modal_slct.value,
        "doctor": gg_injection_doctor_modal_inpt.value 
    };
    switch (gg_injection_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/gg_injections/",
                data: JSON.stringify(gg_injection),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-gg-injection-' + gg_injection.vac_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + gg_injection.vac_date + '</mark></u> <br>\
                        Причина: <u><mark>' + gg_injection.reason + '</mark></u> <br>\
                        Серия: <u><mark>' + gg_injection.serial + '</mark></u>, доза: <u><mark>' + gg_injection.dose + '</mark></u>, реакция: <u><mark>' + gg_injection.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + gg_injection.doctor + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#ggInjectionModal" name="update-gg-injection-' + gg_injection.vac_date + '-btn" onclick="update_gg_injection(\'' + gg_injection.vac_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-gg-injection-' + gg_injection.vac_date + '-btn" onclick="delete_gg_injection(\'' + gg_injection.vac_date + '\')">Удалить</button>\
                    </div>\
                    </div>';
                    let gg_injection_div = document.querySelector('#gg-injection-main-div');
                    gg_injection_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                gg_injection["prev_vac_date"] = gg_injection_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/gg_injections/",
                    data: JSON.stringify(gg_injection),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + gg_injection.vac_date + '</mark></u> <br>\
                        Причина: <u><mark>' + gg_injection.reason + '</mark></u> <br>\
                        Серия: <u><mark>' + gg_injection.serial + '</mark></u>, доза: <u><mark>' + gg_injection.dose + '</mark></u>, реакция: <u><mark>' + gg_injection.reaction + '</mark></u><br>\
                        Врач: <u><mark>' + gg_injection.doctor + '</mark></u>\
                        </p>\
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                            <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#ggInjectionModal" name="update-gg-injection-' + gg_injection.vac_date + '-btn" onclick="update_gg_injection(\'' + gg_injection.vac_date + '\')">Редактировать</button>\
                            <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-gg-injection-' + gg_injection.vac_date + '-btn" onclick="delete_gg_injection(\'' + gg_injection.vac_date + '\')">Удалить</button>\
                        </div>';
                        let gg_injection_div = document.getElementsByName('div-gg-injection-' + gg_injection.prev_vac_date)[0]
                        gg_injection_div.innerHTML = innerHTML;
                        gg_injection_div.setAttribute('name', 'div-gg-injection-' + gg_injection.vac_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* mantoux test */
function mantoux_test_add_set_info(){
    mantoux_test_modal_header.innerHTML = "Добавление сведений о реакции Манту";
    mantoux_test_date_modal_dtpk.value = "2023-04-14";
    mantoux_test_commit_modal_btn.value = 'add'; 
}

function update_mantoux_test(check_date){
    var mantoux_test = {
        "medcard_num": medcard_num,
        "check_date": check_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/mantoux_tests/one",
        data: JSON.stringify(mantoux_test),
        contentType: "application/json",
        dataType: 'json',
        success: function(mantoux_test){
            mantoux_test_modal_header.innerHTML = "Редактирование сведений о реакции Манту";
            mantoux_test_commit_modal_btn.value = 'update';
            mantoux_test_close_modal_btn.value = mantoux_test.check_date;
            mantoux_test_result_modal_slct.value = mantoux_test.result;
            mantoux_test_date_modal_dtpk.value = mantoux_test.check_date;
        }
    });    
}

function delete_mantoux_test(check_date){
    delete_modal_header.innerHTML = 'Удалить сведения о введении гамма-глобулина';
    close_delete_modal_btn.value = check_date;
    delete_commit_modal_btn.value = 'delete_mantoux_test';
}

mantoux_test_commit_modal_btn.addEventListener('click', () =>{    
    var mantoux_test = {
        "medcard_num": medcard_num,
        "check_date": mantoux_test_date_modal_dtpk.value,
        "result": mantoux_test_result_modal_slct.value        
    };
    switch (mantoux_test_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/mantoux_tests/",
                data: JSON.stringify(mantoux_test),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-mantoux-test-' + mantoux_test.check_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + mantoux_test.check_date + '</mark></u> <br>\
                        Результат: <u><mark>' + mantoux_test.result  + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#mantouxTestModal" name="update-mantoux-test-' + mantoux_test.check_date + '-btn" onclick="update_mantoux_test(\'' + mantoux_test.check_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mantoux-test-' + mantoux_test.check_date + '-btn" onclick="delete_mantoux_test(\'' + mantoux_test.check_date + '\')">Удалить</button>\
                    </div>\
                </div>';
                    let mantoux_test_div = document.querySelector('#mantoux-test-main-div');
                    mantoux_test_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                mantoux_test["prev_check_date"] = mantoux_test_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/mantoux_tests/",
                    data: JSON.stringify(mantoux_test),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + mantoux_test.check_date + '</mark></u> <br>\
                        Результат: <u><mark>' + mantoux_test.result  + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#mantouxTestModal" name="update-mantoux-test-' + mantoux_test.check_date + '-btn" onclick="update_mantoux_test(\'' + mantoux_test.check_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-mantoux-test-' + mantoux_test.check_date + '-btn" onclick="delete_mantoux_test(\'' + mantoux_test.check_date + '\')">Удалить</button>\
                    </div>';
                        let mantoux_test_div = document.getElementsByName('div-mantoux-test-' + mantoux_test.prev_check_date)[0]
                        mantoux_test_div.innerHTML = innerHTML;
                        mantoux_test_div.setAttribute('name', 'div-mantoux-test-' + mantoux_test.check_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* TUB VAC */
function tub_vac_add_set_info(){

    tub_vac_modal_header.innerHTML = "Добавление сведений о введении прививки против туберкулеза (БЦЖ)";
    tub_vac_date_modal_dtpk.value = "2023-04-14";
    tub_vac_serial_modal_inpt.value = "АА2548";
    tub_vac_dose_modal_inpt.value = "15.2";
    tub_vac_doctor_modal_inpt.value = "Иванов Иван Иванович";
    tub_vac_commit_modal_btn.value = 'add'; 
}

function update_tub_vac(vac_date){
    var tub_vac = {
        "medcard_num": medcard_num,
        "vac_date": vac_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/tub_vacs/one",
        data: JSON.stringify(tub_vac),
        contentType: "application/json",
        dataType: 'json',
        success: function(tub_vac){
            tub_vac_modal_header.innerHTML = "Редактирование сведений о введении прививки против туберкулеза (БЦЖ)";
            tub_vac_commit_modal_btn.value = 'update';
            tub_vac_close_modal_btn.value = tub_vac.vac_date;
            tub_vac_date_modal_dtpk.value = tub_vac.vac_date;
            tub_vac_serial_modal_inpt.value = tub_vac.serial;
            tub_vac_dose_modal_inpt.value = tub_vac.dose;
            tub_vac_doctor_modal_inpt.value = tub_vac.doctor;
        }
    });    
}

function delete_tub_vac(vac_date){
    delete_modal_header.innerHTML = 'Удалить сведения о введении прививки против туберкулеза (БЦЖ)';
    close_delete_modal_btn.value = vac_date;
    delete_commit_modal_btn.value = 'delete_tub_vac';
}

tub_vac_commit_modal_btn.addEventListener('click', () =>{    
    var tub_vac = {
        "medcard_num": medcard_num,
        "vac_date": tub_vac_date_modal_dtpk.value,
        "serial":  tub_vac_serial_modal_inpt.value,
        "dose": tub_vac_dose_modal_inpt.value,
        "doctor": tub_vac_doctor_modal_inpt.value 
    };
    switch (tub_vac_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/tub_vacs/",
                data: JSON.stringify(tub_vac),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-tub-vac-' + tub_vac.vac_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + tub_vac.vac_date + '</mark></u>\
                        Серия: <u><mark>' + tub_vac.serial + '</mark></u>, доза: <u><mark>' + tub_vac.dose + '</mark></u><br>\
                        Врач: <u><mark>' + tub_vac.doctor + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#tubVacModal" name="update-tub-vac-' + tub_vac.vac_date + '-btn" onclick="update_tub_vac(\'' + tub_vac.vac_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-tub-vac-' + tub_vac.vac_date + '-btn" onclick="delete_tub_vac(\'' + tub_vac.vac_date + '\')">Удалить</button>\
                    </div>\
                </div>';
                    let tub_vac_div = document.querySelector('#tub-vac-main-div');
                    tub_vac_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                tub_vac["prev_vac_date"] = tub_vac_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/tub_vacs/",
                    data: JSON.stringify(tub_vac),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + tub_vac.vac_date + '</mark></u>\
                        Серия: <u><mark>' + tub_vac.serial + '</mark></u>, доза: <u><mark>' + tub_vac.dose + '</mark></u><br>\
                        Врач: <u><mark>' + tub_vac.doctor + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#tubVacModal" name="update-tub-vac-' + tub_vac.vac_date + '-btn" onclick="update_tub_vac(\'' + tub_vac.vac_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-tub-vac-' + tub_vac.vac_date + '-btn" onclick="delete_tub_vac(\'' + tub_vac.vac_date + '\')">Удалить</button>\
                    </div>';
                        let tub_vac_div = document.getElementsByName('div-tub-vac-' + tub_vac.prev_vac_date)[0]
                        tub_vac_div.innerHTML = innerHTML;
                        tub_vac_div.setAttribute('name', 'div-tub-vac-' + tub_vac.vac_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* MEDICAL EXAMINATION */
function medical_examination_add_set_info(){

    medical_examination_modal_header.innerHTML = "Добавление сведений о медицинском осмотре";
    medical_examination_date_modal_dtpk.value = "2023-01-01";
    medical_examination_height_modal_inpt.value = "";
    medical_examination_weight_modal_inpt.value = "";
    medical_examination_complaints_modal_txt.value = "";
    medical_examination_pediatrician_modal_txt.value = "";
    medical_examination_orthopaedist_modal_txt.value = "";
    medical_examination_ophthalmologist_modal_txt.value = "";
    medical_examination_otolaryngologist_modal_txt.value = "";
    medical_examination_dermatologist_modal_txt.value = "";
    medical_examination_neurologist_modal_txt.value = "";
    medical_examination_speech_therapist_modal_txt.value = "";
    medical_examination_denta_surgeon_modal_txt.value = "";
    medical_examination_psychologist_modal_txt.value = "";
    medical_examination_other_doctors_modal_txt.value = "";
    medical_examination_blood_test_modal_txt.value = "";
    medical_examination_urine_analysis_modal_txt.value = "";
    medical_examination_feces_analysis_modal_txt.value = "";
    medical_examination_general_diagnosis_modal_txt.value = "";
    medical_examination_physical_development_modal_txt.value = "";
    medical_examination_mental_development_modal_txt.value = "";
    medical_examination_med_and_ped_conclusion_modal_txt.value = "";
    medical_examination_recommendations_modal_txt.value = "";
    medical_examination_commit_modal_btn.value = 'add'; 
}

function update_medical_examination(period){
    var medical_examination = {
        "medcard_num": medcard_num,
        "period": period
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/medical_examinations/one",
        data: JSON.stringify(medical_examination),
        contentType: "application/json",
        dataType: 'json',
        success: function(medical_examination){
            medical_examination_modal_header.innerHTML = "Редактирование сведений о медицинском осмотре";
            medical_examination_commit_modal_btn.value = 'update';
            medical_examination_close_modal_btn.value = medical_examination.period;
            medical_examination_period_modal_slct.value = medical_examination.period;
            medical_examination_date_modal_dtpk.value = medical_examination.examination_date;
            medical_examination_height_modal_inpt.value = medical_examination.height;
            medical_examination_weight_modal_inpt.value = medical_examination.weight;
            medical_examination_complaints_modal_txt.value = medical_examination.complaints;
            medical_examination_pediatrician_modal_txt.value = medical_examination.pediatrician;
            medical_examination_orthopaedist_modal_txt.value = medical_examination.orthopaedist;
            medical_examination_ophthalmologist_modal_txt.value = medical_examination.ophthalmologist;
            medical_examination_otolaryngologist_modal_txt.value = medical_examination.otolaryngologist;
            medical_examination_dermatologist_modal_txt.value = medical_examination.dermatologist;
            medical_examination_neurologist_modal_txt.value = medical_examination.neurologist;
            medical_examination_speech_therapist_modal_txt.value = medical_examination.speech_therapist;
            medical_examination_denta_surgeon_modal_txt.value = medical_examination.denta_surgeon;
            medical_examination_psychologist_modal_txt.value = medical_examination.psychologist;
            medical_examination_other_doctors_modal_txt.value = medical_examination.other_doctors;
            medical_examination_blood_test_modal_txt.value = medical_examination.blood_test;
            medical_examination_urine_analysis_modal_txt.value = medical_examination.urine_analysis;
            medical_examination_feces_analysis_modal_txt.value = medical_examination.feces_analysis;
            medical_examination_general_diagnosis_modal_txt.value = medical_examination.general_diagnosis;
            medical_examination_physical_development_modal_txt.value = medical_examination.physical_development;
            medical_examination_mental_development_modal_txt.value = medical_examination.mental_development;
            medical_examination_health_group_modal_slct.value = medical_examination.health_group;
            medical_examination_sport_group_modal_slct.value = medical_examination.sport_group;
            medical_examination_med_and_ped_conclusion_modal_txt.value = medical_examination.med_and_ped_conclusion;
            medical_examination_recommendations_modal_txt.value = medical_examination.recommendations;
        }
    });    
}

function delete_medical_examination(period){
    delete_modal_header.innerHTML = 'Удалить сведения о медицинском осмотре';
    close_delete_modal_btn.value = period;
    delete_commit_modal_btn.value = 'delete_medical_examination';
}

medical_examination_commit_modal_btn.addEventListener('click', () =>{    
    var medical_examination = {
        "medcard_num": medcard_num,
        "period":  medical_examination_period_modal_slct.value,
        "examination_date": medical_examination_date_modal_dtpk.value,
        "height": medical_examination_height_modal_inpt.value,
        "weight": medical_examination_weight_modal_inpt.value,
        "complaints": medical_examination_complaints_modal_txt.value,
        "pediatrician": medical_examination_pediatrician_modal_txt.value,
        "orthopaedist":  medical_examination_orthopaedist_modal_txt.value,
        "ophthalmologist": medical_examination_ophthalmologist_modal_txt.value,
        "otolaryngologist": medical_examination_otolaryngologist_modal_txt.value,
        "dermatologist": medical_examination_dermatologist_modal_txt.value,
        "neurologist": medical_examination_neurologist_modal_txt.value,
        "speech_therapist": medical_examination_speech_therapist_modal_txt.value,
        "denta_surgeon": medical_examination_denta_surgeon_modal_txt.value,
        "psychologist": medical_examination_psychologist_modal_txt.value,
        "other_doctors": medical_examination_other_doctors_modal_txt.value,
        "blood_test": medical_examination_blood_test_modal_txt.value,
        "urine_analysis": medical_examination_urine_analysis_modal_txt.value,
        "feces_analysis": medical_examination_feces_analysis_modal_txt.value,
        "general_diagnosis": medical_examination_general_diagnosis_modal_txt.value,
        "physical_development": medical_examination_physical_development_modal_txt.value,
        "mental_development": medical_examination_mental_development_modal_txt.value,
        "health_group": medical_examination_health_group_modal_slct.value,
        "sport_group": medical_examination_sport_group_modal_slct.value,
        "med_and_ped_conclusion": medical_examination_med_and_ped_conclusion_modal_txt.value,
        "recommendations": medical_examination_recommendations_modal_txt.value
    };
    switch (medical_examination_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/medical_examinations/",
                data: JSON.stringify(medical_examination),
                contentType: "application/json",
                dataType: 'json',
                success: (medical_examination_data) => {
                    innerHTML = '<div name="div-medical-examination-' + medical_examination.period.replace(/ /g,'') + '" class="col-12 mb-3">\
                    <p><strong>Период обследования: </strong><u><mark>' + medical_examination.period  + '</mark></u> <br>\
                        Дата обследования: <u><mark>' + medical_examination.examination_date + '</mark></u> Возраст: <u><mark>' + medical_examination_data.age + '</mark></u><br>\
                        Длина тела, см: <u><mark>' + medical_examination.height + '</mark></u>, масса тела, кг: <u><mark>' + medical_examination.weight + '</mark></u><br>\
                        Жалобы: <u><mark>' + medical_examination.complaints + '</mark></u><br>\
                        Педиатр: <u><mark>' + medical_examination.pediatrician + '</mark></u><br>\
                        Ортопед: <u><mark>' + medical_examination.orthopaedist + '</mark></u><br>\
                        Офтальмолог: <u><mark>' + medical_examination.ophthalmologist + '</mark></u><br>\
                        Отоларинголог: <u><mark>' + medical_examination.otolaryngologist + '</mark></u><br>\
                        Дерматолог: <u><mark>' + medical_examination.dermatologist + '</mark></u><br>\
                        Невролог: <u><mark>' + medical_examination.neurologist + '</mark></u><br>\
                        Логопед: <u><mark>' + medical_examination.speech_therapist + '</mark></u><br>\
                        Стоматолог: <u><mark>' + medical_examination.denta_surgeon + '</mark></u><br>\
                        Психолог: <u><mark>' + medical_examination.psychologist + '</mark></u><br>\
                        Другие врачи: <u><mark>' + medical_examination.other_doctors + '</mark></u><br>\
                        Анализ крови: <u><mark>' + medical_examination.blood_test + '</mark></u><br>\
                        Анализ мочи: <u><mark>' + medical_examination.urine_analysis + '</mark></u><br>\
                        Анализ кала: <u><mark>' + medical_examination.feces_analysis + '</mark></u><br>\
                        <strong>Заключительный диагноз: </strong><u><mark>' + medical_examination.general_diagnosis + '</mark></u><br>\
                        Оценка физического развития: <u><mark>' + medical_examination.physical_development + '</mark></u><br>\
                        Оценка нервно-психического развития: <u><mark>' + medical_examination.mental_development + '</mark></u><br>\
                        Группа здоровья: <u><mark>' + medical_examination.health_group + '</mark></u><br>\
                        Мед. гр. для занятий физкультурой: <u><mark>' + medical_examination.sport_group + '</mark></u><br>\
                        <strong>Медико-педагогическое заключение: </strong><u><mark>' + medical_examination.med_and_ped_conclusion + '</mark></u><br>\
                        Рекомендации: <u><mark>' + medical_examination.recommendations + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#medicalExaminationModal" name="update-medical-examination-' + medical_examination.period.replace(/ /g,'') + '-btn" onclick="update_medical_examination(\'' + medical_examination.period + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-medical-examination-' + medical_examination.period.replace(/ /g,'') + '-btn" onclick="delete_medical_examination(\'' + medical_examination.period + '\')">Удалить</button>\
                    </div>\
                </div>';
                    let medical_examination_div = document.querySelector('#medical-examination-main-div');
                    medical_examination_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                medical_examination["prev_period"] = medical_examination_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/medical_examinations/",
                    data: JSON.stringify(medical_examination),
                    contentType: "application/json",
                    dataType: 'json',
                    success: (medical_examination_data) => {
                        innerHTML = '<p><strong>Период обследования: </strong><u><mark>' + medical_examination.period  + '</mark></u> <br>\
                        Дата обследования: <u><mark>' + medical_examination.examination_date + '</mark></u> Возраст: <u><mark>' + medical_examination_data.age + '</mark></u><br>\
                        Длина тела, см: <u><mark>' + medical_examination.height + '</mark></u>, масса тела, кг: <u><mark>' + medical_examination.weight + '</mark></u><br>\
                        Жалобы: <u><mark>' + medical_examination.complaints + '</mark></u><br>\
                        Педиатр: <u><mark>' + medical_examination.pediatrician + '</mark></u><br>\
                        Ортопед: <u><mark>' + medical_examination.orthopaedist + '</mark></u><br>\
                        Офтальмолог: <u><mark>' + medical_examination.ophthalmologist + '</mark></u><br>\
                        Отоларинголог: <u><mark>' + medical_examination.otolaryngologist + '</mark></u><br>\
                        Дерматолог: <u><mark>' + medical_examination.dermatologist + '</mark></u><br>\
                        Невролог: <u><mark>' + medical_examination.neurologist + '</mark></u><br>\
                        Логопед: <u><mark>' + medical_examination.speech_therapist + '</mark></u><br>\
                        Стоматолог: <u><mark>' + medical_examination.denta_surgeon + '</mark></u><br>\
                        Психолог: <u><mark>' + medical_examination.psychologist + '</mark></u><br>\
                        Другие врачи: <u><mark>' + medical_examination.other_doctors + '</mark></u><br>\
                        Анализ крови: <u><mark>' + medical_examination.blood_test + '</mark></u><br>\
                        Анализ мочи: <u><mark>' + medical_examination.urine_analysis + '</mark></u><br>\
                        Анализ кала: <u><mark>' + medical_examination.feces_analysis + '</mark></u><br>\
                        <strong>Заключительный диагноз: </strong><u><mark>' + medical_examination.general_diagnosis + '</mark></u><br>\
                        Оценка физического развития: <u><mark>' + medical_examination.physical_development + '</mark></u><br>\
                        Оценка нервно-психического развития: <u><mark>' + medical_examination.mental_development + '</mark></u><br>\
                        Группа здоровья: <u><mark>' + medical_examination.health_group + '</mark></u><br>\
                        Мед. гр. для занятий физкультурой: <u><mark>' + medical_examination.sport_group + '</mark></u><br>\
                        <strong>Медико-педагогическое заключение: </strong><u><mark>' + medical_examination.med_and_ped_conclusion + '</mark></u><br>\
                        Рекомендации: <u><mark>' + medical_examination.recommendations + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#medicalExaminationModal" name="update-medical-examination-' + medical_examination.period.replace(/ /g,'') + '-btn" onclick="update_medical_examination(\'' + medical_examination.period + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-medical-examination-' + medical_examination.period.replace(/ /g,'') + '-btn" onclick="delete_medical_examination(\'' + medical_examination.period + '\')">Удалить</button>\
                    </div>';
                        let medical_examination_div = document.getElementsByName('div-medical-examination-' + medical_examination.prev_period.replace(/ /g,''))[0]
                        medical_examination_div.innerHTML = innerHTML;
                        medical_examination_div.setAttribute('name', 'div-medical-examination-' + medical_examination.period.replace(/ /g,'')) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* ONGOING MEDICAL SUPERVISION */
function ongoing_medical_supervision_add_set_info(){

    oms_modal_header.innerHTML = "Добавление сведений о проведении текущего медицинского обследования";
    oms_examination_date_modal_dtpk.value = "2023-01-01";
    oms_examination_data_modal_txt.value = "";
    oms_diagnosis_modal_txt.value = "";
    oms_prescription_modal_txt.value = "";
    oms_doctor_modal_inpt.value = "";
    oms_commit_modal_btn.value = 'add'; 
}

function update_ongoing_medical_supervision(examination_date){
    var oms = {
        "medcard_num": medcard_num,
        "examination_date": examination_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/ongoing_medical_supervisions/one",
        data: JSON.stringify(oms),
        contentType: "application/json",
        dataType: 'json',
        success: function(oms){
            oms_modal_header.innerHTML = "Редактирование сведений о текущем медицинском обследовании";
            oms_commit_modal_btn.value = 'update';
            oms_close_modal_btn.value = oms.examination_date;
            oms_examination_date_modal_dtpk.value = oms.examination_date;
            oms_examination_data_modal_txt.value = oms.examination_data;
            oms_diagnosis_modal_txt.value = oms.diagnosis;
            oms_prescription_modal_txt.value = oms.prescription;
            oms_doctor_modal_inpt.value = oms.doctor;
        }
    });    
}

function delete_ongoing_medical_supervision(examination_date){
    delete_modal_header.innerHTML = 'Удалить сведения о текущем медицинском обследовании';
    close_delete_modal_btn.value = examination_date;
    delete_commit_modal_btn.value = 'delete_oms';
}

oms_commit_modal_btn.addEventListener('click', () =>{    
    var oms = {
        "medcard_num": medcard_num,
        "examination_date": oms_examination_date_modal_dtpk.value,
        "examination_data": oms_examination_data_modal_txt.value,
        "diagnosis": oms_diagnosis_modal_txt.value,
        "prescription": oms_prescription_modal_txt.value,
        "doctor": oms_doctor_modal_inpt.value 
    };
    switch (oms_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/ongoing_medical_supervisions/",
                data: JSON.stringify(oms),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    innerHTML = '<div name="div-ongoing-medical-supervision-' + oms.examination_date + '" class="col-12 mb-3">\
                    <p>Дата: <u><mark>' + oms.examination_date + '</mark></u> <br>\
                        Данные осмотра: <u><mark>' + oms.examination_data + '</mark></u> <br>\
                        Диагноз: <u><mark>' + oms.diagnosis + '</mark></u><br>\
                        Назначения: <u><mark>' + oms.prescription + '</mark></u><br>\
                        Врач: <u><mark>' + oms.doctor + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#omsModal" name="update-ongoing-medical-supervision-' + oms.examination_date + '-btn" onclick="update_ongoing_medical_supervision(\'' + oms.examination_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-ongoing-medical-supervision-' + oms.examination_date + '-btn" onclick="delete_ongoing_medical_supervision(\'' + oms.examination_date + '\')">Удалить</button>\
                    </div>\
                </div>';
                    let oms_div = document.querySelector('#ongoing-medical-supervision-main-div');
                    oms_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                oms["prev_examination_date"] = oms_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/ongoing_medical_supervisions/",
                    data: JSON.stringify(oms),
                    contentType: "application/json",
                    dataType: 'json',
                    success: () => {
                        innerHTML = '<p>Дата: <u><mark>' + oms.examination_date + '</mark></u> <br>\
                        Данные осмотра: <u><mark>' + oms.examination_data + '</mark></u> <br>\
                        Диагноз: <u><mark>' + oms.diagnosis + '</mark></u><br>\
                        Назначения: <u><mark>' + oms.prescription + '</mark></u><br>\
                        Врач: <u><mark>' + oms.doctor + '</mark></u>\
                    </p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#omsModal" name="update-ongoing-medical-supervision-' + oms.examination_date + '-btn" onclick="update_ongoing_medical_supervision(\'' + oms.examination_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-ongoing-medical-supervision-' + oms.examination_date + '-btn" onclick="delete_ongoing_medical_supervision(\'' + oms.examination_date + '\')">Удалить</button>\
                    </div>';
                        let oms_div = document.getElementsByName('div-ongoing-medical-supervision-' + oms.prev_examination_date)[0]
                        oms_div.innerHTML = innerHTML;
                        oms_div.setAttribute('name', 'div-ongoing-medical-supervision-' + oms.examination_date) 
                    }
                });
                break;
    
        default:
            break;
    }
})


/* SCREENING */
function screening_add_set_info(){
    screening_modal_header.innerHTML = "Добавление скрининга";
    screening_height_modal_inpt.value = "";
    screening_weight_modal_inpt.value = "";
    screening_blood_pressures_modal_inpt.value = "";
    screening_sight_od_modal_inpt.value = "";
    screening_sight_os_modal_inpt.value = "";
    screening_dynammetry_left_modal_inpt.value = "";
    screening_dynammetry_right_modal_inpt.value = "";
    screening_kern_test_modal_inpt.value = "";
    screening_commit_modal_btn.value = 'add'; 
}

function update_screening(examination_date){
    var screening = {
        "medcard_num": medcard_num,
        "examination_date": examination_date
    }
    $.ajax({
        type: "POST",
        async: true,
        url: "/api/v1/children/" + medcard_num + "/screenings/one",
        data: JSON.stringify(screening),
        contentType: "application/json",
        dataType: 'json',
        success: function(screening){
            screening_modal_header.innerHTML = "Редактирование скрининга";
            screening_commit_modal_btn.value = 'update';
            screening_close_modal_btn.value = screening.examination_date;
            screening_examination_date_modal_dtpk.value = screening.examination_date;
            screening_questionnaire_test_modal_slct.value = screening.questionnaire_test;
            screening_height_modal_inpt.value = screening.height;
            screening_weight_modal_inpt.value = screening.weight;
            screening_physical_development_modal_slct.value = screening.physical_development;
            screening_blood_pressures_modal_inpt.value = screening.blood_pressures;
            screening_carriage_modal_slct.value = screening.carriage;
            screening_foot_condition_modal_slct.value = screening.foot_condition;
            screening_sight_od_modal_inpt.value = screening.sight_od;
            screening_sight_os_modal_inpt.value = screening.sight_os;
            screening_visual_acuity_modal_slct.value = screening.visual_acuity;
            screening_malinovsky_test_modal_slct.value = screening.malinovsky_test;
            screening_binocular_vision_modal_slct.value = screening.binocular_vision;
            screening_hearing_acuteness_modal_slct.value = screening.hearing_acuteness;
            screening_dynammetry_left_modal_inpt.value = screening.dynammetry_left;
            screening_dynammetry_right_modal_inpt.value = screening.dynammetry_right;
            screening_physical_fitness_modal_slct.value = screening.physical_fitness;
            screening_protein_in_urine_modal_slct.value = screening.protein_in_urine;
            screening_glucose_in_urine_modal_slct.value = screening.glucose_in_urine;
            screening_biological_age_modal_slct.value = screening.biological_age;
            screening_speech_defects_modal_chck.checked = screening.speech_defects;
            screening_kern_test_modal_inpt.value = screening.kern_test;
            screening_neurotic_disorders_modal_chck.checked = screening.neurotic_disorders;
            screening_thinking_and_speech_disorders_modal_chck.checked = screening.thinking_and_speech_disorders;
            screening_motor_development_disorders_modal_chck.checked = screening.motor_development_disorders;
            screening_attention_and_memory_disorders_modal_chck.checked = screening.attention_and_memory_disorders;
            screening_social_contacts_disorders_modal_chck.checked = screening.social_contacts_disorders;
        }
    });    
}

function delete_screening(age){
    delete_modal_header.innerHTML = 'Удалить скрининг';
    close_delete_modal_btn.value = age;
    delete_commit_modal_btn.value = 'delete_screening';
}

screening_commit_modal_btn.addEventListener('click', () =>{ 
    var screening = {
        "medcard_num": medcard_num,
        "examination_date": screening_examination_date_modal_dtpk.value,
        "questionnaire_test": screening_questionnaire_test_modal_slct.value,
        "height": screening_height_modal_inpt.value,
        "weight": screening_weight_modal_inpt.value,
        "physical_development": screening_physical_development_modal_slct.value || null,
        "blood_pressures": screening_blood_pressures_modal_inpt.value || null,
        "carriage": screening_carriage_modal_slct.value || null,
        "foot_condition": screening_foot_condition_modal_slct.value || null,
        "sight_od": screening_sight_od_modal_inpt.value || null,
        "sight_os": screening_sight_os_modal_inpt.value || null,
        "visual_acuity": screening_visual_acuity_modal_slct.value || null,
        "malinovsky_test": screening_malinovsky_test_modal_slct.value || null,
        "binocular_vision": screening_binocular_vision_modal_slct.value || null,
        "hearing_acuteness": screening_hearing_acuteness_modal_slct.value || null,
        "dynammetry_left": screening_dynammetry_left_modal_inpt.value || null,
        "dynammetry_right": screening_dynammetry_right_modal_inpt.value || null,
        "physical_fitness": screening_physical_fitness_modal_slct.value || null,
        "protein_in_urine": screening_protein_in_urine_modal_slct.value || null,
        "glucose_in_urine": screening_glucose_in_urine_modal_slct.value || null,
        "biological_age": screening_biological_age_modal_slct.value || null,
        "speech_defects": screening_speech_defects_modal_chck.checked,
        "kern_test": screening_kern_test_modal_inpt.value || null,
        "neurotic_disorders": screening_neurotic_disorders_modal_chck.checked,
        "thinking_and_speech_disorders": screening_thinking_and_speech_disorders_modal_chck.checked,
        "motor_development_disorders": screening_motor_development_disorders_modal_chck.checked,
        "attention_and_memory_disorders": screening_attention_and_memory_disorders_modal_chck.checked,
        "social_contacts_disorders": screening_social_contacts_disorders_modal_chck.checked,
        "diseases_for_year": null
    };
    switch (screening_commit_modal_btn.value) {
        case 'add':
            $.ajax({
                type: "POST",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/screenings/",
                data: JSON.stringify(screening),
                contentType: "application/json",
                dataType: 'json',
                success: (response) => {
                    innerHTML = '<div name="div-screening-' + screening.examination_date + '" class="col-12 mb-3">\
                    <p>Дата проведения: <u><mark>' + screening.examination_date + '</mark></u>, Возраст: <u><mark>' + response.age + '</mark></u>, Анкетный тест: <u><mark>' + screening.questionnaire_test + '</mark></u>, \
                        рост, см: <u><mark>' + screening.height + '</mark></u>, масса, кг: <u><mark>' + screening.weight + '</mark></u>, '
                        if (screening.physical_development){
                            innerHTML += 'Физическое развитие: <u><mark>' + screening.physical_development + '</mark></u>, '
                        }
                        if (screening.blood_pressures){
                            innerHTML += 'АД, мм.рт.ст.: <u><mark>' + screening.blood_pressures + '</mark></u>, '
                        }
                        if (screening.carriage){
                            innerHTML += 'Осанка: <u><mark>' + screening.carriage + '</mark></u>, '
                        }
                        if (screening.foot_condition){
                            innerHTML += 'Состояние стопы: <u><mark>' + screening.foot_condition + '</mark></u>, '
                        }
                        if (screening.sight_od){
                            innerHTML += 'Зрение, ОД: <u><mark>' + screening.sight_od + '</mark></u>, '
                        }
                        if (screening.sight_os){
                            innerHTML += 'Зрение, OS: <u><mark>' + screening.sight_os + '</mark></u>, '
                        }
                        if (screening.visual_acuity){
                            innerHTML += 'Острота зрения: <u><mark>' + screening.visual_acuity + '</mark></u>, '
                        }
                        if (screening.malinovsky_test){
                            innerHTML += 'Тест Малиновского: <u><mark>' + screening.malinovsky_test + '</mark></u>, '
                        }
                        if (screening.binocular_vision){
                            innerHTML += 'Бинокулярное зрение: <u><mark>' + screening.binocular_vision + '</mark></u>, '
                        }
                        if (screening.hearing_acuteness){
                            innerHTML += 'Острота слуха: <u><mark>' + screening.hearing_acuteness + '</mark></u>, '
                        }
                        if (screening.dynammetry_left){
                            innerHTML += 'Динамометрия (Правая рука): <u><mark>' + screening.dynammetry_left + '</mark></u>, '
                        }
                        if (screening.dynammetry_right){
                            innerHTML += 'Динамометрия (Левая рука): <u><mark>' + screening.dynammetry_right + '</mark></u>, '
                        }
                        if (screening.physical_fitness){
                            innerHTML += 'Физическая подготовленность: <u><mark>' + screening.physical_fitness + '</mark></u>, '
                        }
                        if (screening.protein_in_urine){
                            innerHTML += 'Определение белка в моче: <u><mark>' + screening.protein_in_urine + '</mark></u>, '
                        }
                        if (screening.glucose_in_urine){
                            innerHTML += 'Определение глюкозы в моче: <u><mark>' + screening.glucose_in_urine + '</mark></u>'
                        }
                        innerHTML += '<br>'
                        if (screening.biological_age ||  screening.speech_defects || screening.kern_test || screening.neurotic_disorders || screening.thinking_and_speech || screening.motor_development || screening.attention_and_memory || screening.social_contacts){
                            innerHTML += '<strong>Расширенная скрининг-программа</strong><br>'
                            if (screening.biological_age){
                                innerHTML += 'Биологический возраст: <u><mark>' + screening.biological_age + '</mark></u>, '
                            }
                            if (screening.kern_test){
                                innerHTML += 'Тест Керна-Иерасика: <u><mark>' + screening.kern_test + '</mark></u>, '
                            }
                            if (screening.speech_defects){
                                innerHTML += 'Дефекты речи: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.neurotic_disorders){
                                innerHTML += 'Выявление невротических расстройств:  <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.thinking_and_speech_disorders){
                                innerHTML += 'Мышление и речь: <u><mark>Отклонение</mark></u>,  '
                            }
                            if (screening.motor_development_disorders){
                                innerHTML += 'Моторное развитие: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.attention_and_memory_disorders){
                                innerHTML += 'Внимание и память: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.social_contacts_disorders){
                                innerHTML += 'Социальные контакты: <u><mark>Отклонение</mark></u>'
                            }
                        }
                        innerHTML += '<br>\
                        Заболеваний за год: <u><mark>' + response.diseases_for_year + '</mark></u>'
                    innerHTML += '</p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#screeningModal" name="update-screening-' + screening.examination_date + '-btn" onclick="update_screening(\'' + screening.examination_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-screening-' + screening.examination_date + '-btn" onclick="delete_screening(\'' + screening.examination_date + '\')">Удалить</button>\
                    </div>\
                </div>';
                    let screening_div = document.querySelector('#screening-main-div');
                    screening_div.innerHTML += innerHTML;
                }
            });
            break;

            case 'update':
                screening["prev_examination_date"] = screening_close_modal_btn.value;
                $.ajax({
                    type: "PUT",
                    async: true,
                    url: "/api/v1/children/" + medcard_num + "/screenings/",
                    data: JSON.stringify(screening),
                    contentType: "application/json",
                    dataType: 'json',
                    success: (response) => {
                        innerHTML = '<p>Дата проведения: <u><mark>' + screening.examination_date + '</mark></u>, Возраст: <u><mark>' + response.age + '</mark></u>, Анкетный тест: <u><mark>' + screening.questionnaire_test + '</mark></u>, \
                        рост, см: <u><mark>' + screening.height + '</mark></u>, масса, кг: <u><mark>' + screening.weight + '</mark></u>, '
                        if (screening.physical_development){
                            innerHTML += 'Физическое развитие: <u><mark>' + screening.physical_development + '</mark></u>, '
                        }
                        if (screening.blood_pressures){
                            innerHTML += 'АД, мм.рт.ст.: <u><mark>' + screening.blood_pressures + '</mark></u>, '
                        }
                        if (screening.carriage){
                            innerHTML += 'Осанка: <u><mark>' + screening.carriage + '</mark></u>, '
                        }
                        if (screening.foot_condition){
                            innerHTML += 'Состояние стопы: <u><mark>' + screening.foot_condition + '</mark></u>, '
                        }
                        if (screening.sight_od){
                            innerHTML += 'Зрение, ОД: <u><mark>' + screening.sight_od + '</mark></u>, '
                        }
                        if (screening.sight_os){
                            innerHTML += 'Зрение, OS: <u><mark>' + screening.sight_os + '</mark></u>, '
                        }
                        if (screening.visual_acuity){
                            innerHTML += 'Острота зрения: <u><mark>' + screening.visual_acuity + '</mark></u>, '
                        }
                        if (screening.malinovsky_test){
                            innerHTML += 'Тест Малиновского: <u><mark>' + screening.malinovsky_test + '</mark></u>, '
                        }
                        if (screening.binocular_vision){
                            innerHTML += 'Бинокулярное зрение: <u><mark>' + screening.binocular_vision + '</mark></u>, '
                        }
                        if (screening.hearing_acuteness){
                            innerHTML += 'Острота слуха: <u><mark>' + screening.hearing_acuteness + '</mark></u>, '
                        }
                        if (screening.dynammetry_left){
                            innerHTML += 'Динамометрия (Правая рука): <u><mark>' + screening.dynammetry_left + '</mark></u>, '
                        }
                        if (screening.dynammetry_right){
                            innerHTML += 'Динамометрия (Левая рука): <u><mark>' + screening.dynammetry_right + '</mark></u>, '
                        }
                        if (screening.physical_fitness){
                            innerHTML += 'Физическая подготовленность: <u><mark>' + screening.physical_fitness + '</mark></u>, '
                        }
                        if (screening.protein_in_urine){
                            innerHTML += 'Определение белка в моче: <u><mark>' + screening.protein_in_urine + '</mark></u>, '
                        }
                        if (screening.glucose_in_urine){
                            innerHTML += 'Определение глюкозы в моче: <u><mark>' + screening.glucose_in_urine + '</mark></u>'
                        }
                        innerHTML += '<br>'
                        if (screening.biological_age ||  screening.speech_defects || screening.kern_test || screening.neurotic_disorders || screening.thinking_and_speech || screening.motor_development || screening.attention_and_memory || screening.social_contacts){
                            innerHTML += '<strong>Расширенная скрининг-программа</strong><br>'
                            if (screening.biological_age){
                                innerHTML += 'Биологический возраст: <u><mark>' + screening.biological_age + '</mark></u>, '
                            }
                            if (screening.kern_test){
                                innerHTML += 'Тест Керна-Иерасика: <u><mark>' + screening.kern_test + '</mark></u>, '
                            }
                            if (screening.speech_defects){
                                innerHTML += 'Дефекты речи: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.neurotic_disorders){
                                innerHTML += 'Выявление невротических расстройств:  <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.thinking_and_speech_disorders){
                                innerHTML += 'Мышление и речь: <u><mark>Отклонение</mark></u>,  '
                            }
                            if (screening.motor_development_disorders){
                                innerHTML += 'Моторное развитие: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.attention_and_memory_disorders){
                                innerHTML += 'Внимание и память: <u><mark>Отклонение</mark></u>, '
                            }
                            if (screening.social_contacts_disorders){
                                innerHTML += 'Социальные контакты: <u><mark>Отклонение</mark></u>'
                            }
                        }
                        innerHTML += '<br>\
                        Заболеваний за год: <u><mark>' + response.diseases_for_year + '</mark></u>'
                    innerHTML += '</p>\
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">\
                        <button type="button" class="btn btn-outline-primary mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#screeningModal" name="update-screening-' + screening.examination_date + '-btn" onclick="update_screening(\'' + screening.examination_date + '\')">Редактировать</button>\
                        <button type="button" class="btn btn-outline-danger mt-2 btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" name="delete-screening-' + screening.examination_date + '-btn" onclick="delete_screening(\'' + screening.examination_date + '\')">Удалить</button>\
                    </div>';
                        let screening_div = document.getElementsByName('div-screening-' + screening.prev_examination_date)[0]
                        screening_div.innerHTML = innerHTML;
                        screening_div.setAttribute('name', 'div-screening-' + screening.examination_date) 
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
            var allergy = {
                "allergen": close_delete_modal_btn.value,
                "medcard_num": medcard_num
            };
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/allergyes/",
                data: JSON.stringify(allergy),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var allergy_div = document.getElementsByName('div-' + close_delete_modal_btn.value.replace(/ /g,''))[0];
                    allergy_div.remove();
                }
            });

            break;

        case 'delete_parent':
            const parent_type = {"parent_type": close_delete_modal_btn.value}
            console.log(parent_type);
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/parents/",
                data: JSON.stringify(parent_type),
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
            var extra_class_data = close_delete_modal_btn.value.split('///')
            var extra_class = {
                "medcard_num": medcard_num,
                "classes_type": extra_class_data[0],
                "age": extra_class_data[1]
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/extra_classes/",
                data: JSON.stringify(extra_class),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var extra_classes_div = document.getElementsByName('div-class-' + extra_class.classes_type.replace(/ /g,'') + '-' + extra_class.age)[0];
                    extra_classes_div.remove();
                }
            });
            
            break;

        case 'delete_past_illness':
            var past_illness_data = close_delete_modal_btn.value.split('///')
            var past_illness = {
                "medcard_num": medcard_num,
                "diagnosis": past_illness_data[0],
                "start_date": past_illness_data[1]
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/past_illnesses",
                data: JSON.stringify(past_illness),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var past_illness_div = document.getElementsByName('div-past-illness-' + past_illness.diagnosis.replace(/ /g,'') + '-' + past_illness.start_date)[0];
                    past_illness_div.remove();
                }
            });
            
            break;
        
        case 'delete_hospitalization':
            var hospitalization = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/hospitalizations",
                data: JSON.stringify(hospitalization),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var hospitalization_div = document.getElementsByName('div-hospitalization-' + hospitalization.start_date)[0];
                    hospitalization_div.remove();
                }
            });
            
            break;

        case 'delete_spa_treatment':
            var spa_treatment = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/spa_treatments",
                data: JSON.stringify(spa_treatment),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var spa_treatment_div = document.getElementsByName('div-spa-treatment-' + spa_treatment.start_date)[0];
                    spa_treatment_div.remove();
                }
            });
            
            break;        

        case 'delete_medical_certificate':
            var medical_certificate_data = close_delete_modal_btn.value.split('///')
            var medical_certificate = {
                "medcard_num": medcard_num,
                "disease": medical_certificate_data[0],
                "cert_date": medical_certificate_data[1]
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/medical_certificates",
                data: JSON.stringify(medical_certificate),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var medical_certificate_div = document.getElementsByName('div-medical-certificate-' + medical_certificate.disease.replace(/ /g,'') + '-' + medical_certificate.cert_date)[0];
                    medical_certificate_div.remove();
                }
            });
            
            break;

        case 'delete_dispensary':
            var dispensary = {
                "medcard_num": medcard_num,
                "start_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/dispensaryes",
                data: JSON.stringify(dispensary),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var dispensary_div = document.getElementsByName('div-dispensary-' + dispensary.start_date)[0];
                    dispensary_div.remove();
                }
            });
            
            break; 
        
        case 'delete_visit_specialist_control':
            var visit_specialist_control = {
                "medcard_num": medcard_num,
                "start_dispanser_date": visit_specialist_control_add_btn.value,
                "assigned_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/visit_specialist_controls",
                data: JSON.stringify(visit_specialist_control),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var visit_specialist_control_div = document.getElementsByName('div-visit-specialist-control-'+ visit_specialist_control.assigned_date)[0];
                    visit_specialist_control_div.remove();
                }
            });
            
            break;     
         
        case 'delete_deworming':
            var deworming = {
                "medcard_num": medcard_num,
                "deworming_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/dewormings",
                data: JSON.stringify(deworming),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var deworming_div = document.getElementsByName('div-deworming-' + deworming.deworming_date)[0];
                    deworming_div.remove();
                }
            });
            
            break;     
        
        case 'delete_oral_sanation':
            var oral_sanation = {
                "medcard_num": medcard_num,
                "sanation_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/oral_sanations",
                data: JSON.stringify(oral_sanation),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var oral_sanation_div = document.getElementsByName('div-oral-sanation-' + oral_sanation.sanation_date)[0];
                    oral_sanation_div.remove();
                }
            });
            
            break;

        case 'delete_prevaccination_checkup':
            var prevaccination_checkup = {
                "medcard_num": medcard_num,
                "examination_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/prevaccination_checkups",
                data: JSON.stringify(prevaccination_checkup),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var prevaccination_checkup_div = document.getElementsByName('div-prevaccination-checkup-' + prevaccination_checkup.examination_date)[0];
                    prevaccination_checkup_div.remove();
                }
            });
            
            break;
            
        case 'delete_prof_vaccination':
            var pk_data = close_delete_modal_btn.value.split('///');
            var prof_vaccination = {
                "medcard_num": medcard_num,
                "vac_name_id": pk_data[0],
                "vac_type": pk_data[1]
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/vaccinations",
                data: JSON.stringify(prof_vaccination),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var prof_vaccination_div = document.getElementsByName('div-prof-vaccination-' + prof_vaccination.vac_name_id + '-' + prof_vaccination.vac_type.replace(/ /g,''))[0];
                    prof_vaccination_div.remove();
                }
            });
            
            break;
            
        case 'delete_epid_vaccination':
            var pk_data = close_delete_modal_btn.value.split('///');
            var epid_vaccination = {
                "medcard_num": medcard_num,
                "vac_name_id": pk_data[0],
                "vac_type": pk_data[1]
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/vaccinations",
                data: JSON.stringify(epid_vaccination),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var epid_vaccination_div = document.getElementsByName('div-epid-vaccination-' + epid_vaccination.vac_name_id + '-' + epid_vaccination.vac_type.replace(/ /g,''))[0];
                    epid_vaccination_div.remove();
                }
            });
            
            break;

        case 'delete_gg_injection':
            var gg_injection = {
                "medcard_num": medcard_num,
                "vac_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/gg_injections",
                data: JSON.stringify(gg_injection),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var gg_injection_div = document.getElementsByName('div-gg-injection-' + gg_injection.vac_date)[0];
                    gg_injection_div.remove();
                }
            });
            
            break;

        case 'delete_mantoux_test':
            var mantoux_test = {
                "medcard_num": medcard_num,
                "check_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/mantoux_tests",
                data: JSON.stringify(mantoux_test),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var mantoux_test_div = document.getElementsByName('div-mantoux-test-' + mantoux_test.check_date)[0];
                    mantoux_test_div.remove();
                }
            });
            
            break;

        case 'delete_tub_vac':
            var tub_vac = {
                "medcard_num": medcard_num,
                "vac_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/tub_vacs",
                data: JSON.stringify(tub_vac),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var tub_vac_div = document.getElementsByName('div-tub-vac-' + tub_vac.vac_date)[0];
                    tub_vac_div.remove();
                }
            });
            
            break;

        case 'delete_medical_examination':
            var medical_examination = {
                "medcard_num": medcard_num,
                "period": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/medical_examinations",
                data: JSON.stringify(medical_examination),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var medical_examination_div = document.getElementsByName('div-medical-examination-' + medical_examination.period.replace(/ /g,''))[0];
                    medical_examination_div.remove();
                }
            });
            
            break;

         case 'delete_oms':
            var oms = {
                "medcard_num": medcard_num,
                "examination_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/ongoing_medical_supervisions",
                data: JSON.stringify(oms),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var oms_div = document.getElementsByName('div-ongoing-medical-supervision-' + oms.examination_date)[0];
                    oms_div.remove();
                }
            });
            
            break;

        case 'delete_screening':
            var screening = {
                "medcard_num": medcard_num,
                "examination_date": close_delete_modal_btn.value
            }
            $.ajax({
                type: "DELETE",
                async: true,
                url: "/api/v1/children/" + medcard_num + "/screenings",
                data: JSON.stringify(screening),
                contentType: "application/json",
                dataType: 'json',
                success: () => {
                    var screening_div = document.getElementsByName('div-screening-' + screening.examination_date)[0];
                    screening_div.remove();
                }
            });
            
            break;

        default:
            break;
    }
})


function deleteMedcard(medcard_num) {
    var confirmDeleteString = document.getElementById("confirmDeleteString").innerText;
    var confirmDeleteInput = document.getElementById("confirmDeleteInput").value;
    if (confirmDeleteString === confirmDeleteInput) {
        $.ajax({
            type: "DELETE",
            async: true,
            url: "/api/v1/children/" + medcard_num,
            data: null,
            contentType: "application/json",
            dataType: 'json',
            success: () => {
                alert('Медкарта была удалена');
                window.location.href = "/medical_record/all";
            },
            error: () => {
                alert('При удалении произошла ошибка')
            }
        }); 
    } else {
        alert(`Для удаления необходимо ввести в поле ввода текст: "${confirmDeleteString}"`)
    }
    
}
