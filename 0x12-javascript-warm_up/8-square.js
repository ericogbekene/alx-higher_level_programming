#!/usr/bin/node
const args = process.argv.slice(2);
const count = parseInt(args[0]);

if (isNaN(count)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < count) {
    console.log('X'.repeat(count));
    i = i + 1;
  }
}
