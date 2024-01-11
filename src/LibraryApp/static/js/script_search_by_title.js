/* SEARCH BOOK BY TITLE */
document.getElementById('submitByTitle').onclick = (e) => {
  e.preventDefault();
  let input = document.getElementById('searchTitle');
  input.classList.remove('is-invalid');
  let isValid = 1;
  if(input.value.trim() === '') {
    input.classList.add('is-invalid');
    isValid = 0;
  }

  if(isValid === 1) {
    document.getElementById('searchForm').submit();
  }
}
