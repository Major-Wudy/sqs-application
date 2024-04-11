from strenum import StrEnum

class ActivityType(StrEnum):
    ELECTRICITY = 'electricity'
    FLIGHT = 'flight'
    VEHICLE = 'vehicle'
    SHIPPING = 'shipping'
    FUEL_COMBUSTION = 'fuel_combustion'