# hero.py

from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    # We know the name of our hero, so we assign it here
    # Similarly, our starting health is passed in, just like name
    # When a hero is created, their current health is
    # Always the same as their starting health (no damage taken yet!)
  
    

    def __init__(self, name, starting_health=100):
       
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
        
    def defend(self):
        total_damage = 0
        for armor in self.armors:
            total_damage -= armor.defend()
        return total_damage
        
    def battle(self, opponent):
        if self.abilities == []:
            print("Draw")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                opponent.take_damage(self.attack())
                if opponent.current_health <= 0:
                    print(f"{self.name} won!")
                    return


        


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)