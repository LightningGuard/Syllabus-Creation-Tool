
   function generatePDF(){

    const element = document.getElementById("test");

    var opt = {
        margin:       0,
        filename:     'syllabus.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 3,scrollX: 0,scrollY: 0 },
        jsPDF:        { unit: 'in', format: 'a3', orientation: 'portrait' },
    };

    html2pdf().set(opt).from(element).save()

   }