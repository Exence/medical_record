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

function fillVacNames() {
    $.get('/api/v1/catalogs/vac_names', (data) => {
        $('#vacReportVacName-modal').empty();
        for (const vacType in data) {
            for (const vacId in data[vacType]) {
                const vacName = data[vacType][vacId];
                $('#vacReportVacName-modal').append($('<option>', {
                    value: vacId,
                    text: vacName
                }));
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    fillVacNames();
});

