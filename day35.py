#Implement a class for a simple game character.
print ("\nWilson - Day 35 of #100DaysOfCode\n")
print("\nclass for a simple game character\n")

class GameCharacter:
  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage

  def attack(self, other_character):
    print(f"{self.name} is attacking {other_character.name}")
    other_character.take_damage(self.damage)

  def take_damage(self, damage):
    self.health -= damage
    print(f"{self.name} took {damage} damage")

    if self.health <= 0:
      print(f"{self.name} lost")
  
  def display_status(self):
    print(f"{self.name} health = {self.health}")

def game_example():
  player = GameCharacter(name="reyna", health=120, damage=20)
  enemy = GameCharacter(name="raze", health=120,damage=25)

  player.display_status()
  enemy.display_status()

  player.attack(enemy)

  player.display_status()
  enemy.display_status()

game_example()
  
