# main

# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# all code by CUBE
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

from key_input import *
from renderer import *

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

WIDTH = 500
HEIGHT = 500
FPS = 30
BGCOLOR = WHITE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True

RENDERER = renderer(screen)
InputProcessor = input_processor()
load_config("key_config.json")

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # add any other events here (keys, mouse, etc.)
        InputProcessor.main(event)

    screen.fill(BGCOLOR)

    RENDERER.process_input(InputProcessor.getcharacter())
    RENDERER.main()
    # after drawing, flip the display
    pygame.display.flip()
