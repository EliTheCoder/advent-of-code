import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);

const lines = text
	.split("\n")
	.map(line => line.split("").map(c => parseInt(c)));

const basins: Map<number, number> = new Map();

class Height {
	public height: number;
	constructor(public x: number, public y: number) {
		this.height = lines[y][x];
	}

	adjacent(): Height[] {
		const ads = [];
		if (this.x > 0) ads.push(new Height(this.x - 1, this.y));
		if (this.x < lines[this.y].length - 1)
			ads.push(new Height(this.x + 1, this.y));
		if (this.y > 0) ads.push(new Height(this.x, this.y - 1));
		if (this.y < lines.length - 1) ads.push(new Height(this.x, this.y + 1));
		return ads;
	}
	riskLevel(): number {
		return this.height + 1;
	}
	isLowPoint(): boolean {
		return this.adjacent().every(c => this.height < c.height);
	}
	basin(): Height | null {
		if (this.height === 9) return null;
		if (this.isLowPoint()) {
			return this;
		} else {
			return this.adjacent()
				.sort((a, b) => a.height - b.height)[0]
				.basin();
		}
	}
	index(): number {
		return this.x + this.y * lines[this.y].length;
	}
}

let part1 = 0;

for (let y = 0; y < lines.length; y++) {
	for (let x = 0; x < lines[y].length; x++) {
		const height = new Height(x, y);
		if (height.isLowPoint()) {
			part1 += height.riskLevel();
		}
		let basin = height.basin();
		if (basin === null) continue;
		if (basins.has(basin.index())) {
			basins.set(basin.index(), basins.get(basin.index())! + 1);
		} else {
			basins.set(basin.index(), 1);
		}
	}
}

console.log("Part 1:", part1);
console.log(
	"Part 2:",
	[...basins.entries()]
		.sort((a: [number, number], b: [number, number]) => b[1] - a[1])
		.slice(0, 3)
		.reduce((a: number, b: [number, number]) => a * b[1], 1)
);
