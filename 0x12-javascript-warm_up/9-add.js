#!/usr/bin/node
const argss = process.argv;
const numb = parseInt(argss[2]);
const numbP = parseInt(argss[3]);

function add (numb, numbP) {
  return numb + numbP;
}
console.log(add(numb, numbP));
