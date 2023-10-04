const resource = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(resource, function (res, status) {
  const result = res.results;
  result.array.forEach((element) => {
    $('#list_movies').append(`<li>${element.title}</li>`);
    console.log(element.title);
  });
});
