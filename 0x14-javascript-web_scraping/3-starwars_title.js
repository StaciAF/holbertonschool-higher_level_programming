#!/usr/bin/node
const process = require('process');
const movId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
