import { join, dirname, fromFileUrl } from "https://deno.land/std/path/mod.ts";

const text = await Deno.readTextFile(
	join(dirname(fromFileUrl(import.meta.url)), "input.txt")
);
const lines = text.split("\n");

const numbers = lines[0].split(",").map(n => parseInt(n));

const boards = lines
	.slice(1)
	.reduce((acc, line) => {
		if (line.length === 0) {
			acc.push([]);
			return acc;
		} else {
			acc[acc.length - 1].push(line);
			return acc;
		}
	}, [] as string[][])
	.map(board =>
		board.map(line =>
			line
				.trim()
				.split(" ")
				.filter(n => n.length > 0)
				.map(n => parseInt(n))
		)
	)
	.slice(0, -1);

function boardWon(board: number[][]) {
	for (let i = 0; i < board.length; i++) {
		if (board[i].every(n => n < 0)) {
			return true;
		}
	}
	for (let i = 0; i < board[0].length; i++) {
		if (board.every(row => row[i] < 0)) {
			return true;
		}
	}
	return false;
}

function score(board: number[][]) {
	return board.reduce(
		(acc, row) =>
			acc + row.filter(n => n >= 0).reduce((acc, n) => acc + n, 0),
		0
	);
}

let firstWin: number | undefined;

const winners: number[][][] = [];

for (const number of numbers) {
	for (let b = 0; b < boards.length; b++) {
		const board = boards[b];
		board.forEach((row, i) => {
			row.forEach((n, j) => {
				if (n === number) {
					board[i][j] = -1;
				}
			});
		});
		if (boardWon(board)) {
			firstWin = firstWin || score(board) * number;
			winners.push(board);
			if (boards.length <= 1) {
				console.log("Part 1:", firstWin!);
				console.log("Part 2:", score(board) * number);
				Deno.exit();
			}
			boards.splice(b, 1);
			b--;
		}
	}
}

export {};
