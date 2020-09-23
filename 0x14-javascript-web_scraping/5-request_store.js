#!/usr/bin/node
const process = require('process');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
