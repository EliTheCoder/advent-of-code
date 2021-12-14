import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const lines = text
	.split("\n")
	.map(line => line.split("").map(c => parseInt(c)));

class Octopus {
	public value: number;
	constructor(public x: number, public y: number) {
		this.value = octopi[y][x];
	}
	step() {
		this.value++;
	}
}

let octopi = [];
for (let i = 0; i < lines.length; i++) {
	for (let j = 0; j < lines[0].length; j++) {
		octopi.push(new Octopus(j, i));
	}
}

function logOctopi() {
	console.log(octopi.map(o => o.value).join(""));
}
