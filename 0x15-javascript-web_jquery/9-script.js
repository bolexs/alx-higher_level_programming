$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (ds) {
    $('#hello').text('Translation of "hello":' + ds.hello);
  });
});
