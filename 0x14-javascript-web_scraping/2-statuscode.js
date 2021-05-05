#!/usr/bin/node
/*
* Script that display the status code of a GET request
*/

const url = process.argv[2];
const request = require('request');

request(url, function (err, result, body) {
  console.log('code: ' + result.statusCode);
  if (err) {
    console.log(err);
  }
});
