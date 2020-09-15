#!/usr/bin/node
const process = require('process');
const x = Number(process.argv[2]);
const string = 'C is fun';
for (let i = 0; i < parseInt(x); i++) {
  console.log(string);
}
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
