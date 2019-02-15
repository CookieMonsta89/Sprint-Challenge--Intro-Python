# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v

class Vehicle:                       #    <===== BASE CLASS
    def __init__(self, name, level):
        self.name = name
        self.type = level 

class FlightVehicle(Vehicle):        #    <===== SUBCLASS to BASE CLASS => VEHICLE
    def __init__(self):
        super().__init__(name, level)
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
