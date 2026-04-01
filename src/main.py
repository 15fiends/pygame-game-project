import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Grid size
BLOCK_SIZE = 20

# Snake
snake = [(300, 300)]
direction = (BLOCK_SIZE, 0)

# Food
food = (random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE))

running = True
while running:
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = (0, -BLOCK_SIZE)
            if event.key == pygame.K_s:
                direction = (0, BLOCK_SIZE)
            if event.key == pygame.K_a:
                direction = (-BLOCK_SIZE, 0)
            if event.key == pygame.K_d:
                direction = (BLOCK_SIZE, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)

    # Check food collision
    if new_head == food:
        food = (random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE))
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()