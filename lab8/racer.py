import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Load images
car_image = pygame.image.load("images/racer.png")
coin_image = pygame.image.load("images/coin.png")

# Scale images
car_image = pygame.transform.scale(car_image, (60, 40))
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Car properties
car_pos = [WIDTH // 2, HEIGHT // 2]
car_angle = 0
car_speed = 5

# Coin properties
def random_coin_pos():
    return [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]

coin_pos = random_coin_pos()

# Score
score = 0

# Main loop
running = True
while running:
    screen.fill((30, 30, 30))  # background color

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_angle += 5
    if keys[pygame.K_RIGHT]:
        car_angle -= 5
    if keys[pygame.K_UP]:
        car_pos[0] += car_speed * math.cos(math.radians(-car_angle))
        car_pos[1] += car_speed * math.sin(math.radians(-car_angle))
    if keys[pygame.K_DOWN]:
        car_pos[0] -= car_speed * math.cos(math.radians(-car_angle))
        car_pos[1] -= car_speed * math.sin(math.radians(-car_angle))

    # Draw coin
    screen.blit(coin_image, (coin_pos[0], coin_pos[1]))

    # Draw car with rotation
    rotated_car = pygame.transform.rotate(car_image, car_angle)
    car_rect = rotated_car.get_rect(center=(car_pos[0], car_pos[1]))
    screen.blit(rotated_car, car_rect.topleft)

    # Collision detection
    car_center = pygame.Vector2(car_pos)
    coin_center = pygame.Vector2(coin_pos[0] + 15, coin_pos[1] + 15)
    if car_center.distance_to(coin_center) < 40:
        score += 1
        coin_pos = random_coin_pos()

    # Draw score (top-right corner)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()