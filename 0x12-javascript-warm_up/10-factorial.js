#!/usr/bin/node
const argss = process.argv;
const num = argss[2];
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
