#!/usr/bin/node
const process = require('process');
const request = require('request');
const movId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movId;
request(url, 'utf-8', function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const mList = JSON.parse(body);
    console.log(mList.characters);
  }
});
