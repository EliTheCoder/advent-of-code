from enum import Enum, auto
from sys import maxsize
from math import sqrt, ceil

games_str = open("input.txt", "r").read().split("\n\n")

class Button(Enum):
    A = auto()
    B = auto()

class Game():
    def __init__(self, ax: int, ay: int, bx: int, by: int, px: int, py: int):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py
    
    def __repr__(self) -> str:
        return f"a=({self.ax},{self.ay}) b=({self.bx},{self.by}) p=({self.px},{self.py})"

    def won(self, x: int, y: int) -> bool:
        return x == self.px and y == self.py
    
    def move(self, x: int, y: int, button: Button) -> tuple[int, int]:
        if button == Button.A: return x + self.ax, y + self.ay
        else: return x + self.bx, y + self.by

    def moves(self, x: int, y: int, button: Button, qty: int) -> tuple[int, int]:
        if button == Button.A: return x + self.ax*qty, y + self.ay*qty
        else: return x + self.bx*qty, y + self.by*qty

    def undo(self, x: int, y: int, button: Button) -> tuple[int, int]:
        if button == Button.A: return x - self.ax, y - self.ay
        else: return x - self.bx, y - self.by


def parse_game(game_str: str) -> Game:
    a_str, b_str, p_str = game_str.splitlines()
    ax_str = a_str.split()[2][2:-1]
    ay_str = a_str.split()[3][2:]
    bx_str = b_str.split()[2][2:-1]
    by_str = b_str.split()[3][2:]
    px_str = p_str.split()[1][2:-1]
    py_str = p_str.split()[2][2:]
    return Game(int(ax_str), int(ay_str), int(bx_str), int(by_str), int(px_str)+10000000000000, int(py_str)+10000000000000)

games = [parse_game(game) for game in games_str]

def solve(game: Game, x: int, y: int) -> int:
    determinant = game.ax*game.by - game.ay*game.bx
    if determinant == 0: return 0
    a_num = game.by*game.px - game.bx*game.py
    b_num = game.ax*game.py - game.ay*game.px
    a = a_num / determinant
    b = b_num / determinant
    if int(a) == a and int(b) == b: return int(a)*3+int(b)*1
    return 0

total = 0

for game in games:
    solution = solve(game, 0, 0)
    total += solution

print(total)




