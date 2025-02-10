# Superclass (Base class)
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! Health left: {self.health}")

# Derived class without calling superclass constructor
class Mage(Character):
    pass  # No new fields, just inherits everything from Character

# Derived class with new fields and calling the superclass constructor
class Warrior(Character):
    def __init__(self, name, health, armor):
        super().__init__(name, health)  # Calling superclass constructor
        self.armor = armor  # New field unique to Warrior

    def take_damage(self, damage):
        reduced_damage = max(0, damage - self.armor)  # Armor reduces damage
        super().take_damage(reduced_damage)

# Creating instances of both the superclass and subclasses
char1 = Character("Villager", 100)
char2 = Mage("Wizard", 80)  # No extra fields, just a Mage instance
char3 = Warrior("Knight", 120, 10)  # New field: armor

# Demonstrating behavior
char1.take_damage(20)  # Regular damage
char2.take_damage(30)  # Inherits Character's behavior
char3.take_damage(30)  # Reduced damage due to armor
