#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const cha = JSON.parse(body).characters;
    for (let i = 0; i < cha.length; i++) {
      request.get(cha[i], function (err, response, body) {
        if (err) { console.log(err); } else { console.log(JSON.parse(body).name); }
      });
    }
  }
});
