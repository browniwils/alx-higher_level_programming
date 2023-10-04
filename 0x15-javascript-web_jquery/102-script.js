$(document).ready(function () {
  $('input#btn_translate').on('click', () => {
    const param = $('input#language_code').val();
    const resource = `https://hellosalut.stefanbohacek.dev/?lang=${param}`;
    $.get(resource, (res, status) => {
      $('div#hello').text(res.hello);
    });
  });
});
