import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font for score and lives
default_font = pygame.font.Font(None, 36)

# Base class
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Derived class - Player
class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, BLUE)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

# Derived class - Enemy
class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, RED)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

# Create instances
player = Player(WIDTH//2, HEIGHT - 60)
enemies = [Enemy(random.randint(0, WIDTH-40), random.randint(0, HEIGHT//2)) for _ in range(5)]

# Scoring system
score = 0
lives = 3

def draw_score_lives():
    score_text = default_font.render(f"Score: {score}", True, BLACK)
    lives_text = default_font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

# Game loop
running = True

while running:
    pygame.time.delay(30)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    for enemy in enemies:
        enemy.move()

        if player.get_rect().colliderect(enemy.get_rect()):
            score += 1
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - enemy.width)
        elif enemy.y > HEIGHT:  # Enemy reached bottom
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - enemy.width)
            
            # Correctly reference global lives
            lives -= 1

            if lives == 0:
                running = False

        enemy.draw(screen)
    
    player.draw(screen)
    draw_score_lives()
    pygame.display.update()

pygame.quit()

# Development Checklist:
# - [] Create a game window
# - [] Implement a base class for game objects
# - [] Implement a player class with movement
# - [] Implement enemy objects with movement
# - [] Add collision detection
# - [] Add scoring system
# - [] Add lives system with game over condition