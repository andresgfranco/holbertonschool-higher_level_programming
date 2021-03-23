#!/usr/bin/node
const args = process.argv;

let max = 0;
let secondMax = 0;
let i, j;

if (!args || args.lenght <= 1) {
  console.log(0);
} else {
  for (i = 0; i < args.lenght; i++) {
    if (parseInt(args[i]) > max) {
      max = parseInt(args[i]);
    }
  }

  for (j = 0; j < args.lenght; j++) {
    if (parseInt(args[j]) < max && parseInt(args[j]) > secondMax) {
      secondMax = parseInt(args[j]);
    }
  }
}
