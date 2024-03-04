/* ON LOAD HIDE */
document.getElementById('editFormArea').style.display = 'none';
document.getElementById('editCol').style.display = 'none';

/* RENDER EDIT BOOK FORM */
document.getElementById('submitBookTitle').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('bookSelect');
  if(input.value !== '')
  {
    let obj = JSON.parse(input.value.replaceAll('€€', '"'));
    document.getElementById('bookTitle').value = obj.title;
    document.getElementById('bookId').value = obj.id;
    document.getElementById('publisherSelectUpd').value = obj.publisher_id;
    if(obj.edition !== 'None') {
      document.getElementById('editionUpd').value = obj.edition;
    }
    document.getElementById('editFormArea').style.display = 'block';
    document.getElementById('editCol').style.display = 'none';
    if(obj.col_title !== 'None') {
      if(obj.volume !== 'None') {
        document.getElementById('volumeUpd').value = obj.volume;
      }
      document.getElementById('colName').textContent = obj.col_title;
      document.getElementById('editCol').style.display = 'flex';
    }
  }
}

/* SUBMIT EDIT REQUEST */
document.getElementById('submitEditBook').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('bookTitle');
  input.classList.remove('is-invalid');
  let isValid = 1;
  if(input.value.trim() === '') {
    input.classList.add('is-invalid');
    isValid = 0;
  }

  if(isValid === 1) {
    document.getElementById('editBookForm').submit();
  }
}
