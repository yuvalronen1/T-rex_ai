from random import choice
from random import randrange as rnd

obstacles = ["o1", "o2", "o3", "o4", "o5", "o6", "b1"]

class Logic():

    def __init__(self, speed):
        self.intialSpeed = speed
        self.speed = speed
        self.score = 1
        self.state = 'r'
        self.chrashed = False
        self.jumping = False
        self.fast_fall = False
        self.height = 110



    def newObs(self):
        obs = (rnd(600, 600+500), 130)
        obast = choice(obstacles)
        if obast in  ["o4", "o5", "o6"]:obs = (obs[0], 115)
        if obast == "b1":
            obs1 = (obs1[0], choice([80, 60]))
            isbird = True
        else: isbird = False
        
        return obs, obast, isbird
    
    def updateSpeedScore(self):
        self.speed += 0.001
        self.score += 0.1