#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

const arg1 = parseInt(args[0]);
const arg2 = parseInt(args[1]);

if (args[0] && args[1]) {
  console.log(add(arg1, arg2));
} else {
  console.log('NaN');
}
