class FuelSourceType:
    types = [{'name':'Bituminous Coal', 'api_name': 'bit', 'unit': 'short_ton'},
             {'name':'Home Heating and Diesel Fuel (Distillate)', 'api_name':'dfo', 'unit':'gallon'},
             {'name':'Jet Fuel', 'api_name':'jf','unit':'gallon'},
             {'name':'Kerosene', 'api_name':'ker','unit':'gallon'},
             {'name':'Lignite Coal', 'api_name':'lig','unit':'short_ton'},
             {'name':'Municipal Solid Waste', 'api_name':'msw','unit':'short_ton'},
             {'name':'Natural Gas', 'api_name':'ng','unit':'thousand_cubic_feet'},
             {'name':'Petroleum Coke', 'api_name':'pc','unit':'gallon'},
             {'name':'Propane Gas', 'api_name':'pg','unit':'gallon'},
             {'name':'Residual Fuel Oil', 'api_name':'rfo','unit':'gallon'},
             {'name':'Subbituminous Coal', 'api_name':'sub','unit':'short_ton'},
             {'name':'Tire-Derived Fuel', 'api_name':'tdf','unit':'short_ton'},
             {'name':'Waste Oil', 'api_name':'wo','unit':'barrel'},
             ]

    @classmethod
    def getApiNameByName(cls, name: str) -> str:
        try:
            if not isinstance(name, str):
                raise TypeError()
            for fuel_type in cls.types:
                if fuel_type['name'] == name:
                    return fuel_type['api_name']
            return ''
        except TypeError:
            print("name parameter must be a string")
            return ''