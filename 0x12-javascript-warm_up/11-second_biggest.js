#!/usr/bin/node

// Get all the arguments except the script name
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  // Convert the arguments to integers and sort them in descending order
  const num = args.map(Number).sort((a, b) => b - a);
  // Locate the second biggest integer (at index 1 after sorting )
  console.log(num[1]);
}
