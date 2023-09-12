#!/usr/bin/node
exports.converter = function (base) {
  return function (numbs) {
    return numbs.toString(base);
  };
};
