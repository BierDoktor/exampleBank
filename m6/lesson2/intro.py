import pygame
import random
import time

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE, BLUE, RED, BLACK = (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 0, 0)
font = pygame.font.Font(None, 36)
text = font.render("Duel Game", True, WHITE)
clock = pygame.time.Clock()

# List of characters
characters = ["Warrior", "Mage"]

# Sorting (alphabetical order of characters)
characters.sort()
print("Available characters:", characters)

# Defining a base class for fighters
class Fighter:
    def __init__(self, name, health, attack_power, color, x, y):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.color = color
        self.rect = pygame.Rect(x, y, 100, 100)

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        return f"{self.name} attacks {opponent.name} for {damage} damage!"

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        health_text = font.render(f"{self.name}: {self.health} HP", True, WHITE)
        screen.blit(health_text, (self.rect.x, self.rect.y - 20))

# Creating Warrior and Mage
warrior = Fighter("Warrior", 100, 20, RED, 100, 150)
mage = Fighter("Mage", 80, 25, BLUE, 400, 150)

# Battle log using a list
battle_log = []

# Game loop
running = True

while running:
    screen.fill(BLACK)
    
    pressed = pygame.key.get_pressed()

    # Press Space to attack
    if pressed[pygame.K_SPACE]:
        attacker = random.choice([warrior, mage])
        defender = mage if attacker == warrior else warrior
        battle_log.append(attacker.attack(defender))
        time.sleep(0.1)

        # Remove from the list if defeated
        if defender.health <= 0:
            battle_log.append(f"{defender.name} has been defeated!")
            running = False  # End game

    # Display characters
    warrior.draw()
    mage.draw()

    # Display battle log
    font = pygame.font.Font(None, 24)
    for i, log in enumerate(battle_log[-5:]):  # Show last 5 log entries
        log_text = font.render(log, True, WHITE)
        screen.blit(log_text, (50, 300 + i * 20))
    
    pygame.display.update()
    clock.tick(60)

# Print battle log after the game ends
print("\nBattle Log:")
for log in battle_log:
    print(log)
