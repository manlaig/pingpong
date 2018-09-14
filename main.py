import pygame, sys, random, math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WIDTH_PLAYER = 15
HEIGHT_PLAYER = 75
PLAYER_SPEED = 10
BALL_RADIUS = 10
WHITE = (255, 255, 255)

def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    positionP1 = [35, 230]
    positionP2 = [SCREEN_WIDTH - 35, 230]
    ballSpeed = [3, 3]
    positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    
    # game loop
    while True:
        screen.fill((0, 0, 0))
        ball = pygame.draw.circle(screen, WHITE, positionBall, BALL_RADIUS)
        player1 = pygame.draw.rect(screen, WHITE, [positionP1[0], positionP1[1], WIDTH_PLAYER, HEIGHT_PLAYER])
        player2 = pygame.draw.rect(screen, WHITE, [positionP2[0], positionP2[1], WIDTH_PLAYER, HEIGHT_PLAYER])


        positionBall[0] += ballSpeed[0]
        positionBall[1] += ballSpeed[1]


        # ball collision check on the walls
        if positionBall[1] <= BALL_RADIUS:
            ballSpeed[1] = -ballSpeed[1]

        if positionBall[1] + BALL_RADIUS >= SCREEN_HEIGHT:
            ballSpeed[1] = -ballSpeed[1]

        if positionBall[0] <= BALL_RADIUS:
            ballSpeed[0] = -ballSpeed[0]

        if positionBall[0] + BALL_RADIUS >= SCREEN_WIDTH:
            ballSpeed[0] = -ballSpeed[0]

    
        # ball collison check on 2 paddles
        if positionBall[0] - BALL_RADIUS <= positionP1[0] and positionBall[1] >= positionP1[1] - 5 and positionBall[1] <= positionP1[1] + HEIGHT_PLAYER + 5:
            ballSpeed[0] = -ballSpeed[0]
     
        if positionBall[0] + BALL_RADIUS >= positionP2[0] and positionBall[1] >= positionP2[1] - 5 and positionBall[1] <= positionP2[1] + HEIGHT_PLAYER + 5:
            ballSpeed[0] = -ballSpeed[0]


        # checking user input to move the players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if positionP1[1] >= 0:
                positionP1[1] -= PLAYER_SPEED
        if keys[pygame.K_s]:
            if positionP1[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
                positionP1[1] += PLAYER_SPEED
        if keys[pygame.K_UP]:
            if positionP2[1] >= 0:
                positionP2[1] -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            if positionP2[1] + HEIGHT_PLAYER <= SCREEN_HEIGHT:
                positionP2[1] += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]

        #pygame.image.save(screen, "screenshot.jpeg")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()   # update display
        pygame.time.Clock().tick(60)    # 60 FPS


main()

