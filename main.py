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


def render():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, WHITE, positionBall, BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, [positionP1[0], positionP1[1], WIDTH_PLAYER, HEIGHT_PLAYER])
    pygame.draw.rect(screen, WHITE, [positionP2[0], positionP2[1], WIDTH_PLAYER, HEIGHT_PLAYER])


def resetGame():
    global positionBall, ballSpeed
    print("Human: " + str(playerScore))
    print("Bot: " + str(botScore))
    positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    ballSpeed = [BALL_SPEED, BALL_SPEED]


def predictBotMove():
    if modelName != "model_ANN":
        sc = pygame.surfarray.array3d(screen)
        pred = bot.getMoveArray(format_array(sc))
        index = np.argmax(pred)
        return index
    else:
        return 0 # write here


def collectDatasets(images=False):
    global countDown, countUp, countStill
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and countUp < 5000:
        if images:
            pygame.image.save(screen, "Dataset/" + "u-" + str(countUp) + ".jpg")
        else:
            dataset_file.write(getDatasetFileName(0))
        countUp += 1

    elif keys[pygame.K_DOWN] and countDown < 5000:
        if images:
            pygame.image.save(screen, "Dataset/" + "d-" + str(countDown) + ".jpg")
        else:
            dataset_file.write(getDatasetFileName(1))
        countDown += 1

    elif countStill < 5000:
        if images:
            pygame.image.save(screen, "Dataset/" + "s-" + str(countStill) + ".jpg")
        else:
            dataset_file.write(getDatasetFileName(2))
        countStill += 1


def getDatasetFileName(label):
    s = (str(ballSpeed[0]) + "," + str(ballSpeed[1]) + "," + str(positionBall[0]) + "," + str(positionBall[1])
        + "," + str(positionP2[1]) + "," + str(label) + "\n")
    return s


def updateBallPosition():
    global positionBall
    positionBall[0] += ballSpeed[0]
    positionBall[1] += ballSpeed[1]


def updatePlayerPosition():
    global positionP1, positionP2
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and positionP1[1] >= 0:
        positionP1[1] -= PLAYER_SPEED
    elif keys[pygame.K_s] and positionP1[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
        positionP1[1] += PLAYER_SPEED

    if keys[pygame.K_UP] and positionP2[1] >= 0:
        positionP2[1] -= PLAYER_SPEED

    elif keys[pygame.K_DOWN] and positionP2[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
        positionP2[1] += PLAYER_SPEED


def updateBotPosition():
    global positionP2
    botChoice = predictBotMove()
    if botChoice == 0:
        print("UP")
        if positionP2[1] >= 0:
            positionP2[1] -= PLAYER_SPEED
    elif botChoice == 1:
        print("DOWN")
        if positionP2[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
            positionP2[1] += PLAYER_SPEED
    elif botChoice == 2:
        print("STAY")


def ballCollisionOnWalls():
    global ballSpeed, botScore, playerScore
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


def ballCollisionOnPaddles():
    global ballSpeed
    if positionBall[0] - BALL_RADIUS <= positionP1[0] and positionBall[1] >= positionP1[1] - 5 and positionBall[1] <= positionP1[1] + HEIGHT_PLAYER + 5:
        ballSpeed[0] = -ballSpeed[0]

    if positionBall[0] + BALL_RADIUS >= positionP2[0] and positionBall[1] >= positionP2[1] - 5 and positionBall[1] <= positionP2[1] + HEIGHT_PLAYER + 5:
        ballSpeed[0] = -ballSpeed[0]


modelName = str(input("Select model: ANN, CNN, or RNN: "))
bot = Bot("bot_" + modelName + ".model")

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

np.set_printoptions(threshold=np.inf)

countUp = 0
countDown = 0
countStill = 0

playerScore = 0
botScore = 0
positionP1 = [35, 230]
positionP2 = [SCREEN_WIDTH - 35, 230]
ballSpeed = [BALL_SPEED, BALL_SPEED]
positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]

dataset_file = open("dataset.txt", "a")

while True:
    render()
    updateBallPosition()
    updatePlayerPosition()
    updateBotPosition()
    ballCollisionOnWalls()
    ballCollisionOnPaddles()

    collectDatasets()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dataset_file.close()
            pygame.quit()
            sys.exit()
            print("countUp is at: " + str(countUp))
            print("countDown is at: " + str(countDown))
            print("countStill is at: " + countStill)

    pygame.time.Clock().tick(100)
    pygame.display.flip()   # update screen
