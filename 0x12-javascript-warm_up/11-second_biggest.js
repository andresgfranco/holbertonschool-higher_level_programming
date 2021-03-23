#!/usr/bin/node

const args = process.argv;
let max = 0;
let secondMax = 0;

if (!args || args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) > max) {
      max = parseInt(args[i]);
    }
  }

  for (let j = 0; j < args.length; j++) {
    if (parseInt(args[j]) < max && parseInt(args[j]) > secondMax) {
      secondMax = parseInt(args[j]);
    }
  }
}
console.log(secondMax);
