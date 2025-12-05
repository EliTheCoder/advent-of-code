from __future__ import annotations
from enum import Enum, auto

warehouse_str, moves_str = open("input.txt", "r").read().split("\n\n")

class Block(Enum):
    EMPTY = auto()
    WALL = auto()
    LEFT_BOX = auto()
    RIGHT_BOX = auto()
    ROBOT = auto()

    def __str__(self) -> str:
        match self:
            case Block.EMPTY: return "."
            case Block.LEFT_BOX: return "["
            case Block.RIGHT_BOX: return "]"
            case Block.WALL: return "#"
            case Block.ROBOT: return "@"
        assert False, f"Unknown block {self}"

    @staticmethod
    def parse(ch: str) -> tuple[Block, Block]:
        match ch:
            case ".": return Block.EMPTY, Block.EMPTY
            case "O": return Block.LEFT_BOX, Block.RIGHT_BOX
            case "#": return Block.WALL, Block.WALL
            case "@": return Block.ROBOT, Block.EMPTY
        assert False, f"Unknown character {ch}"

rx, ry = 0, 0

warehouse: list[list[Block]] = []
for i, line in enumerate(warehouse_str.splitlines()):
    row: list[Block] = []
    for j, c in enumerate(line):
        block = Block.parse(c)
        if block[0] == Block.ROBOT: rx, ry = j*2, i
        row += block
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

def can_push(x: int, y: int, d: int) -> bool:
    ch = warehouse[y][x]
    if ch == Block.WALL: return False
    if ch == Block.EMPTY: return True
    if ch == Block.ROBOT: return can_push(*move(x, y, d), d)
    if ch == Block.LEFT_BOX:
        if d == 3: return can_push(*move(x, y, d), d)
        ox, oy = move(x, y, 1)
        return can_push(*move(x, y, d), d) and can_push(*move(ox, oy, d), d)
    if ch == Block.RIGHT_BOX:
        if d == 1: return can_push(*move(x, y, d), d)
        ox, oy = move(x, y, 3)
        return can_push(*move(x, y, d), d) and can_push(*move(ox, oy, d), d)
    assert False, f"Unknown block {ch}"

def push(x: int, y: int, d: int, force: bool = False) -> bool:
    ch = warehouse[y][x]
    if ch == Block.EMPTY: return True
    if ch == Block.WALL: return False
    if ch == Block.LEFT_BOX:
        if can_push(x, y, d):
            if d == 1:
                if not force:
                    ox, oy = move(x, y, 1)
                    push(ox, oy, d, True)
                mx, my = move(x, y, d)
                push(mx, my, d)
            else:
                mx, my = move(x, y, d)
                push(mx, my, d)
                if not force:
                    ox, oy = move(x, y, 1)
                    push(ox, oy, d, True)
            warehouse[y][x], warehouse[my][mx] = warehouse[my][mx], warehouse[y][x]
            return True
        return False
    if ch == Block.RIGHT_BOX:
        if can_push(x, y, d):
            if d == 3:
                if not force:
                    ox, oy = move(x, y, 3)
                    push(ox, oy, d, True)
                mx, my = move(x, y, d)
                push(mx, my, d)
            else:
                mx, my = move(x, y, d)
                push(mx, my, d)
                if not force:
                    ox, oy = move(x, y, 3)
                    push(ox, oy, d, True)
            warehouse[y][x], warehouse[my][mx] = warehouse[my][mx], warehouse[y][x]
            return True
        return False
    if ch == Block.ROBOT:
        if can_push(x, y, d):
            mx, my = move(x, y, d)
            push(mx, my, d)
            warehouse[y][x], warehouse[my][mx] = warehouse[my][mx], warehouse[y][x]
            return True
        return False
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
        if warehouse[y][x] == Block.LEFT_BOX: total += 100*y+x

print(total)