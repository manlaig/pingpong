import pygame, sys, random, math
width = 500
height = 500


def drawAll(screen):
    screen.fill((56, 142, 60))
    pygame.draw.circle(screen, (255, 255, 255), [int(width/2), int(height/2)], 50, 3)  # halfcourt circle
    pygame.draw.line(screen, (255, 255, 255), (int(width/2), 0), (int(width/2), height), 3)  # halfcourt line
    # pygame.draw.rect(screen, (255, 255, 255), [0, 0, width, height], 10)  # border
    # pygame.draw.rect(screen, (56, 142, 60), [0, 200, 10, 100])
    # pygame.draw.rect(screen, (56, 142, 60), [0, 0, 10, height])
    # pygame.draw.rect(screen, (56, 142, 60), [widht - 10, 200, 10, 100])
    # pygame.draw.rect(screen, (56, 142, 60), [width - 10, 0, 10, height])


def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((width, height))
    fpsController = pygame.time.Clock()
    positionP1 = 230
    positionP2 = 230
    ballSpeed = 4
    positionBall = [int(width/2), int(height/2)]
    ballAngle = random.random() * 350 + 10

    while True:
        drawAll(screen)
        ball = pygame.draw.circle(screen, (255, 0, 0), positionBall, 10)
        player1 = pygame.draw.rect(screen, (0, 0, 255), [15, positionP1, 10, 40])
        player2 = pygame.draw.rect(screen, (0, 0, 255), [width - 22, positionP2, 10, 40])

        positionBall[0] += ballSpeed * math.ceil(math.sin(math.radians(ballAngle)))
        positionBall[1] += ballSpeed * math.ceil(math.cos(math.radians(ballAngle)))

        if positionBall[0] >= 500:
            ballSpeed = -4
        if positionBall[0] <= 0:
            ballSpeed = 4
        if positionBall[1] >= 500:
            ballSpeed = -4
        if positionBall[1] <= 0:
            ballSpeed = 4

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if positionP1 >= 0:
                positionP1 -= 5
        if keys[pygame.K_s]:
            if positionP1 + 40 <= height:
                positionP1 += 5
        if keys[pygame.K_UP]:
            if positionP2 >= 0:
                positionP2 -= 5
        if keys[pygame.K_DOWN]:
            if positionP2 + 40 <= height:
                positionP2 += 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsController.tick(100)


main()
