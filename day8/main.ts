import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const lines = text.split("\n");

const dicts = lines.map(line =>
	line
		.split(" | ")[0]
		.split(" ")
		.map(word => word.split("").sort().join(""))
		.sort((a, b) => a.length - b.length)
);
const nums = lines.map(line =>
	line
		.split(" | ")[1]
		.split(" ")
		.map(n => n.split("").sort().join(""))
);

function solve(dict: string[], num: string[]) {
	let key: string[] = Array(10);
	key[1] = dict.filter(word => word.length === 2)[0];
	key[4] = dict.filter(word => word.length === 4)[0];
	key[7] = dict.filter(word => word.length === 3)[0];
	key[8] = dict.filter(word => word.length === 7)[0];
	key[6] = dict.filter(
		word =>
			word.length === 6 &&
			!key[7].split("").every(letter => word.includes(letter))
	)[0];
	key[5] = dict.filter(
		word =>
			word.length === 5 &&
			word.split("").every(letter => key[6].includes(letter))
	)[0];
	key[9] = dict.filter(
		word =>
			word.length === 6 &&
			word !== key[6] &&
			key[5].split("").every(letter => word.includes(letter))
	)[0];
	key[0] = dict.filter(word => !key.includes(word) && word.length === 6)[0];
	key[3] = dict.filter(
		word =>
			!key.includes(word) &&
			word.split("").every(letter => key[9].includes(letter))
	)[0];
	key[2] = dict.filter(word => !key.includes(word))[0];

	return parseInt(num.map(n => key.indexOf(n)).join(""));
}

let part1 = 0;
let part2 = 0;
for (let i = 0; i < nums.length; i++) {
	let solution = solve(dicts[i], nums[i]);
	part2 += solution;
	part1 += solution
		.toString()
		.split("")
		.reduce((a, b) => a + (["1", "4", "7", "8"].includes(b) ? 1 : 0), 0);
}

console.log("Part 1:", part1);
console.log("Part 2:", part2);
