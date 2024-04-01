print("--- Testing Electricity ---")
from Electricity import *

elec = Electricity(ActivityType.ELECTRICITY, ElectricityUnit.KWH, 100.5, "Germany", "Bavaria")
print(elec.type.name)
print(elec.electricity_unit.name)
print(elec.electricity_value)
print(elec.country)
print(elec.state)

print("--- Testing FuelSourceType ---")
from FuelSourceType import *

api_name = FuelSourceType.getApiNameByName("Waste Oil")
print(api_name)
with_error = FuelSourceType.getApiNameByName(1)
print(with_error)

print("--- Testing Leg ---")
from Leg import * 
leg = Leg('MUC', 'DUB', CabinClass.ECONOMY)
print(leg.destination_airport)
print(leg.depature_airport)
print(leg.cabin_class)
leg = Leg('MUC', 'DUB', '1')