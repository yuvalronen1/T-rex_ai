from random import randrange as rnd
from itertools import cycle
from random import choice
from PIL import  Image
import pygame
import time
import math

def jump(x):
    return x/15

pygame.init()
speed = 2



# extracting game items and characters form the resource.png image.
player_init = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((77,5,163,96)).convert("RGBA")
player_init = player_init.resize(list(map(lambda x:x//2 , player_init.size)))

player_frame_1 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1679,2,1765,95)).convert("RGBA")
player_frame_1 = player_frame_1.resize(list(map(lambda x:x//2 , player_frame_1.size)))

player_frame_2 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1767,2,1853,95)).convert("RGBA")
player_frame_2 = player_frame_2.resize(list(map(lambda x:x//2 , player_frame_2.size)))

player_frame_3 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1855,2,1941,95)).convert("RGBA")
player_frame_3 = player_frame_3.resize(list(map(lambda x:x//2 , player_frame_3.size)))

player_frame_31 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1943,2,2029,95)).convert("RGBA")
player_frame_31 = player_frame_31.resize(list(map(lambda x:x//2 , player_frame_31.size)))

player_frame_4 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((2030,2,2117,95)).convert("RGBA")
player_frame_4 = player_frame_4.resize(list(map(lambda x:x//2 , player_frame_4.size)))

player_frame_5 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((2207,2,2323,95)).convert("RGBA")
player_frame_5 = player_frame_5.resize(list(map(lambda x:x//2 , player_frame_5.size)))

player_frame_6 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((2324,2,2441,95)).convert("RGBA")
player_frame_6 = player_frame_6.resize(list(map(lambda x:x//2 , player_frame_6.size)))

cloud = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((166,2,257,29)).convert("RGBA")
cloud = cloud.resize(list(map(lambda x:x//2 , cloud.size)))

ground = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((2,102,2401,127)).convert("RGBA")
ground = ground.resize(list(map(lambda x:x//2 , ground.size)))

obstacle1 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((446,2,479,71)).convert("RGBA")
obstacle1 = obstacle1.resize(list(map(lambda x:x//2 , obstacle1.size)))

obstacle2 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((446,2,547,71)).convert("RGBA")
obstacle2 = obstacle2.resize(list(map(lambda x:x//2 , obstacle2.size)))

obstacle3 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((446,2,581,71)).convert("RGBA")
obstacle3 = obstacle3.resize(list(map(lambda x:x//2 , obstacle3.size)))

obstacle4 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((653,2,701,101)).convert("RGBA")
obstacle4 = obstacle4.resize(list(map(lambda x:x//2 , obstacle4.size)))

obstacle5 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((653,2,749,101)).convert("RGBA")
obstacle5 = obstacle5.resize(list(map(lambda x:x//2 , obstacle5.size)))

obstacle6 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((851,2,950,101)).convert("RGBA")
obstacle6 = obstacle6.resize(list(map(lambda x:x//2 , obstacle6.size)))

bird1 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((258,15,347,105)).convert("RGBA")
bird1 = bird1.resize(list(map(lambda x:x//2 , bird1.size)))

bird2 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((355,2,440,55)).convert("RGBA")
bird2 = bird2.resize(list(map(lambda x:x//2 , bird2.size)))

num0 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1292,0,1312,28)).convert("RGBA")
num0 = num0.resize(list(map(lambda x:x//2 , num0.size)))

num1 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1312,0,1332,28)).convert("RGBA")
num1 = num1.resize(list(map(lambda x:x//2 , num1.size)))

num2 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1332,0,1352,28)).convert("RGBA")
num2 = num2.resize(list(map(lambda x:x//2 , num2.size)))

num3 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1352,0,1372,28)).convert("RGBA")
num3 = num3.resize(list(map(lambda x:x//2 , num3.size)))

num4 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1372,0,1392,28)).convert("RGBA")
num4 = num4.resize(list(map(lambda x:x//2 , num4.size)))

num5 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1392,0,1412,28)).convert("RGBA")
num5 = num5.resize(list(map(lambda x:x//2 , num5.size)))

num6 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1412,0,1432,28)).convert("RGBA")
num6 = num6.resize(list(map(lambda x:x//2 , num6.size)))

num7 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1432,0,1452,28)).convert("RGBA")
num7 = num7.resize(list(map(lambda x:x//2 , num7.size)))

num8 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1452,0,1472,28)).convert("RGBA")
num8 = num8.resize(list(map(lambda x:x//2 , num8.size)))

num9 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1472,0,1493,28)).convert("RGBA")
num9 = num9.resize(list(map(lambda x:x//2 , num9.size)))

def showScore(score):
    numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    size = math.floor(math.log10(score)) + 1
    score = str(score)
    pos = (10, 10)
    for i in range(size):
        num = numbers[int(score[i])]
        gameDisplay.blit(pygame.image.fromstring(num.tobytes(), num.size, 'RGBA'), pos)
        pos = (pos[0] + 10, 10)


speed_identifier = lambda x: 2 if x >= 30 else 8 if x < 8 else 5
cust_speed = speed_identifier(speed)
running = cycle([player_frame_3]*cust_speed+[player_frame_31]*cust_speed)
crouch = cycle([player_frame_5]*cust_speed+ [player_frame_6]*cust_speed)
flying = cycle([bird1]*cust_speed + [bird1]*cust_speed + [bird2]*cust_speed + [bird2]*cust_speed)
crouch_scope = [player_frame_5]+[player_frame_6]
obstacles = [obstacle1,obstacle2, obstacle3,obstacle4,obstacle5,obstacle6, bird1]
isbird1 = False
isbird3 = False

playing = True
gameDisplay = pygame.display.set_mode((600,200))
while playing:
    score = 1
    speed = 2
    pygame.display.set_caption('T-Rex Runner')
    clock = pygame.time.Clock()
    state = running
    crashed = False
    lock = False
    bg = (0, 150)
    bg1 = (600,150)
    start = True
    height = 110
    jumping = False
    fast_fall = False
    c1 = (rnd(30, 600), rnd(0, 100))
    c2 = (rnd(50,600), rnd(0, 100))
    c3 = (rnd(30,700), rnd(0, 100))
    c4 = (rnd(30,600),rnd(0, 100))
    obs1 = (rnd(600, 600+500), 130)
    obs3 = (rnd(1700, 2000), 130)
    obast1 = choice(obstacles)
    if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (obs1[0], 115)
    if obast1 is bird1:
        obs1 = (obs1[0], choice([60, 100, 120]))
        isbird1 = True
    else:
        isbird1 = False
    obast3 = choice(obstacles)
    if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (obs3[0], 115)
    if obast3 is bird1:
        obs3 = (obs3[0], choice([60, 100, 120]))
        isbird3 = True
    else:
        isbird3 = False

    while not crashed:
        score += 0.1
        speed += 0.001
        gameDisplay.fill((255,255,255))
        showScore(math.floor(score))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                playing = False
            if event.type==pygame.KEYDOWN:
                start = True
                if event.key == pygame.K_DOWN:
                    fast_fall = True
                    state = crouch
                if event.key == pygame.K_UP:
                    if height >= 110:jumping = True
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    fast_fall = False
                    state = running
        player = state if type(state) != cycle else next(state)
        if isbird1: obast1 = next(flying)
        if isbird3: obast3 = next(flying)

        gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), c1)
        gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), c2)
        gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), c3)
        gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), c4)
        c1 = (c1[0]-1, c1[1])
        c2 = (c2[0]-1, c2[1])
        c3 = (c3[0]-1, c3[1])
        c4 = (c4[0]-1, c4[1])
        if c1[0]<= -50:
            c1 = (640, c1[1])
        if c2[0]<= -50:
            c2 = (700, c2[1])
        if c3[0]<= -50:
            c3 = (600, c3[1])
        if c4[0]<= -50:
            c4 = (800, c4[1])
        gameDisplay.blit(pygame.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), bg)
        gameDisplay.blit(pygame.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), bg1)
        if jumping:
            if height>=110-100:
                height -= jump(height)
            if height <= 110-100:
                jumping = False
        if height<110 and not jumping:
            if fast_fall:
                height += 7
            else: height += jump(height)
        player = gameDisplay.blit(pygame.image.fromstring(player.tobytes(), player.size, 'RGBA'), (5,height))
        gameDisplay.blit(pygame.image.fromstring(obast1.tobytes(), obast1.size, 'RGBA'), obs1)
        gameDisplay.blit(pygame.image.fromstring(obast3.tobytes(), obast3.size, 'RGBA'), obs3)
        if obs1[0]<=-50:
            obs1 = (rnd(600, 600+500), 130)
            obast1 = choice(obstacles)
            if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (obs1[0], 115)
            if obast1 is bird1:
                obs1 = (obs1[0], choice([80, 60]))
                isbird1 = True
            else:
                isbird1 = False
        if obs3[0]<=-50:
            obs3 = (rnd(1700, 2000), 130) 
            obast3 = choice(obstacles)
            if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (obs3[0], 115)
            if obast3 is bird1:
                obs3 = (obs3[0], choice([80, 60]))
                isbird3 = True
            else:
                isbird3 = False
        player_stading_cub = (5, height + 40 if crouch else height, 5 + 43,height + 46)
        if height< 100:
            start=True
        if start:
            obs1 = (obs1[0]-speed, obs1[1])
            obs3 = (obs3[0]-speed, obs3[1])
            obs1_cub = (obs1[0], obs1[1], obs1[0]+obast1.size[0],obs1[1]+obast1.size[1])
            obs3_cub = (obs3[0], obs3[1], obs3[0]+obast3.size[0],obs3[1]+obast3.size[1])
            if not lock:
                bg = (bg[0]-speed, bg[1])
                if bg[0]<=-(600):
                    lock = 1
            if -bg[0]>=600 and lock:
                bg1 = (bg1[0]-speed, bg1[1])
                bg = (bg[0]-speed, bg[1])
                if -bg1[0]>=600:bg = (600,150)
            if -bg1[0]>=600 and lock:
                bg = (bg[0]-speed, bg1[1])
                bg1 = (bg1[0]-speed, bg1[1])
                if -bg[0]>=600:bg1 = (600,150)

            if obs1_cub[0]<=player_stading_cub[2]-10<=obs1_cub[2] and (obs1_cub[1]<=player_stading_cub[3]-10<=obs1_cub[3]-5 or obs1_cub[1]<=player_stading_cub[1]-10<=obs1_cub[3]-5):
                crashed = True
                speed = 2
                state = player_frame_4
            if obs3_cub[0]<=player_stading_cub[2]-10<=obs3_cub[2] and (obs3_cub[1]<=player_stading_cub[3]-10<=obs3_cub[3]-5 or obs3_cub[1]<=player_stading_cub[1]-10<=obs3_cub[3]-5):
                crashed = True
                speed = 2
                state = player_frame_4
        pygame.display.update()
        clock.tick(120)