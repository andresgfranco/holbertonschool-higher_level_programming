#!/usr/bin/node
const int1 = parseInt(process.argv[2]);
const int2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(int1, int2));
