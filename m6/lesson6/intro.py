import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Font
default_font = pygame.font.Font(None, 36)

# Paddle class
class Paddle:
    def __init__(self):
        self.width = 80
        self.height = 10
        self.x = (width - self.width) // 2
        self.y = height - 40
        self.speed = 6
        self.color = blue

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < width - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Ball class
class Ball:
    def __init__(self):
        self.radius = 8
        self.x = width // 2
        self.y = height // 2
        self.dx = random.choice([-3, 3])
        self.dy = -3
        self.color = red

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Wall collisions
        if self.x <= 0 or self.x >= width - self.radius * 2:
            self.dx *= -1
            
        if self.y <= 0:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

# Brick class
class Brick:
    def __init__(self, x, y):
        self.width = 50
        self.height = 20
        self.x = x
        self.y = y
        self.color = green
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Create game objects
paddle = Paddle()
ball = Ball()
bricks = [Brick(x * 55 + 10, y * 25 + 50) for x in range(1) for y in range(1)]
score = 0

# Game loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.move(keys)
    ball.move()

    # Ball collision with paddle
    if ball.get_rect().colliderect(paddle.get_rect()):
        ball.dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if brick.active and ball.get_rect().colliderect(brick.get_rect()):
            brick.active = False
            ball.dy *= -1
            score += 1

    # Check if all bricks are destroyed
    if all(not brick.active for brick in bricks):
        running = False  # Game over when all bricks are destroyed

    # Ball falls below paddle
    if ball.y > height:
        running = False  # Game over

    # Draw objects
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    # Display score
    score_text = default_font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
