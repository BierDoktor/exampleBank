# Superclass (Base Class)
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health is now {self.health}")

    def is_alive(self):
        return self.health > 0

# Derived Class (Inheriting from Character without additional constructor)
class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword!")

# Derived Class (Inheriting from Character and adding new fields)
class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)  # Calling the superclass constructor
        self.mana = mana  # New field specific to Mage

    def cast_spell(self):
        if self.mana > 0:
            print(f"{self.name} casts a fireball!")
            self.mana -= 10
        else:
            print(f"{self.name} is out of mana!")

# Example usage:
warrior = Warrior("Thor", 100)
mage = Mage("Merlin", 80, 50)

warrior.attack()
mage.cast_spell()
mage.take_damage(30)
print(f"Is {mage.name} alive? {mage.is_alive()}")
print(warrior.is_alive())
