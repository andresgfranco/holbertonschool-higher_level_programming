#!/usr/bin/node

const integer = parseInt(process.argv[2]);

function recursion (integer) {
  if (integer === 1) {
    return 1;
  } else {
    return integer * recursion(integer - 1);
  }
}

if (isNaN(integer)) {
  console.log(1);
} else {
  console.log(recursion(integer));
}
