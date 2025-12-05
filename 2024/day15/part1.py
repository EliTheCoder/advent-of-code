from __future__ import annotations
from enum import Enum, auto

warehouse_str, moves_str = open("input.txt", "r").read().split("\n\n")

class Block(Enum):
    EMPTY = auto()
    WALL = auto()
    BOX = auto()
    ROBOT = auto()

    def __str__(self) -> str:
        match self:
            case Block.EMPTY: return "."
            case Block.BOX: return "O"
            case Block.WALL: return "#"
            case Block.ROBOT: return "@"
        assert False, f"Unknown block {self}"

    @staticmethod
    def parse(ch: str) -> Block:
        match ch:
            case ".": return Block.EMPTY
            case "O": return Block.BOX
            case "#": return Block.WALL
            case "@": return Block.ROBOT
        assert False, f"Unknown character {ch}"

rx, ry = 0, 0

warehouse: list[list[Block]] = []
for i, line in enumerate(warehouse_str.splitlines()):
    row = []
    for j, c in enumerate(line):
        block = Block.parse(c)
        if block == Block.ROBOT: rx, ry = j, i
        row.append(block)
    warehouse.append(row)

width = len(warehouse[0])
height = len(warehouse)

def parse_dir(ch: str) -> int:
    return ["^", ">", "v", "<"].index(ch)

moves = [parse_dir(ch) for ch in moves_str if ch != "\n"]

def move(x: int, y: int, d: int) -> tuple[int, int]:
    match d:
        case 0: y -= 1
        case 1: x += 1
        case 2: y += 1
        case 3: x -= 1
    return x, y

def push(x: int, y: int, d: int) -> bool:
    ch = warehouse[y][x]
    if ch == Block.WALL: return False
    if ch == Block.EMPTY: return True
    if ch == Block.BOX or ch == Block.ROBOT:
        mx, my = move(x, y, d)
        can_move = push(mx, my, d)
        if can_move:
            warehouse[y][x], warehouse[my][mx] = warehouse[my][mx], warehouse[y][x]
            return True
        else: return False
    assert False, f"Unknown block {ch}"

def print_warehouse() -> None:
    for row in warehouse:
        print("".join(map(str, row)))

for m in moves:
    can_move = push(rx, ry, m)
    if can_move:
        rx, ry = move(rx, ry, m)

total = 0
for y in range(height):
    for x in range(width):
        if warehouse[y][x] == Block.BOX: total += 100*y+x

print(total)