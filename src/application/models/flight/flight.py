class Flight:
    def __init__(self, type, passengers, leg, distance_unit):
        try:
            self.type = type
            self.passengers = passengers
            self.leg = leg
            self.distance_unit = distance_unit
        except Exception as ex:
            print(ex)