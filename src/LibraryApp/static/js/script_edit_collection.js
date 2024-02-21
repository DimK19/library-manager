/* ON LOAD HIDE */
document.getElementById('editFormArea').style.display = 'none';

/* RENDER EDIT COLLECTION FORM */
document.getElementById('submitCollectionName').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('collectionSelect');
  if(input.value !== '')
  {
    let obj = JSON.parse(input.value.replaceAll('\'', '"'));
    document.getElementById('collectionName').value = obj.title;
    document.getElementById('collectionId').value = obj.id;
    document.getElementById('collectionType').value = obj.type_id;
    document.getElementById('editFormArea').style.display = 'block';
  }
}

/* SUBMIT EDIT REQUEST */
document.getElementById('submitEditCollection').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('collectionName');
  input.classList.remove('is-invalid');
  let isValid = 1;
  if(input.value.trim() === '') {
    input.classList.add('is-invalid');
    isValid = 0;
  }

  if(isValid === 1) {
    document.getElementById('editCollectionForm').submit();
  }
}
