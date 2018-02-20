import pygame, sys

def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((720, 480))
    fpsController = pygame.time.Clock()
    while(True):
        screen.fill(pygame.Color(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

main()