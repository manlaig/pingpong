import pygame, sys, random, math
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WIDTH_PLAYER = 15
HEIGHT_PLAYER = 75
PLAYER_SPEED = 10
BALL_RADIUS = 10

def ball_init(right):
    global positionBall, ballSpeed # these are vectors stored as lists
    positionBall = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ballSpeed = [horz,-vert]


def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsController = pygame.time.Clock()
    positionP1 = [35, 230]
    positionP2 = [SCREEN_WIDTH - 35, 230]
    ballSpeed = [3, 3]
    positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]
    
    while True:
        screen.fill((0, 0, 0))
        ball = pygame.draw.circle(screen, (255, 255, 255), positionBall, BALL_RADIUS)
        player1 = pygame.draw.rect(screen, (255, 255, 255), [positionP1[0], positionP1[1], WIDTH_PLAYER, HEIGHT_PLAYER])
        player2 = pygame.draw.rect(screen, (255, 255, 255), [positionP2[0], positionP2[1], WIDTH_PLAYER, HEIGHT_PLAYER])

        positionBall[0] += ballSpeed[0]
        positionBall[1] += ballSpeed[1]


        if positionBall[1] <= BALL_RADIUS:
            ballSpeed[1] = -ballSpeed[1]
        if positionBall[1] >= SCREEN_HEIGHT - BALL_RADIUS:
            ballSpeed[1] = -ballSpeed[1]
    
        #ball collison check on gutters or paddles
        if positionBall[0] - BALL_RADIUS <= positionP1[0] and int(positionBall[1]) in range(positionP1[1] - 5, positionP1[1] + HEIGHT_PLAYER + 5, 1):
            ballSpeed[0] = -ballSpeed[0]

        elif positionBall[0] - BALL_RADIUS <= 0:
            ballSpeed[0] = -ballSpeed[0]

        #elif int(positionBall[0]) <= BALL_RADIUS + WIDTH_PLAYER:
            #ball_init(True)
        
        if positionBall[0] + BALL_RADIUS >= positionP2[0] and int(positionBall[1]) in range(positionP2[1] - 5, positionP2[1] + HEIGHT_PLAYER + 5, 1):
            ballSpeed[0] = -ballSpeed[0]
        
        elif positionBall[0] + BALL_RADIUS >= SCREEN_WIDTH:
            ballSpeed[0] = -ballSpeed[0]

        #elif int(positionBall[0]) >= SCREEN_WIDTH - BALL_RADIUS - WIDTH_PLAYER:
            #ball_init(False)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if positionP1[1] >= 0:
                positionP1[1] -= PLAYER_SPEED
        if keys[pygame.K_s]:
            if positionP1[1] + 40 <= SCREEN_HEIGHT:
                positionP1[1] += PLAYER_SPEED
        if keys[pygame.K_UP]:
            if positionP2[1] >= 0:
                positionP2[1] -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            if positionP2[1] + 40 <= SCREEN_HEIGHT:
                positionP2[1] += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            positionBall = [int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsController.tick(100)


main()

