import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

WHITE, BLUE = (255, 255, 255), (0, 0, 255)
font = pygame.font.Font(None, 36)
text = font.render("Use arrow keys to move!", True, WHITE)
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_UP]: self.rect.y -= 5
        if keys[pygame.K_DOWN]: self.rect.y += 5

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

player = Player()
running = True

while running:
    screen.fill(BLUE)
    screen.blit(text, (WIDTH // 2 - 100, 50))
    
    player.move(pygame.key.get_pressed())
    player.draw()
    
    pygame.display.update()
    clock.tick(60)
