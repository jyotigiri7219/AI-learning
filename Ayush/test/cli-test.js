#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: ayu <anything>');
    process.exit(1);
}

// Joins all arguments with a space
const input = args.join(' ');

console.log(`Hello from ${input}`);
