#!/usr/bin/node
/*
* Script that reads and prints the content of a file
*/

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'UTF-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
