from PIL import  Image
import pygame
import math
from itertools import cycle
from random import randrange as rnd
import logic


# extracting game items and characters form the resource.png image.
player_frame_1 = Image.open(r"game\resources.png").crop((1855,2,1941,95)).convert("RGBA")
player_frame_1 = player_frame_1.resize(list(map(lambda x:x//2 , player_frame_1.size)))

player_frame_2 = Image.open(r"game\resources.png").crop((1943,2,2029,95)).convert("RGBA")
player_frame_2 = player_frame_2.resize(list(map(lambda x:x//2 , player_frame_2.size)))

player_frame_4 = Image.open(r"game\resources.png").crop((2030,2,2117,95)).convert("RGBA")
player_frame_4 = player_frame_4.resize(list(map(lambda x:x//2 , player_frame_4.size)))

player_frame_5 = Image.open(r"game\resources.png").crop((2207,2,2323,95)).convert("RGBA")
player_frame_5 = player_frame_5.resize(list(map(lambda x:x//2 , player_frame_5.size)))

player_frame_6 = Image.open(r"game\resources.png").crop((2324,2,2441,95)).convert("RGBA")
player_frame_6 = player_frame_6.resize(list(map(lambda x:x//2 , player_frame_6.size)))

cloud = Image.open(r"game\resources.png").crop((166,2,257,29)).convert("RGBA")
cloud = cloud.resize(list(map(lambda x:x//2 , cloud.size)))

ground = Image.open(r"game\resources.png").crop((2,102,2401,127)).convert("RGBA")
ground = ground.resize(list(map(lambda x:x//2 , ground.size)))

obstacle1 = Image.open(r"game\resources.png").crop((446,2,479,71)).convert("RGBA")
obstacle1 = obstacle1.resize(list(map(lambda x:x//2 , obstacle1.size)))

obstacle2 = Image.open(r"game\resources.png").crop((446,2,547,71)).convert("RGBA")
obstacle2 = obstacle2.resize(list(map(lambda x:x//2 , obstacle2.size)))

obstacle3 = Image.open(r"game\resources.png").crop((446,2,581,71)).convert("RGBA")
obstacle3 = obstacle3.resize(list(map(lambda x:x//2 , obstacle3.size)))

obstacle4 = Image.open(r"game\resources.png").crop((653,2,701,101)).convert("RGBA")
obstacle4 = obstacle4.resize(list(map(lambda x:x//2 , obstacle4.size)))

obstacle5 = Image.open(r"game\resources.png").crop((653,2,749,101)).convert("RGBA")
obstacle5 = obstacle5.resize(list(map(lambda x:x//2 , obstacle5.size)))

obstacle6 = Image.open(r"game\resources.png").crop((851,2,950,101)).convert("RGBA")
obstacle6 = obstacle6.resize(list(map(lambda x:x//2 , obstacle6.size)))

bird1 = Image.open(r"game\resources.png").crop((258,15,347,105)).convert("RGBA")
bird1 = bird1.resize(list(map(lambda x:x//2 , bird1.size)))

bird2 = Image.open(r"game\resources.png").crop((355,2,440,55)).convert("RGBA")
bird2 = bird2.resize(list(map(lambda x:x//2 , bird2.size)))

num0 = Image.open(r"game\resources.png").crop((1292,0,1312,28)).convert("RGBA")
num0 = num0.resize(list(map(lambda x:x//2 , num0.size)))

num1 = Image.open(r"game\resources.png").crop((1312,0,1332,28)).convert("RGBA")
num1 = num1.resize(list(map(lambda x:x//2 , num1.size)))

num2 = Image.open(r"game\resources.png").crop((1332,0,1352,28)).convert("RGBA")
num2 = num2.resize(list(map(lambda x:x//2 , num2.size)))

num3 = Image.open(r"game\resources.png").crop((1352,0,1372,28)).convert("RGBA")
num3 = num3.resize(list(map(lambda x:x//2 , num3.size)))

num4 = Image.open(r"game\resources.png").crop((1372,0,1392,28)).convert("RGBA")
num4 = num4.resize(list(map(lambda x:x//2 , num4.size)))

num5 = Image.open(r"game\resources.png").crop((1392,0,1412,28)).convert("RGBA")
num5 = num5.resize(list(map(lambda x:x//2 , num5.size)))

num6 = Image.open(r"game\resources.png").crop((1412,0,1432,28)).convert("RGBA")
num6 = num6.resize(list(map(lambda x:x//2 , num6.size)))

num7 = Image.open(r"game\resources.png").crop((1432,0,1452,28)).convert("RGBA")
num7 = num7.resize(list(map(lambda x:x//2 , num7.size)))

num8 = Image.open(r"game\resources.png").crop((1452,0,1472,28)).convert("RGBA")
num8 = num8.resize(list(map(lambda x:x//2 , num8.size)))

num9 = Image.open(r"game\resources.png").crop((1472,0,1493,28)).convert("RGBA")
num9 = num9.resize(list(map(lambda x:x//2 , num9.size)))

# T-rex's and bird's animation
running = cycle([player_frame_1] * 8 +[player_frame_2] * 8)
crouch = cycle([player_frame_5] * 8 + [player_frame_6] * 8)
flying = cycle([bird1] * 8 * 2 + [bird2] * 8 * 2)

obstacles = {"o1" : obstacle1, "o2" : obstacle2, "o3" : obstacle3, "o4" : obstacle4, "o5" : obstacle5, "o6" : obstacle6, "b" : bird1}

class Graphics():

    def __init__(self, screenSize, is_displayed):
        # initilaize pygame
        pygame.init()
        
        # create clock
        self.clock = pygame.time.Clock()

        if is_displayed:
            # set game display
            self.gameDisplay = pygame.display.set_mode(screenSize)
            pygame.display.set_caption('T-Rex Runner')

            # create background
            self.c1 = (rnd(30, 600), rnd(0, 100))
            self.c2 = (rnd(50,600), rnd(0, 100))
            self.c3 = (rnd(30,700), rnd(0, 100))
            self.c4 = (rnd(30,600),rnd(0, 100))
            self.lock = False
            self.bg = (0, 150)
            self.bg1 = (600,150)

    def updateBackground(self, speed):
        self.gameDisplay.fill((255, 255, 255))
        # move clouds
        self.c1 = (self.c1[0]-1, self.c1[1])
        self.c2 = (self.c2[0]-1, self.c2[1])
        self.c3 = (self.c3[0]-1, self.c3[1])
        self.c4 = (self.c4[0]-1, self.c4[1])
        if self.c1[0] <= -50:
            self.c1 = (640, self.c1[1])
        if self.c2[0] <= -50:
            self.c2 = (700, self.c2[1])
        if self.c3[0] <= -50:
            self.c3 = (600, self.c3[1])
        if self.c4[0] <= -50:
            self.c4 = (800, self.c4[1])
        # move ground
        if not self.lock:
            self.bg = (self.bg[0] - speed, self.bg[1])
            if self.bg[0] <= -(600):
                self.lock = 1
        if -self.bg[0] >= 600 and self.lock:
            self.bg1 = (self.bg1[0] - speed, self.bg1[1])
            self.bg = (self.bg[0]- speed, self.bg[1])
            if -self.bg1[0] >= 600: self.bg = (600,150)
        if -self.bg1[0] >= 600 and self.lock:
            self.bg = (self.bg[0]- speed, self.bg1[1])
            self.bg1 = (self.bg1[0]- speed, self.bg1[1])
            if -self.bg[0]>=600: self.bg1 = (600,150)
        # draw clouds and background
        self.gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), self.c1)
        self.gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), self.c2)
        self.gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), self.c3)
        self.gameDisplay.blit(pygame.image.fromstring(cloud.tobytes(), cloud.size, 'RGBA'), self.c4)
        self.gameDisplay.blit(pygame.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), self.bg)
        self.gameDisplay.blit(pygame.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), self.bg1)

    # display player's score
    def showScore(self, score):
        numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
        size = math.floor(math.log10(score)) + 1
        score = str(score)
        pos = (10, 10)
        for i in range(size):
            num = numbers[int(score[i])]
            self.gameDisplay.blit(pygame.image.fromstring(num.tobytes(), num.size, 'RGBA'), pos)
            pos = (pos[0] + 10, pos[1])
    
    # display obsticle
    def showObsitcle(self, obs):
        obast = obstacles[obs.sort]
        if obs.isbird:
            obast = next(flying)
        self.gameDisplay.blit(pygame.image.fromstring(obast.tobytes(), obast.size, 'RGBA'), obs.pos)
    
    # display player
    def showPlayer(self, p):
        if p.state == 'r':
            frame = next(running)
        else:
            frame = next(crouch)
        
        self.gameDisplay.blit(pygame.image.fromstring(frame.tobytes(), frame.size, 'RGBA'), (p.POSITION, p.height))


###################################################################################################################
def play(ai_active: bool, display: bool):
    while True:
        
        l = logic.Logic(2)
        game = Graphics((600,200), display)

        p = logic.Player()

        ob = logic.Obstacle()

        while not p.isCrashed(ob):
            # adjust speed and score
            l.updateSpeedScore()
            # display background
            if display:
                game.updateBackground(l.speed)
            if ai_active:
                choice = yield p.height, ob.pos[0], ob.pos[1], int(ob.sort[1]) if len(ob.sort) == 2 else 7, l.speed
                if choice == 2:
                    l.downKey(p)
                else:
                    l.keyUp(p)
                    if choice == 1:
                        l.upKey(p)
            else:
                # check input
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type==pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                l.downKey(p)
                            if event.key == pygame.K_UP:
                                l.upKey(p)
                        if event.type==pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                l.keyUp(p)

            l.update_height(p)

            # show player
            if display:
                game.showPlayer(p)

            # move and show Obstacle
            ob.move(l.speed)
            if display:
                game.showObsitcle(ob)

            if ob.pos[0] <= -50:
                ob = logic.Obstacle()

            # show score
            if display:
                game.showScore(l.score)
                pygame.display.update()
            
            if not ai_active:
                game.clock.tick(120)

        if ai_active:
            yield "done"
            

#########################################################################################
import neat
import numpy as np

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        run = play(True, True)
        net_input = run.send(None)
        while type(net_input) == tuple:
            net_output = net.activate(net_input)
            softmax_result = neat.math_util.softmax(net_output)
            output = np.argmax(np.argmax((softmax_result / np.max(softmax_result)) == 1).astype(int))
            net_input = run.send(output)
        
        genome.fitness = net_input

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(eval_genomes, 10)
    
run(r"game\config-feedforward")