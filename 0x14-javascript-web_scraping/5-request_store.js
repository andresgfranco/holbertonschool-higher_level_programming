#!/usr/bin/node
/*
* Script that gets the contents
* of a webpage and stores it in a file.
*/

const url = process.argv[2];
const request = require('request');

request(url, function (err, result, body) {
  if (err) {
    console.log(err);
  } else {
    const fs = require('fs');
    const filename = process.argv[3];
    fs.writeFile(filename, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
