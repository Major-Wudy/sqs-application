import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.electricity import electricity
print("--- Testing Electricity ---")

elec = electricity(ActivityType.ELECTRICITY, ElectricityUnit.KWH, 100.5, "Germany", "Bavaria")
print(elec.type.name)
print(elec.electricity_unit.name)
print(elec.electricity_value)
print(elec.country)
print(elec.state)

"""
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

from IATAAirport import *
link = IATAAirport.getIATAAirportUrl()
print(link)
"""