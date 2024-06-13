function export_to_xlsx() {
  const url = "/api/v1/children/" + medcard_num + "/xlsx";
  const a = document.createElement("a");
  a.href = url;
  a.download = "data.xlsx";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function export_to_pdf(fileName) {
  const { jsPDF } = window.jspdf;

  const content = document.getElementById('content');

  // Скрываем кнопки
  const allButtons = content.querySelectorAll('.btn')
  allButtons.forEach(button => {
    button.style.display = 'none';
  });

  // Сохраняем текущее состояние аккордиона, а затем расскрываем
  const accordionItems = document.querySelectorAll('.accordion-item');

  const accordionItemsInitialState = [];
  accordionItems.forEach((item, index) => {
    const buttonElement = item.querySelector('.accordion-button');
    const collapseElement = item.querySelector('.accordion-collapse');
    const isCollapsed = collapseElement.classList.contains('show');
    accordionItemsInitialState[index] = isCollapsed; 
    collapseElement.classList.add('show');
    buttonElement.classList.remove('collapsed');
  });

  $('#dellete-accordion-item').hide();

  const pdf = new jsPDF('p', 'pt', 'a4');
  const pdfWidth = pdf.internal.pageSize.getWidth();
  const pdfHeight = pdf.internal.pageSize.getHeight();

  html2canvas(content).then((canvas) => {
      const imgData = canvas.toDataURL('image/jpeg', 1.0);
      const imgWidth = pdfWidth;
      const imgHeight = canvas.height * pdfWidth / canvas.width;

      let heightLeft = imgHeight;
      let position = 0;

      pdf.addImage(imgData, 'JPEG', 0, position, imgWidth, imgHeight);
      heightLeft -= pdfHeight;

      while (heightLeft >= 0) {
          position = heightLeft - imgHeight;
          pdf.addPage();
          pdf.addImage(imgData, 'JPEG', 0, position, imgWidth, imgHeight);
          heightLeft -= pdfHeight;
      }

      pdf.save(fileName);
  });

  // Возвращаем кнопки и аккордион в начальное состояние
  allButtons.forEach(button => {
    button.style.display = 'inline-block';
  });
  accordionItems.forEach((item, index) => {
    const buttonElement = item.querySelector('.accordion-button');
    const collapseElement = item.querySelector('.accordion-collapse');
    const initialState = accordionItemsInitialState[index];

    if (initialState) {
        collapseElement.classList.add('show');
        buttonElement.classList.remove('collapsed');
    } else {
        collapseElement.classList.remove('show');
        buttonElement.classList.add('collapsed');
    }
  });
  $('#dellete-accordion-item').show();
}
