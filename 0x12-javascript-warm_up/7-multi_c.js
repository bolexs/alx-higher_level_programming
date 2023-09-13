#!/usr/bin/node
const argss = process.argv;
const numb = parseInt(argss[2]);
if (isNaN(numb)) {
    console.log('Missing number of occurrences');
    } else {
        while (numb > 0) {
            console.log('C is fun');
            numb--;
        }
    }
