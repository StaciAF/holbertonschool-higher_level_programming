#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  while (list.length) {
    newList.push(list.pop());
  }
  return newList;
// for (let i = -1; i < list.length; i--) {
//    newList.push(list[i]);
};
