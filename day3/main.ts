import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

let lines = text.split("\n").map(a => a.split(""));
let gamma = "";

for (let i = 0; i < lines[0].length; i++) {
	const dict = new Map<string, number>();
	for (let j = 0; j < lines.length; j++) {
		const char = lines[j][i];
		if (!dict.has(char)) {
			dict.set(char, 1);
		} else {
			dict.set(char, (dict.get(char) as number) + 1);
		}
	}
	gamma += (dict.get("0") || 0) > (dict.get("1") || 0) ? "0" : "1";
}

const gRate = parseInt(gamma, 2);
const eRate = 2 ** lines[0].length - gRate - 1;

for (let i = 0; i < lines[0].length; i++) {
	const dict = new Map<string, number>();
	for (let j = 0; j < lines.length; j++) {
		const char = lines[j][i];
		if (!dict.has(char)) {
			dict.set(char, 1);
		} else {
			dict.set(char, (dict.get(char) as number) + 1);
		}
	}
	const mostCommon = (dict.get("0") || 0) > (dict.get("1") || 0) ? "0" : "1";
	lines = lines.filter(a => a[i] === mostCommon);
	if (lines.length <= 1) {
		break;
	}
}

let O2rating = parseInt(lines[0].join(""), 2);
lines = text.split("\n").map(a => a.split(""));

for (let i = 0; i < lines[0].length; i++) {
	const dict = new Map<string, number>();
	for (let j = 0; j < lines.length; j++) {
		const char = lines[j][i];
		if (!dict.has(char)) {
			dict.set(char, 1);
		} else {
			dict.set(char, (dict.get(char) as number) + 1);
		}
	}
	const leastCommon =
		(dict.get("0") || 0) <= (dict.get("1") || 0) ? "0" : "1";
	lines = lines.filter(a => a[i] === leastCommon);
	if (lines.length <= 1) {
		break;
	}
}

console.log("Part 1:", gRate * eRate);
console.log("Part 2:", parseInt(lines[0].join(""), 2) * O2rating);

export {};
