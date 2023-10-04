const resource = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(resource, (res, status) => {
  $('#character').text(res.name);
});
