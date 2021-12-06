import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);
const lines = text.split("\n");

const ventPoints: Point[] = [];
const crossPoints: Point[] = [];

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
	constructor(public start: Point, public end: Point) {}

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
			for (let x = this.start.x, y = this.start.y; x <= this.end.x; x++) {
				points.push(new Point(x, y));
				y++;
			}
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

const vents = lines
	.map(line => {
		const lineArr = line.split(" -> ").map(point => {
			const pointArr = point.split(",").map(Number);
			return new Point(pointArr[0], pointArr[1]);
		});
		return new Line(lineArr[0], lineArr[1]);
	})
	.slice(0, -1)
	.filter(line => line.type() !== LineType.DIAGONAL);

for (const vent of vents) {
	vent.span().forEach(point => {
		if (!ventPoints.some(v => v.equals(point))) {
			ventPoints.push(point);
		} else if (!crossPoints.some(v => v.equals(point))) {
			crossPoints.push(point);
		}
	});
}

console.log(ventPoints.length);
console.log(crossPoints.length);
