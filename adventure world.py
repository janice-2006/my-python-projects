import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Quest")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load assets
player_size = 40
player = pygame.Rect(100, 100, player_size, player_size)

# Enemy (Obstacles)
enemy_size = 40
enemies = [pygame.Rect(random.randint(200, WIDTH-50), random.randint(100, HEIGHT-50), enemy_size, enemy_size) for _ in range(5)]

# Treasure
treasure = pygame.Rect(random.randint(100, WIDTH-50), random.randint(100, HEIGHT-50), 30, 30)

# Movement speed
speed = 5

# Game loop
running = True
score = 0
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player_size:
        player.y += speed

    # Check for collision with treasure
    if player.colliderect(treasure):
        score += 1
        treasure.x = random.randint(100, WIDTH-50)
        treasure.y = random.randint(100, HEIGHT-50)

    # Check for collision with enemies
    for enemy in enemies:
        if player.colliderect(enemy):
            print("Game Over!")
            running = False
    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, treasure)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    pygame.display.update()

pygame.quit()

