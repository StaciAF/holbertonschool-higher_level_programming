#!/usr/bin/node
const process = require('process');
const fctrl = Number(process.argv[2]);
function factorial (fctrl) {
  if (isNaN(fctrl)) {
    return (1);
  }
  if (fctrl === 0) {
    return (1);
  }
  return (fctrl * factorial(fctrl - 1));
}
console.log(factorial(fctrl));
