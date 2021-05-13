$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const titles = data.results;
  console.log(titles);

  for (let i = 0; i < titles.length; i++) {
    $('UL#list_movies').append('<li>' + titles[i].title + '</li>');
  }
});
