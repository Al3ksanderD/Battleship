import pygame

# constant values
WIDTH = SQ_SIZE * 10 * 2
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
GREY = (40, 50, 60)
# initialize pygame
pygame.init()
pygame.display.set_caption("Battleship")

# main loop

animating = True
pausing = False
while animating:
    # track user interaction
    for event in pygame.event.get():
        # user closes window
        if event.type == pygame.QUIT:
            animating = False

        # key press
        if event.type == pygame.KEYDOWN:
            # escape to close
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar to pause and unpasue the animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing

        if not pausing:

            # draw background
            SCREEN.fill(GREY)

            # update screen
            pygame.display.flip()