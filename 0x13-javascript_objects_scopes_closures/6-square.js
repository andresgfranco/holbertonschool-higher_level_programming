#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    let character;
    if (c === undefined) {
      character = 'X';
    } else {
      character = c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
