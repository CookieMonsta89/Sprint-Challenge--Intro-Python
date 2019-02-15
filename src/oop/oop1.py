# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v

class Vehicle:                       #    <===== BASE CLASS
    def __init__(self, name):
        self.name = name

class FlightVehicle(Vehicle):        #    <===== SUBCLASS to BASE CLASS => VEHICLE
    def __init__(self, name, year_built):
        super().__init__(name, 1943)
        self.year_built = year_built


class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(self, name, 2044)      #         <===== SUBCLASS to SUBCLASS => FLIGHTVEHICLE


class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(self, name, 1902)
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
class GroundVehicle:
    def __init__(self, name, wheels):

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
