class Car:

  def move(self):
    print("The car drives under the speed limit.")


class Boat:

  def move(self):
    print("The boat sails to the ocean")


class Drone:

  def move(self):
    print("The drone flies High")


def start_trip(vehicle):
  vehicle.move()


car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)