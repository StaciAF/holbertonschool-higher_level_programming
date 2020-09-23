#!/usr/bin/node
const process = require ('process');
const request = require ('request');
const url = process.argv[2];
let count = 0;
request(url, 'utf-8', function (err, resp, body) {
    if (err) {
	console.log(err);
    } else {
	const toDos = JSON.parse(body);
	const userId = toDos.userId;
	const tskDone = () => ({completed: true}) 
	for (let i = 0; i < toDos.length; i++) {
	    console.log(toDos[i]);
	    }
	console.log(userId);
	console.log(count);
    }
});
