import pygame

# constant values
SQ_SIZE = 40
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 250, 250)
GREY = (40, 50, 60)
# initialize pygame
pygame.init()
pygame.display.set_caption("Battleship")

# Functions

# Function to draw a grid
def draw_grid(left = 0, top = 0):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width= 3)



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
            # draw search grid
            # Docelowo chcę to zrobić tak żeby
            # zasłaniało pola gracza który aktualnie
            # jest nieaktywny, żeby aktywny gracz nie
            # mógł podejrzeć położenia jego statków
            
            draw_grid()
            draw_grid(left=(WIDTH-H_MARGIN)//2 + H_MARGIN, top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)

            # draw position grids
            draw_grid(left=(WIDTH-H_MARGIN)//2 + H_MARGIN)
            draw_grid(top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)
            # update screen
            pygame.display.flip()