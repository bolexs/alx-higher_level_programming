#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const settler = process.argv[2];
const path = process.argv[3];

request(settler, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
