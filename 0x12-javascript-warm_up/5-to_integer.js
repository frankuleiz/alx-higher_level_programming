#!/usr/bin/node

const args = parseInt(process.argv[2]);
if (args === undefined || isNaN(args)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args);
}
