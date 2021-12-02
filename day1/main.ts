import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);
const numbers = text.split("\n").map(Number);
let p1 = 0;
let p2 = 0;
for (let i = 1; i < numbers.length; i++) {
	const a = numbers[i - 1];
	const b = numbers[i];
	if (a < b) p1++;
}
for (let i = 2; i < numbers.length; i++) {
	const c = numbers.slice(i - 2, i + 1).reduce((a, b) => a + b);
	const d = numbers.slice(i - 1, i + 2).reduce((a, b) => a + b);
	if (c < d) p2++;
}
console.log("Part 1:", p1);
console.log("Part 2:", p2);

export {};
