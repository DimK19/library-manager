// listening for clicks on entire table
document.getElementById('table').onclick = (e) => {
  // if click was on a button
  // the click may register on children element
  if(e.target.id.split('-')[0] == 'delete') {
    // find nearest form
    let f = e.target;
    // if click registered on button
    if(f.tagName.toLowerCase() == 'button') {
      f = f.parentNode;
    }
    // old tags are capital by convention
    else if(f.tagName.toLowerCase() == 'span') {
      f = f.parentNode.parentNode;
    }
    else if(f.tagName.toLowerCase() == 'svg') {
      f = f.parentNode.parentNode.parentNode;
    }
    else if(f.tagName.toLowerCase() == 'path') {
      f = f.parentNode.parentNode.parentNode.parentNode;
    }

    // find title
    let td = f.parentNode;
    let tr = td.parentNode;
    let firstTd = tr.firstElementChild;
    if(firstTd.childElementCount == 2) {
      var title = firstTd.children[1].textContent.trim();
    }
    else {
      var title = firstTd.firstElementChild.textContent.trim();
    }
    if(confirm(`Οριστική διαγραφή του βιβλίου με τίτλο «${title}»;`)) {
      f.submit();
    }
  }
}
