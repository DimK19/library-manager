/* FOR AUTHOR */
var authorCount = 1;

document.getElementById('author-1-btn-existing').classList.add('library-btn-radio-active');
document.getElementById('author-1-form-new').style.display = 'none';
document.getElementById('authorSelect1').classList.add('required');
var authorOptionsHTML = document.getElementById('authorSelect1').innerHTML;
var publisherOptions = document.getElementById('publisherSelect').options;
// above returns an HTMLOptionsCollection, hence the use of the spread operator
// below to convert it to an Array. The shift() function removes and returns
// the first element, used to remove the default 'Αναζήτηση'
publisherOptions = [...publisherOptions].map(x => x.text);
publisherOptions.shift();

document.getElementById('author').onclick = function(e) {
  if(e.target.classList.contains('library-btn-radio-right')) {
    let authorId = e.target.id.split('-')[1];
    document.getElementById(`author-${authorId}-btn-existing`).classList.remove('library-btn-radio-active');
    document.getElementById(`author-${authorId}-btn-existing`).classList.add('library-btn-radio-inactive');
    document.getElementById(`author-${authorId}-btn-new`).classList.add('library-btn-radio-active');
    document.getElementById(`author-${authorId}-btn-new`).classList.remove('library-btn-radio-inactive');

    document.getElementById(`author-${authorId}-form-existing`).style.display = 'none';
    document.getElementById(`author-${authorId}-form-new`).style.display = 'block';

    // notice the use of == because authorId is a char
    if(authorId == 1) {
      document.getElementById('authorLastName1').classList.add('required');
      document.getElementById('authorSelect1').classList.remove('required');
    }
  }
  else if(e.target.classList.contains('library-btn-radio-left')) {
    let authorId = e.target.id.split('-')[1];
    document.getElementById(`author-${authorId}-btn-new`).classList.remove('library-btn-radio-active');
    document.getElementById(`author-${authorId}-btn-new`).classList.add('library-btn-radio-inactive');
    document.getElementById(`author-${authorId}-btn-existing`).classList.add('library-btn-radio-active');
    document.getElementById(`author-${authorId}-btn-existing`).classList.remove('library-btn-radio-inactive');

    document.getElementById(`author-${authorId}-form-new`).style.display = 'none';
    document.getElementById(`author-${authorId}-form-existing`).style.display = 'block';

    // notice the use of == because authorId is a char
    if(authorId == 1) {
      document.getElementById('authorLastName1').classList.remove('required');
      document.getElementById('authorSelect1').classList.add('required');
    }
  }
}

document.getElementById('btn-add-author').onclick = function() {
  authorCount++;
  let html = `
    <div id="author-${authorCount}">
      <div class="mb-3">
        <div class="container">
          <div class="row">
            <div id="author-${authorCount}-btn-existing" class="col library-btn-radio library-btn-radio-left">
              Επιλογή υπάρχοντος
            </div>
            <div id="author-${authorCount}-btn-new" class="col library-btn-radio library-btn-radio-right">
              Καταχώρηση νέου
            </div>
          </div>
        </div>
      </div>
      <div class="mb-3" id="author-${authorCount}-form-new">
        <div class="row">
          <div class="col-md-6 mb-3">
            <label for="authorFirstName${authorCount}">Όνομα</label>
            <input type="text" class="form-control" id="authorFirstName${authorCount}">
            <div class="invalid-feedback">
              Valid first name is required.
            </div>
          </div>
          <div class="col-md-6 mb-3">
            <label for="authorLastName${authorCount}">Επώνυμο</label>
            <input type="text" class="form-control" id="authorLastName${authorCount}">
            <div class="invalid-feedback">
              Valid last name is required.
            </div>
          </div>
        </div>
      </div>

      <div class="mb-3" id="author-${authorCount}-form-existing">
        <br>
        <select class="form-control form-select d-block w-100" name="authorSelect${authorCount}" id="authorSelect${authorCount}">
          ${authorOptionsHTML}
        </select>
        <br>
      </div>
    </div>
  `;
  document.getElementById('btn-add-author').insertAdjacentHTML('beforebegin', html);

  document.getElementById(`author-${authorCount}-btn-existing`).classList.add('library-btn-radio-active');
  document.getElementById(`author-${authorCount}-form-new`).style.display = 'none';
}
/* -------------------------------------------------------------------------- */

