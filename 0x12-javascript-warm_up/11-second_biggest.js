#!/usr/bin/node
const argss = process.argv;

if (argss.length === 2) {
  console.log(0);
} else if (argss.length === 3) {
  console.log(0);
} else {
    let maxi = Math.max.apply(null, argss.slice(2));
    const index = argss.indexOf(maxi.toString());
    argss.splice(index, 1);
    maxi = Math.max.apply(null, argss.slice(2));
    console.log(maxi);
}
