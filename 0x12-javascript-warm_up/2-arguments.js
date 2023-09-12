#!/usr/bin/node
const argss = process.argv;
if (argss.length === 2) {
  console.log('No argument');
} else if (argss.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}