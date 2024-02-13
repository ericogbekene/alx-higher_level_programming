#!/usr/bin/node

function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const args = process.argv.slice(2);

const argument1 = parseInt(args[0]);

if (isNaN(argument1)) {
  console.log('1'); // Exit with code 1 if the first argument is not a number
} else {
  console.log(factorial(argument1));
}
