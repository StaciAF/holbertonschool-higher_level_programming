#!/usr/bin/node
const process = require('process');
const n = Number(process.argv[2]);
const ex = 'X';
let str = '';
if (isNaN(n)) {
  console.log('Missing size');
}
for (let i = 0; i < n; i++) {
  str += ex;
}
for (let i = 0; i < n; i++) {
  console.log(str);
}
