#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const cha = JSON.parse(body).characters;
    const limit = cha.length;
    Characters(0, cha[0], cha, limit);
  }
});

function Characters (i, url, charList, limit) {
  if (i === limit) { return; }
  request.get(url, function (err, respinse, body) {
    if (err) { console.log(err); } else {
      console.log(JSON.parse(body).name);
      i++;
      Characters(i, charList[i], charList, limit);
    }
  });
}
