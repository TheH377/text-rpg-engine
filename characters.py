class Character:
    """Base class for all characters in the game"""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def is_alive(self):
        """Checks if the character is alive"""
        return self.health > 0

    def take_damage(self, amount):
        """Deals damage to the character"""
        self.health -= amount
        if self.health < 0:
            self.health = 0

class Player(Character):
    """Player class (inherits from Character and adds an inventory)"""
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.inventory = []

    def show_status(self):
        print(f"\n--- Status: {self.name} ---")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

class Enemy(Character):
    """Enemy class"""
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)