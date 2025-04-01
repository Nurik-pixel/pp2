import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw walls
def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Generate food not on snake or walls
def generate_food(snake, walls):
    while True:
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        if pos not in snake and pos not in walls:
            value = random.randint(1, 3)  # random food weight
            return pos, value

# Generate temporary yellow food
def generate_temp_food(snake, walls):
    while True:
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        if pos not in snake and pos not in walls:
            value = random.randint(1, 5)
            timer = time.time()
            return pos, value, timer

# Function to draw food
def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw temporary yellow food
def draw_temp_food(food):
    pygame.draw.rect(screen, YELLOW, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw score and temporary food timer
def draw_ui(score, temp_timer):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    if temp_timer is not None:
        remaining = max(0, 5 - int(time.time() - temp_timer))
        timer_text = font.render(f"Timer: {remaining}", True, YELLOW)
        screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

# Game variables
snake = [[5, 5]]
direction = [1, 0]
food, food_value = generate_food(snake, [])
temp_food = None
temp_value = 0
temp_start_time = None
next_temp_food_score = 10
walls = []
score = 0
speed = 10  # base speed

# Game loop
running = True
while running:
    clock.tick(speed)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != [0, 1]:
        direction = [0, -1]
    elif keys[pygame.K_DOWN] and direction != [0, -1]:
        direction = [0, 1]
    elif keys[pygame.K_LEFT] and direction != [1, 0]:
        direction = [-1, 0]
    elif keys[pygame.K_RIGHT] and direction != [-1, 0]:
        direction = [1, 0]

    # Move the snake
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    # Check for wall or border collision
    if (new_head in snake or
        new_head in walls or
        not 0 <= new_head[0] < COLS or
        not 0 <= new_head[1] < ROWS):
        running = False  # Game over

    snake.insert(0, new_head)

    # Check food collision
    if new_head == food:
        score += food_value
        food, food_value = generate_food(snake, walls)
        if score >= next_temp_food_score:
            if temp_food is None:
                temp_food, temp_value, temp_start_time = generate_temp_food(snake, walls)
                next_temp_food_score += 10
    elif temp_food and new_head == temp_food:
        score += temp_value
        temp_food = None
        temp_value = 0
        temp_start_time = None
    else:
        if len(snake) > score + 1:
            snake.pop()

    # Check if temporary food expired
    if temp_food and time.time() - temp_start_time > 5:
        temp_food = None
        temp_value = 0
        temp_start_time = None

    # Draw everything
    draw_snake(snake)
    draw_food(food)
    if temp_food:
        draw_temp_food(temp_food)
    draw_walls(walls)
    draw_ui(score, temp_start_time)

    pygame.display.flip()


pygame.quit()