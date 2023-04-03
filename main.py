import pygame
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

PADDLE_WIDTH, PADDLE_HEIGHT = 200, 20
PADDLE_VEL = 5

BRICK_WIDTH, BRICK_HEIGHT = 100, 50

BALL_RADIUS = 10


def draw_window(paddle, bricks, ball):
    WIN.fill("cyan")

    pygame.draw.rect(WIN, "red", paddle)

    for row in bricks:
        for brick in row:
            pygame.draw.rect(WIN, "blue", brick)

    pygame.draw.circle(WIN, "white", (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    paddle = pygame.rect.Rect(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
    x_pos = paddle.x

    ball = pygame.rect.Rect(WIDTH / 2 - BALL_RADIUS, 450, 2 * BALL_RADIUS, 2 * BALL_RADIUS)
    ball_y_vel = 5
    #ball_x_vel = random.random() * random.randint(-10, 10)
    ball_x_vel = 1

    bricks = []
    for row_num in range(4):
        row = []
        for brick_num in range(10):
            row.append(
                pygame.rect.Rect(
                    brick_num * BRICK_WIDTH + 1, row_num * BRICK_HEIGHT + 1, BRICK_WIDTH - 2, BRICK_HEIGHT - 2))
        bricks.append(row)
    while run:
        clock.tick(60)
        # Checks for user closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Moves paddle to mouse position
        mouse_vel = pygame.mouse.get_pos()[0] - x_pos
        x_pos = pygame.mouse.get_pos()[0]

        if PADDLE_WIDTH / 2 < x_pos < WIDTH - PADDLE_WIDTH / 2:
            paddle.x = x_pos - PADDLE_WIDTH / 2
        elif x_pos < PADDLE_WIDTH / 2:
            paddle.x = 0
        else:
            paddle.x = WIDTH - PADDLE_WIDTH

        # Checks for collisions
        # Paddle collisions
        if pygame.Rect.colliderect(paddle, ball):
            ball_y_vel *= -1
            ball_x_vel -= mouse_vel
            ball_x_vel *= -0.2
        # Edge collisions
        if ball.y + ball_y_vel < 0:
            ball_y_vel *= -1
            ball.y = 0
        if ball.x + ball_x_vel < 0 or ball.x + ball_x_vel + 2 * BALL_RADIUS > WIDTH:
            ball_x_vel *= -1
            ball.x += ball_x_vel
        else:
            ball.x += ball_x_vel
        # Check for brick collisions
        for row in bricks:
            if pygame.Rect.collidelist(ball, row) == -1:
                continue
            row.pop(pygame.Rect.collidelist(ball, row))
            ball_y_vel *= -1

        ball.y += ball_y_vel

        draw_window(paddle, bricks, ball)

    pygame.quit()


if __name__ == "__main__":
    main()
