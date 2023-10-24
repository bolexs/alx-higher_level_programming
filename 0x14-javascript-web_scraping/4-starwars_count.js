#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    let counter = 0;
    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
