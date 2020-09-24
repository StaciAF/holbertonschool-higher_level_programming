$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, object) {
    $('#list_movies').append('<li>' + object.titles + '</li>');
  });
});
