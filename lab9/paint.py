import pygame
import sys
import math

pygame.init()

# Setup the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Color palette shortcuts using number keys
COLOR_PALETTE = {
    pygame.K_1: BLACK,
    pygame.K_2: (255, 0, 0),
    pygame.K_3: (0, 255, 0),
    pygame.K_4: (0, 0, 255),
    pygame.K_5: (255, 255, 0),
}

# Starting settings
clock = pygame.time.Clock()
screen.fill(WHITE)
drawing = False
tool = "line"      
color = BLACK      
start_pos = (0, 0)
current_pos = (0, 0)
ERASER_SIZE = 20
background = screen.copy()  # saves whats drawn

# Set font
font = pygame.font.SysFont("arial", 26)

# Function to draw tool help text in the corner
def draw_ui():
    lines = [
        "L - Line",
        "R - Rectangle",
        "S - Square",
        "T - Right Triangle",
        "Y - Equilateral Triangle",
        "H - Rhombus",
        "C - Circle",
        "E - Eraser",
        "1-5: Colors"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, 10 + i * 30))  # space out lines vertically

# Function to draw the shapes
def draw_shape(tool, start, end, color):
    if tool == "rect":
        #rectangle
        rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                            abs(end[0] - start[0]), abs(end[1] - start[1]))
        pygame.draw.rect(screen, color, rect, 2)

    elif tool == "circle":
        # calculate radius
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start, radius, 2)

    elif tool == "square":
        # make width and height to be equal
        size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], size, size)
        pygame.draw.rect(screen, color, rect, 2)

    elif tool == "right_triangle":
        # right angled triangle
        points = [start, (start[0], end[1]), end]
        pygame.draw.polygon(screen, color, points, 2)

    elif tool == "equilateral_triangle":
        base_length = abs(end[0] - start[0])
        height = base_length * math.sqrt(3) / 2
        if end[1] < start[1]:
            tip = (start[0] + base_length // 2, start[1] - height)
        else:
            tip = (start[0] + base_length // 2, start[1] + height)
        points = [start, (start[0] + base_length, start[1]), tip]
        pygame.draw.polygon(screen, color, points, 2)

    elif tool == "rhombus":
        # diamond shape, centered between start and end
        center_x = (start[0] + end[0]) // 2
        center_y = (start[1] + end[1]) // 2
        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2
        points = [
            (center_x, start[1]),
            (end[0], center_y),
            (center_x, end[1]),
            (start[0], center_y)
        ]
        pygame.draw.polygon(screen, color, points, 2)

    elif tool == "line":
        # simple line from start to end
        pygame.draw.line(screen, color, start, end, 2)

# Game loop
while True:
    #show preview for shape tools
    if tool not in ["line", "eraser"]:
        screen.blit(background, (0, 0))  # reset the screen before preview

    draw_ui()  # draw tool instructions

    # while dragging, show the preview
    if drawing and tool not in ["line", "eraser"]:
        draw_shape(tool, start_pos, current_pos, color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                current_pos = event.pos
                drawing = True
                background = screen.copy()  # save current canvas
                if tool == "line":
                    pygame.draw.circle(screen, color, event.pos, 2)  # tiny dot at start

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                if tool == "line":
                    # draw free-hand line by drawing small lines between positions
                    pygame.draw.line(screen, color, start_pos, current_pos, 3)
                    start_pos = current_pos
                elif tool == "eraser":
                    # erase by drawing white squares
                    pygame.draw.rect(screen, WHITE,
                                     (current_pos[0] - ERASER_SIZE // 2,
                                      current_pos[1] - ERASER_SIZE // 2,
                                      ERASER_SIZE, ERASER_SIZE))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool not in ["line", "eraser"]:
                    draw_shape(tool, start_pos, end_pos, color)  # finalize shape
                    background = screen.copy()  # update saved canvas
            drawing = False

        elif event.type == pygame.KEYDOWN:
            # Tool shortcuts
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_y:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"
            elif event.key in COLOR_PALETTE:
                color = COLOR_PALETTE[event.key]

    pygame.display.update()
    clock.tick(60)
