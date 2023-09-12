#!/usr/bin/node
const argss = process.argv;
if (argss[2]) {
  console.log(argss[2]);
} else {
  console.log('No argument');
}
