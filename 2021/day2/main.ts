import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);
const instructions: [string, number][] = text
	.split("\n")
	.map(a => [a.split(" ")[0], parseInt(a.split(" ")[1])]);
let x = 0;
let y = 0;
let x2 = 0;
let y2 = 0;
let a = 0;
for (const i of instructions) {
	if (i[0] === "forward") x += i[1];
	if (i[0] === "up") y -= i[1];
	if (i[0] === "down") y += i[1];
}
for (const i of instructions) {
	if (i[0] === "forward") {
		x2 += i[1];
		y2 += a * i[1];
	}
	if (i[0] === "up") {
		a -= i[1];
	}
	if (i[0] === "down") {
		a += i[1];
	}
}

console.log("Part 1:", x * y);
console.log("Part 2:", x2 * y2);

export {};
