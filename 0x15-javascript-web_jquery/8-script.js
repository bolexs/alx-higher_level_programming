$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (ds) {
    const films = ds.results;
    const listsOfFilms = $('#list_movies');

    $.each(films, function (index, film) {
      listsOfFilms.append('<li>' + film.title + '</li>');
    });
  });
});
