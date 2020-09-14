# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class:
class Vehicle:
    pass

# GroundVehicle and Subclass:
class GroundVehicle(Vehicle):
    pass

class car(GroundVehicle):
    pass

# FlightVehicle and Subclass
class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class starship(FlightVehicle):
    pass
