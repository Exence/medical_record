window.addEventListener('load', (event) => {
    document.cookie = 'err=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/catalogs/clinics;';
    document.cookie = 'msg=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/catalogs/clinics;';
});

function errorWithDetailText(xhr, error) {
  const detail = JSON.parse(xhr.responseText).detail;
  if (detail) {
    error += ` (${detail})`
  }
  return error
}

function editClinic(id, name) {
  $('#clinicId').val(id);
  $('#clinicName').val(name);
  $('#commitModal').click(
    function(e) {
      e.preventDefault();
      var id = $('#clinicId').val();
      var name = $('#clinicName').val();
      $.ajax({
          url: '/api/v1/catalogs/clinics/',
          method: 'PUT',
          contentType: 'application/json',
          data: JSON.stringify({ id: id, name: name }),
          success: function() {
            document.cookie = `msg=${encodeURIComponent(`Поликлиника успешно обновлена`)}`;
            window.location.href = "/catalogs/clinics";
          },
          error: function(xhr, status, error) {
            const detailErr = errorWithDetailText(xhr,error);
            document.cookie = `err=${encodeURIComponent(`При попытке обновления записи сервер вернул ошибку: ${detailErr}`)}`;
            window.location.href = "/catalogs/clinics";
          } 
      });
    }
  )
}

function addClinic() {
  $('#clinicName').val('');
  $('#commitModal').click(
    function(e) {
      e.preventDefault();
      var name = $('#clinicName').val();
      $.ajax({
          url: '/api/v1/catalogs/clinics/',
          method: 'POST',
          contentType: 'application/json',
          data: JSON.stringify({ name: name }),
          success: function() {
            document.cookie = `msg=${encodeURIComponent(`Поликлиника успешно добавлена`)}`;
            window.location.href = "/catalogs/clinics";
          },
          error: function(xhr, status, error) {
            const detailErr = errorWithDetailText(xhr,error);
            document.cookie = `err=${encodeURIComponent(`При попытке добавления записи сервер вернул ошибку: ${detailErr}`)}`;
            window.location.href = "/catalogs/clinics";
          } 
      });
    }
  )
}

function deleteClinic(id, name) {
  $('#deleteClinicId').val(id);
  $('#deleteModalText').html(`Удалить сведения о "${name}"?`);
  $('#deleteModalCommit').click(function() {
    var id = $('#deleteClinicId').val();
    $.ajax({
      url: '/api/v1/catalogs/clinics/',
      method: 'DELETE',
      contentType: 'application/json',
      data: JSON.stringify({ id: id }),
      success: function() {
        document.cookie = `msg=${encodeURIComponent(`Поликлиника удалена`)}`;
        window.location.href = "/catalogs/clinics";
      },
      error: function(xhr, status, error) {
        const detailErr = errorWithDetailText(xhr,error);
        document.cookie = `err=${encodeURIComponent(`При попытке удаления записи сервер вернул ошибку: ${detailErr}`)}`;
        window.location.href = "/catalogs/clinics";
      }
  });
  });
}
