function import_from_xlsx() {
  var formData = new FormData($("#uploadForm")[0]);

    $.ajax({
        url: "/api/v1/medical_record/import/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          alert('Медкарта добавлена')
          location.reload();
        },
        error: function(xhr, status, error) {
            console.error("Error importing file:", error);
        }
    });
}