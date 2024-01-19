/* ON LOAD HIDE */
document.getElementById('editFormArea').style.display = 'none';

/* RENDER EDIT AUTHOR FORM */
document.getElementById('submitAuthorName').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('authorSelect');
  if(input.value !== '')
  {
    let obj = JSON.parse(input.value.replaceAll('\'', '"'));
    if(obj.firstName !== 'NULL') {
      document.getElementById('authorFirstName').value = obj.firstName;
    }
    document.getElementById('authorLastName').value = obj.lastName;
    document.getElementById('authorId').value = obj.id;
    document.getElementById('editFormArea').style.display = 'block';
  }
}

/* SUBMIT EDIT REQUEST */
document.getElementById('submitEditAuthor').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('authorLastName');
  input.classList.remove('is-invalid');
  let isValid = 1;
  if(input.value.trim() === '') {
    input.classList.add('is-invalid');
    isValid = 0;
  }

  if(isValid === 1) {
    document.getElementById('editAuthorForm').submit();
  }
}
