#!/usr/bin/node
const argss = process.argv;
const numb = parseInt(argss[2]);
if (isNaN(numb)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < numb; index++) {
    console.log('X'.repeat(numb));
  }
}
