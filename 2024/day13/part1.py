from enum import Enum, auto
from sys import maxsize
from math import sqrt

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
    return Game(int(ax_str), int(ay_str), int(bx_str), int(by_str), int(px_str), int(py_str))

games = [parse_game(game) for game in games_str]

def solve(game: Game, x: int, y: int) -> int:
    a_cost = sqrt(game.ax*game.ax+game.ay*game.ay) / 3
    b_cost = sqrt(game.bx*game.bx+game.by*game.by) / 1
    cheap = Button.B if b_cost > a_cost else Button.A
    expensive = Button.A if b_cost > a_cost else Button.B
    x, y = 0, 0
    nc, ne = 0, 0
    while x < game.px and y < game.py:
        x, y = game.move(x, y, cheap)
        nc += 1
    while not game.won(x, y) and nc >= 0:
        if x > game.px or y > game.py:
            nc -= 1
            x, y = game.undo(x, y, cheap)
        else:
            ne += 1
            x, y = game.move(x, y, expensive)
        
    if nc < 0: return -1

    return nc*3+ne*1 if cheap == Button.A else nc*1+ne*3

total = 0

for game in games:
    solution = solve(game, 0, 0)
    if solution >= 0: total += solution

print(total)




