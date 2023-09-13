#!/usr/bin/node
const argss = process.argv;
const numb = parseInt(argss[2]);
if (isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numb}`);
}
