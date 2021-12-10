import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const lines = text.split("\n");

function blockCorrupt(line: string): number {
	const stack = [];
	const opens = "([{<".split("");
	const closes = ")]}>".split("");
	const chars = line.split("");
	for (const char of chars) {
		if (opens.includes(char)) {
			stack.push(char);
		} else if (stack[stack.length - 1] === opens[closes.indexOf(char)]) {
			stack.pop();
		} else {
			return points[char];
		}
	}
	return 0;
}

function blockIncomplete(line: string): number {
	const stack = [];
	const opens = "([{<".split("");
	const closes = ")]}>".split("");
	const chars = line.split("");
	for (const char of chars) {
		if (opens.includes(char)) {
			stack.push(char);
		} else if (stack[stack.length - 1] === opens[closes.indexOf(char)]) {
			stack.pop();
		} else {
			return 0;
		}
	}
	return stack
		.map(c => opens.indexOf(c) + 1)
		.reverse()
		.reduce((a, b) => a * 5 + b, 0);
}

const points: { [key: string]: number } = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
};

let part1 = 0;
let part2 = [];

for (const line of lines) {
	part1 += blockCorrupt(line);
	part2.push(blockIncomplete(line));
}

part2 = part2.filter(p => p > 0).sort((a, b) => b - a);

console.log("Part 1:", part1);
console.log("Part 2:", part2[(part2.length - 1) / 2]);
