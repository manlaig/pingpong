import pygame, sys

width = 800
height = 500

def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((width, height))
    fpsController = pygame.time.Clock()
    positionP1 = 230
    positionP2 = 230

    while(True):
        screen.fill((56, 142, 60))
        pygame.draw.circle(screen, (255, 255, 255), [400, 250], 50, 3)
        pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 500), 3)
        pygame.draw.rect(screen, (255, 255, 255), [0, 0, 800, 500], 10)
        pygame.draw.rect(screen, (56, 142, 60), [0, 200, 10, 100])
        pygame.draw.rect(screen, (56, 142, 60), [790, 200, 10, 100])
        ball = pygame.draw.circle(screen, (255, 0, 0), [400, 250], 10)
        player1 = pygame.draw.rect(screen, (0, 0, 255), [15, positionP1, 10, 40])
        player2 = pygame.draw.rect(screen, (0, 0, 255), [778, positionP2, 10, 40])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            positionP1 -= 1
        if keys[pygame.K_s]:
            positionP1 += 1
        if keys[pygame.K_UP]:
            positionP2 -= 1
        if keys[pygame.K_DOWN]:
            positionP2 += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsController.tick(200)

main()
