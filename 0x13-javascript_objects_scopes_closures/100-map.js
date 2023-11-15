#!/usr/bin/node

const newArray = require('./100-data').list;

console.log(newArray);
console.log(newArray.map((value, index) => value * index));
