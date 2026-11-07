class Warrior:

  def special_move(self):
    print("Warrior swings his magical mihty sword!")


class Mage:

  def special_move(self):
    print("Mage casts a powerful magic spell!")


class Archer:

  def special_move(self):
    print("Archer shoots a precise arrow and bullseye!")


def perform_move(character):
  character.special_move()


characters = [Warrior(), Mage(), Archer()]

for character in characters:
  perform_move(character)