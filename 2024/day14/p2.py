from math import floor, ceil
from time import sleep

robot_strs = open("input.txt", "r").read().splitlines()

width = 101
height = 103

class Robot():
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"{self.px},{self.py} {self.vx},{self.vy}"
    
    def move(self, s):
        self.px = (self.px + self.vx * s) % width
        self.py = (self.py + self.vy * s) % height

def parse_robot(robot_str):
    p_str, v_str = robot_str.split()
    ps = p_str.split(",")
    vs = v_str.split(",")
    return Robot(int(ps[0][2:]), int(ps[1]), int(vs[0][2:]), int(vs[1]))

robots = [parse_robot(robot) for robot in robot_strs]


def robot_at(rs, robot, x, y):
    rx = robot.px + x
    ry = robot.py + y
    if rx < 0 or rx >= width or ry < 0 or ry >= height: return False
    return next((robot for robot in robots if robot.px == rx and robot.py == ry), None) is not None

i = 7000
for robot in robots:
    robot.move(i)

while True:
    i += 1
    if i % 100 == 0: print(i)
    for robot in robots:
        robot.move(1)
    c = False
    for robot in robots:
        if robot_at(robots, robot, 0, 0) and robot_at(robots, robot, -1, 1) and robot_at(robots, robot, 0, 1) and robot_at(robots, robot, 1, 1) and robot_at(robots, robot, -2, 2) and robot_at(robots, robot, -1, 2) and robot_at(robots, robot, 0, 2) and robot_at(robots, robot, 1, 2) and robot_at(robots, robot, 2, 2):
           c = True
           break
    if not c: continue
    output = f"{i}\n"
    for y in range(width):
        for x in range(height):
            if next((robot for robot in robots if robot.px == x and robot.py == y), None) is not None:
                output += "##"
            else:
                output += "  "
        output += "\n"
    output += "-" * 200
    print(output)
