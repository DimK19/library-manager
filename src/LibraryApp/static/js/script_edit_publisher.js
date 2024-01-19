/* ON LOAD HIDE */
document.getElementById('editFormArea').style.display = 'none';

/* RENDER EDIT PUBLISHER FORM */
document.getElementById('submitPublisherName').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('publisherSelect');
  if(input.value !== '')
  {
    let obj = JSON.parse(input.value.replaceAll('\'', '"'));
    document.getElementById('publisherName').value = obj.name;
    document.getElementById('publisherId').value = obj.id;
    document.getElementById('editFormArea').style.display = 'block';
  }
}

/* SUBMIT EDIT REQUEST */
document.getElementById('submitEditPublisher').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('publisherName');
  input.classList.remove('is-invalid');
  let isValid = 1;
  if(input.value.trim() === '') {
    input.classList.add('is-invalid');
    isValid = 0;
  }

  if(isValid === 1) {
    document.getElementById('editPublisherForm').submit();
  }
}
