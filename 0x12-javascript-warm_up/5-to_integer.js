#!/usr/bin/node
const argInt = parseInt(process.argv[2]);
if (isNaN(argInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argInt}`);
}
