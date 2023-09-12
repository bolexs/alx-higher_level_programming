#!/usr/bin/node
exports.esrever = function (list) {
  const newListing = [];
  for (let index = list.length - 1; index >= 0; index--) {
    newListing.push(list[index]);
  }
  return newListing;
};
