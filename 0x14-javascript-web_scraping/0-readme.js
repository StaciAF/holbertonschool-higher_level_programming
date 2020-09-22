#!/usr/bin/node
const process = require('process');
const fileName = process.argv[2];
const fs = require('fs');
fs.readFile(fileName, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
