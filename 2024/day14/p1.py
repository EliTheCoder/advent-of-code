from math import floor, ceil

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

seconds = 100

q1, q2, q3, q4 = 0, 0, 0, 0

for robot in robots:
    robot.move(seconds)
    if robot.px < floor(width/2) and robot.py < floor(height/2): q1 += 1
    if robot.px > floor(width/2) and robot.py < floor(height/2): q2 += 1
    if robot.px < floor(width/2) and robot.py > floor(height/2): q3 += 1
    if robot.px > floor(width/2) and robot.py > floor(height/2): q4 += 1

print(q1*q2*q3*q4)