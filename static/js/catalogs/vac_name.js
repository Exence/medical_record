window.addEventListener('load', (event) => {
  document.cookie = 'err=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/catalogs/vac_names;';
  document.cookie = 'msg=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/catalogs/vac_names;';
});

function errorWithDetailText(xhr, error) {
const detail = JSON.parse(xhr.responseText).detail;
if (detail) {
  error += ` (${detail})`
}
return error
}

function editVacName(id, name, vac_type) {
$('#vacNameId').val(id);
$('#vacNameInput').val(name);
$('#vacType').val(vac_type);
$('#commitModal').click(
  function(e) {
    e.preventDefault();
    var id = $('#vacNameId').val();
    var name = $('#vacNameInput').val();
    var vac_type = $('#vacType').val();
    $.ajax({
        url: '/api/v1/catalogs/vac_names/',
        method: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify({ id: id, name: name, vac_type: vac_type }),
        success: function() {
          document.cookie = `msg=${encodeURIComponent(`Наименование прививки успешно обновлено`)}`;
          window.location.href = "/catalogs/vac_names";
        },
        error: function(xhr, status, error) {
          const detailErr = errorWithDetailText(xhr,error);
          document.cookie = `err=${encodeURIComponent(`При попытке обновления записи сервер вернул ошибку: ${detailErr}`)}`;
          window.location.href = "/catalogs/vac_names";
        } 
    });
  }
)
}

function addVacName() {
$('#vacNameInput').val('');
$('#commitModal').click(
  function(e) {
    e.preventDefault();
    var name = $('#vacNameInput').val();
    var vac_type = $('#vacType').val();
    $.ajax({
        url: '/api/v1/catalogs/vac_names/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ name: name, vac_type: vac_type }),
        success: function() {
          document.cookie = `msg=${encodeURIComponent(`Наименование прививки успешно добавлено`)}`;
          window.location.href = "/catalogs/vac_names";
        },
        error: function(xhr, status, error) {
          const detailErr = errorWithDetailText(xhr,error);
          document.cookie = `err=${encodeURIComponent(`При попытке добавления записи сервер вернул ошибку: ${detailErr}`)}`;
          window.location.href = "/catalogs/vac_names";
        } 
    });
  }
)
}

function deleteVacName(id, name) {
$('#deleteVacNameId').val(id);
$('#deleteModalText').html(`Удалить прививку: "${name}"?`);
$('#deleteModalCommit').click(function() {
  var id = $('#deleteVacNameId').val();
  $.ajax({
    url: '/api/v1/catalogs/vac_names/',
    method: 'DELETE',
    contentType: 'application/json',
    data: JSON.stringify({ id: id }),
    success: function() {
      document.cookie = `msg=${encodeURIComponent(`Наименование прививки удалено`)}`;
      window.location.href = "/catalogs/vac_names";
    },
    error: function(xhr, status, error) {
      const detailErr = errorWithDetailText(xhr,error);
      document.cookie = `err=${encodeURIComponent(`При попытке удаления записи сервер вернул ошибку: ${detailErr}`)}`;
      window.location.href = "/catalogs/vac_names";
    }
});
});
}
