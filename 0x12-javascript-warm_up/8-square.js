#!/usr/bin/node
const ocurrences = parseInt(process.argv[2]);
let i;
if (ocurrences === undefined || isNaN(ocurrences)) {
  console.log('Missing size');
} else {
  for (i = 0; i < ocurrences; i++) {
    console.log('X'.repeat(ocurrences));
  }
}
