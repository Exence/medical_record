const tub_record_close_modal_btn = document.querySelector('#tub-report-close-modal');
const tub_record_commit_modal_btn = document.querySelector('#tub-report-commit-modal');
const tub_record_start_date_modal_btn = document.querySelector('#tubReportStartDate-modal');
const tub_record_end_date_modal_btn = document.querySelector('#tubReportEndDate-modal');

tub_record_commit_modal_btn.addEventListener('click', () => {
    if (tub_record_start_date_modal_btn.value && tub_record_end_date_modal_btn.value){
        location.href='/reports/tuberculin/' + tub_record_start_date_modal_btn.value + '/' + tub_record_end_date_modal_btn.value
    }
})



const add_vac_report_btn = document.querySelector('#add-vac-report-btn')
const vac_record_commit_modal_btn = document.querySelector('#vac-report-commit-modal');

add_vac_report_btn.addEventListener('click', () => {
    $.ajax({
        type: "POST",
        async: true,
        url: "api/v1/vaccine/get_all",
        success: (data) => {
            let vac_name_modal_slct = document.querySelector('#vacReportVacName-modal');
            data.forEach(vac => {
                let vac_name = new Option(vac.name, vac.id);
                vac_name_modal_slct.append(vac_name);
            });
            
        }
    });
})
