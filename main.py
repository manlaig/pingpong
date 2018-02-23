import pygame, sys
import pygame.gfxdraw

width = 800
height = 500

def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((width, height))
    fpsController = pygame.time.Clock()
    #screen.fill(pygame.Color(0, 0, 0))
    ATOM_IMG = pygame.Surface((30, 30), pygame.SRCALPHA)

    while(True):
        pygame.draw.circle(screen, (255,255,255), [400, 250], 50, 3)
        pygame.draw.line(screen, (255,255,255), (400,0), (400,500), 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball = pygame.draw.circle(screen, (255, 0, 0), [400, 250], 10)
        player1 = pygame.draw.rect(screen, (0,255,0), [0,250, 5, 50])
        player2 = pygame.draw.rect(screen, (0,0,255), [790,250, 5, 50])

        pygame.display.flip()

main()
