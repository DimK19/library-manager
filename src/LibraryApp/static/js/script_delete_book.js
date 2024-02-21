// listening for clicks on entire table
document.getElementById('table').onclick = (e) => {
  // if click was on a button
  // (technically the click registers on the span inside it)
  if(e.target.id.split('-')[0] == 'delete') {
    // find nearest form
    let f = e.target.parentNode.parentNode;
    // find title
    let td = f.parentNode;
    let tr = td.parentNode;
    let title = tr.firstElementChild.textContent;
    if(confirm(`Οριστική διαγραφή του βιβλίου με τίτλο «${title}»;`)) {
      f.submit();
    }
  }
}
