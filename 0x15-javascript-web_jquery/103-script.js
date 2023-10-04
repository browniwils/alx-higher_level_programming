$(document).ready(function () {
  const param = $('input#language_code').val();
  const resource = `https://hellosalut.stefanbohacek.dev/?lang=${param}`;
  $('input#btn_translate').on('click', (event) => {
    translate(resource, event);
  });
  $('input#btn_translate').on('keypress', (event) => {
    translate(resource, event);
  });
});

function translate(url, event) {
  if (event.type === 'click' || (event.type === 'keypress' && event.keyCode === 13)) {
    $.get(url, (res, status) => {
      $('div#hello').text(res.hello);
    });
  }
}
