$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const text = `${data.name}`;
  $('#character').html(text);
});
