import pygame, sys, random, math
from bot import Bot
from dataset import format_array
import numpy as np

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WIDTH_PLAYER = 15
HEIGHT_PLAYER = 75
PLAYER_SPEED = 17
BALL_RADIUS = 10
BALL_SPEED = 10
WHITE = (255, 255, 255)

"""
    returns: 'u' for UP
             'd' for DOWN
             's' for STILL
"""
def getLabel():
    global positionBall, ballSpeed
    global positionP2
    if ballSpeed[0] > 0 and ballSpeed[1] > 0 and positionBall[1] > positionP2[1]:
        return 'd'

def resetGame():
    global positionBall, ballSpeed
    global playerScore, botScore
    print("Human: " + str(playerScore))
    print("Bot: " + str(botScore))
    positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    ballSpeed = [BALL_SPEED, -BALL_SPEED if random.randint(0, 1) == 0 else BALL_SPEED]


pygame.init()
bot = Bot()

np.set_printoptions(threshold=np.inf)

pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerScore = 0
botScore = 0
countUp = 760
countDown = 755
#countStill = 9

positionP1 = [35, 230]
positionP2 = [SCREEN_WIDTH - 35, 230]
ballSpeed = [BALL_SPEED, BALL_SPEED]
positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]

# game loop
while True:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, WHITE, positionBall, BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, [positionP1[0], positionP1[1], WIDTH_PLAYER, HEIGHT_PLAYER])
    pygame.draw.rect(screen, WHITE, [positionP2[0], positionP2[1], WIDTH_PLAYER, HEIGHT_PLAYER])


    # predict a move from the bot
    sc = pygame.surfarray.array3d(screen)
    pred = bot.getMoveArray(format_array(sc))
    index = np.argmax(pred)

    if index == 0:
        # UP
        print("UP")
        if positionP2[1] >= 0:
            positionP2[1] -= PLAYER_SPEED
    elif index == 1:
        # DOWN
        print("DOWN")
        if positionP2[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
            positionP2[1] += PLAYER_SPEED
    elif index == 2:
        # STILL
        print("STAY")


    # update ball position
    positionBall[0] += ballSpeed[0]
    positionBall[1] += ballSpeed[1]


    # ball collision check on walls
    if positionBall[1] <= BALL_RADIUS:
        ballSpeed[1] = -ballSpeed[1]

    if positionBall[1] + BALL_RADIUS >= SCREEN_HEIGHT:
        ballSpeed[1] = -ballSpeed[1]

    if positionBall[0] <= BALL_RADIUS:
        botScore += 1
        resetGame()

    if positionBall[0] + BALL_RADIUS >= SCREEN_WIDTH:
        playerScore += 1
        resetGame()


    # ball collison check on 2 paddles
    if positionBall[0] - BALL_RADIUS <= positionP1[0] and positionBall[1] >= positionP1[1] - 5 and positionBall[1] <= positionP1[1] + HEIGHT_PLAYER + 5:
        ballSpeed[0] = -ballSpeed[0]
    
    if positionBall[0] + BALL_RADIUS >= positionP2[0] and positionBall[1] >= positionP2[1] - 5 and positionBall[1] <= positionP2[1] + HEIGHT_PLAYER + 5:
        ballSpeed[0] = -ballSpeed[0]


    # checking user input to move the players
    # if UP or DOWN is pressed, a new image for a dataset is created, it will be used to train the neural network
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if positionP1[1] >= 0:
            positionP1[1] -= PLAYER_SPEED

    if keys[pygame.K_s]:
        if positionP1[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
            positionP1[1] += PLAYER_SPEED

    """
    if keys[pygame.K_UP]:
        #countUp += 1
        #pygame.image.save(screen, "Dataset/" + "u-" + str(countUp) + ".jpg")
        if positionP2[1] >= 0:
            positionP2[1] -= PLAYER_SPEED

    if keys[pygame.K_DOWN]:
        #countDown += 1
        #pygame.image.save(screen, "Dataset/" + "d-" + str(countDown) + ".jpg")
        if positionP2[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
            positionP2[1] += PLAYER_SPEED

    #else:
        #countStill += 1
        #pygame.image.save(screen, "Dataset/" + "s-" + str(countStill) + ".jpg")
    """

    # just to reset the ball
    if keys[pygame.K_SPACE]:
        positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("countUp is at: " + str(countUp))
            print("countDown is at: " + str(countDown))
            #print("countStill is at: " + countStill)
            pygame.quit()
            sys.exit()

    pygame.time.Clock().tick(50)
    pygame.display.flip()   # update screen
