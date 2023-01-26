from random import choice
from random import randrange as rnd

obstacles = ["o1", "o2", "o3", "o4", "o5", "o6", "b"]

class Logic():

    def __init__(self, speed):
        self.intialSpeed = speed
        self.speed = speed
        self.score = 1
        self.chrashed = False
        self.jumping = False
        self.fast_fall = False
    
    def updateSpeedScore(self):
        self.speed += 0.001
        self.score += 0.1

class Obstacle():
    def __init__(self):
        self.pos = (rnd(600, 600+500), 130)
        self.sort = choice(obstacles)
        if self.sort in  ["o4", "o5", "o6"]: self.pos = (self.pos[0], 115)
        if self.sort == "b":
            self.pos = (self.pos[0], choice([80, 60]))
            self.isbird = True
        else: self.isbird = False
    
    def move(self, speed):
        self.pos = (self.pos[0] - speed, self.pos[1])


class Player():
    def __init__(self):
        self.state = 'r'
        self.height = 110
        self.POSITION = 5