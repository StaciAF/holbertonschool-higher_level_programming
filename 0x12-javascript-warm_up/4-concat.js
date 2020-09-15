#!/usr/bin/node
const process = require('process');
const first = process.argv[2];
const second = process.argv[3];
const res = first + ' is ' + second;
console.log(res);
