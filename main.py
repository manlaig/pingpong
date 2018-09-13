import pygame, sys, random, math
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WIDTH_PLAYER = 50
PLAYER_SPEED = 10


def drawAll(screen):
    screen.fill((0, 0, 0))


def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsController = pygame.time.Clock()
    positionP1 = 230
    positionP2 = 230
    ballSpeed = 4
    positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    ballAngle = random.random() + 1
    print("Angle is: ", ballAngle)
    while True:
        drawAll(screen)
        ball = pygame.draw.circle(screen, (255, 255, 255), positionBall, 10)
        player1 = pygame.draw.rect(screen, (255, 255, 255), [15, positionP1, 10, WIDTH_PLAYER])
        player2 = pygame.draw.rect(screen, (255, 255, 255), [SCREEN_WIDTH - 22, positionP2, 10, WIDTH_PLAYER])

        #positionBall[0] += int(ballSpeed * math.cos(ballAngle))
        #positionBall[1] += int(ballSpeed * math.sin(ballAngle))

        if positionBall[0] + 10 >= 500:
            ballSpeed = -4
            ballAngle = math.degrees(ballAngle) * 2
        if positionBall[0] - 10 <= 0:
            ballSpeed = 4
            ballAngle = math.degrees(ballAngle) * 2
        if positionBall[1] + 10 >= 500:
            ballSpeed = -4
            ballAngle = math.degrees(ballAngle) * 2
        if positionBall[1] - 10 <= 0:
            ballSpeed = 4
            ballAngle = math.degrees(ballAngle) * 2
        if positionBall[1] == positionP1 - 40 and positionBall[1] == positionP1 and positionBall[0] - 10 == 25:
            ballSpeed = 4
            ballAngle = math.degrees(ballAngle) * 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if positionP1 >= 0:
                positionP1 -= PLAYER_SPEED
        if keys[pygame.K_s]:
            if positionP1 + 40 <= SCREEN_HEIGHT:
                positionP1 += PLAYER_SPEED
        if keys[pygame.K_UP]:
            if positionP2 >= 0:
                positionP2 -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            if positionP2 + 40 <= SCREEN_HEIGHT:
                positionP2 += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            ballAngle = random.random() + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsController.tick(100)


main()
