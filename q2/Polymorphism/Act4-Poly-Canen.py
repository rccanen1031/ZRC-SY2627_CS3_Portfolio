class HealthPotion:

  def use(self):
    print("You have regained 50 HP!")


class ManaPotion:

  def use(self):
    print("You have restored 30 MP!")


class SpeedBoost:

  def use(self):
    print("Your speed has increased for 15 seconds!")


def apply_item(item):
  item.use()


potions = [HealthPotion(), ManaPotion(), SpeedBoost()]

for item in potions:
  apply_item(item)