#!/usr/bin/node

const args = process.argv;

const isInt = parseInt(args[2], 10);

if (isNaN(isInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${isInt}`);
}
