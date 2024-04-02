from DistanceUnit import *
from ActivityType import *
from Leg import *

class Flight:
    def __init__(self, type: ActivityType, passangers: int, leg: Leg, distance_unit: DistanceUnit):
        try:
            if not isinstance(type, ActivityType) or not isinstance(passangers, int) or not isinstance(leg, Leg) or not isinstance(distance_unit, DistanceUnit):
                raise TypeError()
            self.type = type
            self.passangers = passangers
            self.leg = leg
            self.distance_unit = distance_unit
        except TypeError:
            print("wrong parameter types")