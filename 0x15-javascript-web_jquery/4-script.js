$(document).ready(function () {
  $('#toggle_header').click(function () {
    const head = $('header');
    if (head.hasClass('red')) {
      head.removeClass('red').addClass('green');
    } else if (head.hasClass('green')) {
      head.removeClass('green').addClass('red');
    }
  });
});
