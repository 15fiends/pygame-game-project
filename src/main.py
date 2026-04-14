import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake: Power-Up Chaos")

clock = pygame.time.Clock()
BLOCK_SIZE = 20

font = pygame.font.SysFont(None, 36)


def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


class Food:
    def __init__(self, snake):
        self.type = random.choice(["normal", "speed", "danger"])
        self.position = self.generate_position(snake)

    def generate_position(self, snake):
        while True:
            pos = (
                random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE)
            )
            if pos not in snake:
                return pos

    def draw(self):
        if self.type == "normal":
            color = (255, 0, 0)
        elif self.type == "speed":
            color = (255, 255, 0)
        else:
            color = (128, 0, 128)

        pygame.draw.rect(screen, color, (*self.position, BLOCK_SIZE, BLOCK_SIZE))


def reset_game():
    snake = [(300, 300)]
    direction = (BLOCK_SIZE, 0)
    foods = [Food(snake) for _ in range(3)]
    speed = 10
    game_over = False
    return snake, direction, foods, speed, game_over


snake, direction, foods, speed, game_over = reset_game()
running = True


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_w and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                if event.key == pygame.K_s and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                if event.key == pygame.K_a and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                if event.key == pygame.K_d and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

            if game_over and event.key == pygame.K_r:
                snake, direction, foods, speed, game_over = reset_game()

    if not game_over:
        previous_length = len(snake)
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            game_over = True

        if new_head in snake:
            game_over = True

        if not game_over:
            snake.insert(0, new_head)
            segments_to_remove = 1

            for food in foods[:]:
                if new_head == food.position:
                    if food.type in ["normal", "speed"]:
                        segments_to_remove = 0

                        if food.type == "speed":
                            speed += 2
                    elif food.type == "danger":
                        if previous_length == 1:
                            game_over = True
                        else:
                            segments_to_remove = 2

                    foods.remove(food)
                    foods.append(Food(snake))
                    break

            for _ in range(segments_to_remove):
                if snake:
                    snake.pop()

        if len(snake) < 1:
            game_over = True

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))

    for food in foods:
        food.draw()

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT), 5)

    score = len(snake)
    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 20)
        draw_text("Press R to Restart", WIDTH // 2 - 150, HEIGHT // 2 + 20)

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