/* FOR PUBLISHER */
document.getElementById('publisher-btn-existing').classList.add('library-btn-radio-active');
document.getElementById('publisher-form-new').style.display = 'none';
document.getElementById('publisherSelect').classList.add('required');

document.getElementById('publisher-btn-new').onclick = function(e) {
  document.getElementById(`publisher-btn-existing`).classList.remove('library-btn-radio-active');
  document.getElementById(`publisher-btn-existing`).classList.add('library-btn-radio-inactive');
  document.getElementById(`publisher-btn-new`).classList.add('library-btn-radio-active');
  document.getElementById(`publisher-btn-new`).classList.remove('library-btn-radio-inactive');

  document.getElementById(`publisher-form-existing`).style.display = 'none';
  document.getElementById(`publisher-form-new`).style.display = 'block';

  document.getElementById('newPublisher').classList.add('required');
  document.getElementById('publisherSelect').classList.remove('required');
}

document.getElementById('publisher-btn-existing').onclick = function(e) {
  document.getElementById(`publisher-btn-new`).classList.remove('library-btn-radio-active');
  document.getElementById(`publisher-btn-new`).classList.add('library-btn-radio-inactive');
  document.getElementById(`publisher-btn-existing`).classList.add('library-btn-radio-active');
  document.getElementById(`publisher-btn-existing`).classList.remove('library-btn-radio-inactive');

  document.getElementById(`publisher-form-new`).style.display = 'none';
  document.getElementById(`publisher-form-existing`).style.display = 'block';

  document.getElementById('newPublisher').classList.remove('required');
  document.getElementById('publisherSelect').classList.add('required');
}
/* -------------------------------------------------------------------------- */

/* FOR SET */
document.getElementById('set-btn-existing').classList.add('library-btn-radio-active');
document.getElementById(`set-form-new`).style.display = 'none';
document.getElementById('set-form-global').style.display = 'none';

document.getElementById('setYes').onclick = function(e) {
  document.getElementById('set-form-global').style.display = 'block';
  document.getElementById(`setType`).classList.remove('required');
  document.getElementById(`setName`).classList.remove('required');
  document.getElementById(`setSelect`).classList.add('required');
}

document.getElementById('setNo').onclick = function(e) {
  document.getElementById('set-form-global').style.display = 'none';
  document.getElementById(`setType`).classList.remove('required');
  document.getElementById(`setName`).classList.remove('required');
  document.getElementById(`setSelect`).classList.remove('required');
}

document.getElementById('set-btn-new').onclick = function(e) {
  document.getElementById(`set-btn-existing`).classList.remove('library-btn-radio-active');
  document.getElementById(`set-btn-existing`).classList.add('library-btn-radio-inactive');
  document.getElementById(`set-btn-new`).classList.add('library-btn-radio-active');
  document.getElementById(`set-btn-new`).classList.remove('library-btn-radio-inactive');

  document.getElementById(`set-form-existing`).style.display = 'none';
  document.getElementById(`set-form-new`).style.display = 'block';

  document.getElementById(`setType`).classList.add('required');
  document.getElementById(`setName`).classList.add('required');
  document.getElementById(`setSelect`).classList.remove('required');
}

document.getElementById('set-btn-existing').onclick = function(e) {
  document.getElementById(`set-btn-new`).classList.remove('library-btn-radio-active');
  document.getElementById(`set-btn-new`).classList.add('library-btn-radio-inactive');
  document.getElementById(`set-btn-existing`).classList.add('library-btn-radio-active');
  document.getElementById(`set-btn-existing`).classList.remove('library-btn-radio-inactive');

  document.getElementById(`set-form-new`).style.display = 'none';
  document.getElementById(`set-form-existing`).style.display = 'block';

  document.getElementById(`setType`).classList.remove('required');
  document.getElementById(`setName`).classList.remove('required');
  document.getElementById(`setSelect`).classList.add('required');
}

