from random import choice
from random import randrange as rnd

obstacles = ["o1", "o2", "o3", "o4", "o5", "o6", "b"]

obstacle_sizes = {"o1" : (16, 34), "o2" : (50, 34), "o3" : (67, 34), "o4" : (24, 49), "o5" : (48, 49), "o6" : (49, 49), "b" : (44, 45)}

def jump_motion(x):
    return x/15

class Logic():

    def __init__(self, speed):
        self.intialSpeed = speed
        self.speed = speed
        self.score = 1
        self.chrashed = False
    
    def updateSpeedScore(self):
        self.speed += 0.001
        self.score += 0.1
    
    def upKey(self, player):
        if player.height >= 110: 
            player.jumping = True
    
    def downKey(self, player):
        player.fast_fall = True
        player.state = 'c'

    def keyUp(self, player):
        player.fast_fall = False
        player.state = 'r'
    
    def update_height(self, player):
        if player.jumping:
            if player.height >= 110 - 100:
                player.height -= jump_motion(player.height)
            if player.height <= 110-100:
                player.jumping = False
        if player.height<110 and not player.jumping:
            if player.fast_fall:
                player.height += 7
            else: player.height += jump_motion(player.height)

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
        self.jumping = False
        self.fast_fall = False
     
    def isCrashed(self, obsticle):
        obs_cub = (obsticle.pos[0], obsticle.pos[1], obsticle.pos[0] + obstacle_sizes[obsticle.sort][0], obsticle.pos[1] + obstacle_sizes[obsticle.sort][1])
        player_stading_cub = (5, self.height + 40 if self.state == 'c' else self.height, 5 + 43,self.height + 46)
        if obs_cub[0]<=player_stading_cub[2]-10<=obs_cub[2] and (obs_cub[1]<=player_stading_cub[3]-10<=obs_cub[3]-5 or obs_cub[1]<=player_stading_cub[1]-10<=obs_cub[3]-5):
                return True
        return False