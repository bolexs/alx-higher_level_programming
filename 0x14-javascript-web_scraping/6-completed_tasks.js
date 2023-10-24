#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const tasksToDo = {};
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (tasksToDo[task.userId] === undefined) {
          tasksToDo[task.userId] = 1;
        } else {
          tasksToDo[task.userId]++;
        }
      }
    }
    console.log(tasksToDo);
  }
});
