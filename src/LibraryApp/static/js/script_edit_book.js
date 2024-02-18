/* ON LOAD HIDE */
document.getElementById('editFormArea').style.display = 'none';

/* RENDER EDIT BOOK FORM */
document.getElementById('submitBookTitle').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('bookSelect');
  if(input.value !== '')
  {
    let obj = JSON.parse(input.value.replaceAll('€€', '"'));
    document.getElementById('bookTitle').value = obj.title;
    document.getElementById('bookId').value = obj.id;
    document.getElementById('editFormArea').style.display = 'block';
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
