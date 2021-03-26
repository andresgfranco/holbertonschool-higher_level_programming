#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let length = list.length - 1; length !== -1; length--) {
    newList.push(list[length]);
  }
  return newList;
};
