const resource = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(resource, (res, status) => {
    $('#hello').text(res['hello']);
  });
});