/* SUBMIT - VALIDATION - QUERIES */
document.getElementById('insertButton').onclick = (e) => {
  e.preventDefault();
  let reqs = document.getElementsByClassName('required');

  let isValid = 1;
  for(let r of reqs) {
    r.classList.remove('is-invalid');
    if(r.value.trim() === '') {
      console.log(`Empty ${r.tagName}`);
      r.classList.add('is-invalid');
      isValid = 0;
    }
  }

  if(isValid === 1) {
    // console.log('valid submission');
    // request Object
    let ro = {};

    /* TITLE */
    let title = document.getElementById('title').value;
    Object.assign(ro, {'title': title});

    /* AUTHOR OR AUTHORS */
    let as = [];
    for(let i = 1; i <= authorCount; i++) {
      if(document.getElementById(`author-${i}-form-existing`).style.display === 'none') {
        let authorFirstName = document.getElementById(`authorFirstName${i}`).value;
        let authorLastName = document.getElementById(`authorLastName${i}`).value;
        if(authorFirstName == '') {
          authorFirstName = null;
        }
        as.push({
          'firstName': authorFirstName,
          'lastName': authorLastName
        });
      }
      else {
        let authorId = document.getElementById(`authorSelect${i}`).value;
        as.push({'id': authorId});
      }
    }
    Object.assign(ro, {'authors': as});

    /* PUBLISHER AND EDITION*/
    if(document.getElementById('publisher-form-existing').style.display === 'none') {
      let newPublisherName = document.getElementById('newPublisher').value;
      // If new publisher, check that there is not one with the same name
      if(publisherOptions.includes(newPublisherName)) {
        let confirmMessage = `Υπάρχει ήδη καταχωρημένος εκδότης με το όνομα «${newPublisherName}». Να γίνει καταχώρηση εκδότη με ίδιο όνομα;`
        if(!confirm(confirmMessage)) {
          return;
        }
      }
      let edition = document.getElementById('editionNew').value;
      if(edition == '') {
        edition = null
      }
      else {
        edition = parseInt(edition);
      }
      Object.assign(ro, {'publisher': {'newPublisherName': newPublisherName}});
      Object.assign(ro, {'edition': edition});
    }
    else {
      let publisherId = document.getElementById('publisherSelect').value;
      let edition = parseInt(document.getElementById('editionExisting').value);
      if(edition == '') {
        edition = null
      }
      else {
        edition = parseInt(edition);
      }
      Object.assign(ro, {'publisher': {'id': publisherId}});
      Object.assign(ro, {'edition': edition});
    }

    /* LOCATION */
    let loc = document.getElementById('location').value;
    Object.assign(ro, {'location': loc});

    /* SET */
    if(document.getElementById('setYes').checked) {
      if(document.getElementById('set-form-existing').style.display === 'none') {
        let setType = document.getElementById('setType').value;
        let setName = document.getElementById('setName').value;
        let volume = document.getElementById('volumeNew').value;
        if(volume == '') {
          volume = null;
        }
        else {
          volume = parseInt(volume)
        }
        Object.assign(ro, {'set': {
          'setType': setType,
          'setName': setName,
          'volume': volume
        }});
      }
      else {
        let setId = document.getElementById('setSelect').value;
        let volume = document.getElementById('volumeExisting').value;
        if(volume == '') {
          volume = null;
        }
        else {
          volume = parseInt(volume)
        }
        Object.assign(ro, {'set': {
          'id': setId,
          'volume': volume
        }});
      }
    }

    fetch(new URL('http://127.0.0.1:8009/book/record'), {
      method: 'POST',
      headers: new Headers({'Content-Type': 'application/json'}),
      body: JSON.stringify(ro)
    })
    .then(response => {location.reload()});
  }
}
