#!/usr/bin/node
const request = require('request');
const settler = process.argv[2];

request(settler, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
