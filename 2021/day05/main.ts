import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);
const lines = text.split("\n");

let ventPoints: Point[] = [];
let crossPoints: Point[] = [];

class Point {
	constructor(public x: number, public y: number) {}
	equals(other: Point) {
		return this.x === other.x && this.y === other.y;
	}
}

enum LineType {
	HORIZONTAL,
	VERTICAL,
	DIAGONAL
}

class Line {
	public start: Point;
	public end: Point;

	constructor(start: Point, end: Point) {
		if (start.x > end.x) {
			[start, end] = [end, start];
		}
		if (start.y > end.y) {
			[start, end] = [end, start];
		}
		this.start = start;
		this.end = end;
	}

	span(): Point[] {
		const points = [];
		if (this.type() === LineType.HORIZONTAL) {
			for (let x = this.start.x; x <= this.end.x; x++) {
				points.push(new Point(x, this.start.y));
			}
		} else if (this.type() === LineType.VERTICAL) {
			for (let y = this.start.y; y <= this.end.y; y++) {
				points.push(new Point(this.start.x, y));
			}
		} else if (this.type() === LineType.DIAGONAL) {
			let x = this.start.x;
			let y = this.start.y;
			while (x !== this.end.x) {
				points.push(new Point(x, y));
				if (x < this.end.x) x++;
				if (x > this.end.x) x--;
				if (y < this.end.y) y++;
				if (y > this.end.y) y--;
			}
			points.push(new Point(x, y));
		}
		return points;
	}

	type(): LineType {
		if (this.start.x === this.end.x) {
			return LineType.VERTICAL;
		}

		if (this.start.y === this.end.y) {
			return LineType.HORIZONTAL;
		}

		return LineType.DIAGONAL;
	}
}

let vents = lines.slice(0, -1).map(line => {
	const lineArr = line.split(" -> ").map(point => {
		const pointArr = point.split(",").map(Number);
		return new Point(pointArr[0], pointArr[1]);
	});
	return new Line(lineArr[0], lineArr[1]);
});

for (const vent of vents) {
	vent.span().forEach(point => {
		if (!ventPoints.some(v => v.equals(point))) {
			ventPoints.push(point);
		} else if (!crossPoints.some(v => v.equals(point))) {
			crossPoints.push(point);
		}
	});
}

let part2 = crossPoints.length;

vents = vents.filter(line => line.type() !== LineType.DIAGONAL);

crossPoints = [];
ventPoints = [];

for (const vent of vents) {
	vent.span().forEach(point => {
		if (!ventPoints.some(v => v.equals(point))) {
			ventPoints.push(point);
		} else if (!crossPoints.some(v => v.equals(point))) {
			crossPoints.push(point);
		}
	});
}

console.log("Part 1:", crossPoints.length);
console.log("Part 2:", part2);
