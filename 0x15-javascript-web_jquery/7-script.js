$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (ds) {
    const charName = ds.name;
    $('#character').text('Character Name: ' + charName);
  });
});
