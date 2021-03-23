#!/usr/bin/node
if (!process.argv[2]) {
  console.log('No argument');
} else {
  const arg = process.argv[2];
  console.log(arg);
}
