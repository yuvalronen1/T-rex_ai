from PIL import  Image
import pygame
import math

# initilaize pygame
pygame.init()


# extracting game items and characters form the resource.png image.
player_frame_1 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1855,2,1941,95)).convert("RGBA")
player_frame_1 = player_frame_1.resize(list(map(lambda x:x//2 , player_frame_1.size)))

player_frame_2 = Image.open(r"D:\Users\User\Documents\T-rex_ai\game\resources.png").crop((1943,2,2029,95)).convert("RGBA")
player_frame_2 = player_frame_2.resize(list(map(lambda x:x//2 , player_frame_2.size)))

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

class Graphics():

    def __init__(self, screenSize):
        # set game display
        self.gameDisplay = pygame.display.set_mode(screenSize)

    def displayBackground(self):
        pass

    # display player's score
    def showScore(self, score):
        numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
        size = math.floor(math.log10(score)) + 1
        score = str(score)
        pos = (10, 10)
        for i in range(size):
            num = numbers[int(score[i])]
            self.gameDisplay.blit(pygame.image.fromstring(num.tobytes(), num.size, 'RGBA'), pos)
            pos = (pos[0] + 10, 10)
