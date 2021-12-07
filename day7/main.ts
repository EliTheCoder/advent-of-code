import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const numbers = text
	.split(",")
	.map(n => parseInt(n))
	.sort((a, b) => a - b);

const sum = numbers.reduce((a, b) => a + b);

const best = numbers[Math.round(numbers.length / 2)];
const best2 = Math.floor(sum / numbers.length);
const fuel = numbers.map(n => Math.abs(n - best)).reduce((a, b) => a + b);
const fuel2 = numbers
	.map(n => (Math.abs(n - best2) + 1) * (Math.abs(n - best2) / 2))
	.reduce((a, b) => a + b);

console.log("Part 1:", fuel);
console.log("Part 2:", fuel2);
