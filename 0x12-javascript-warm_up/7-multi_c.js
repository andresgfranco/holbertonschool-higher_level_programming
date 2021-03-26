#!/usr/bin/node
const ocurrences = parseInt(process.argv[2]);
let i;
if (ocurrences === undefined || isNaN(ocurrences)) {
  console.log('Missing number of ocurrences');
} else {
  for (i = 0; i < ocurrences; i++) {
    console.log('C is fun');
  }
}
