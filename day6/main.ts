import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const fishes = text.split(",").map(x => parseInt(x));
const incubator = [0, 0, 0, 0, 0, 0, 0].map(BigInt);

const days = [0, 0, 0, 0, 0, 0, 0].map(BigInt);
for (let f of fishes) {
	const day = f % 7;
	days[day]++;
}

for (let i = 0; i < 256 + 1; i++) {
	console.log(
		`Day ${i} (${
			days.reduce((a, b) => a + b) + incubator.reduce((a, b) => a + b)
		} fish)`
	);
	const dow = i % 7;
	const newborns = days[dow];
	incubator[(dow + 2) % 7] += newborns;
	const grown = incubator[dow];
	incubator[dow] = BigInt(0);
	days[dow] += grown;
}
