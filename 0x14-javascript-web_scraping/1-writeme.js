#!/usr/bin/node
/*
* Script that writes a string to a file
*/

const fs = require('fs');
const file = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(file, stringToWrite, function (err) {
  if (err) {
    console.log(err);
  }
});
