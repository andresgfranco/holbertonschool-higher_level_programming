#!/usr/bin/node
const data = require('./100-data');
const array = data.list;

const newArray = array.map((currentElement, index) => {
  return currentElement * index;
});

console.log(array);
console.log(newArray);
