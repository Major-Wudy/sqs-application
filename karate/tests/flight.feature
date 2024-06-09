Feature: Test POST /api/create/flight/

  Background:
    * url 'http://web:8000/api/create/flight/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Create flight - Valid input
    Given request { "passengers": 2, "legs": [{ "departure": "MUC", "destination": "DUB", "class": "premium" }], "distance_unit": "km" }
    When method post
    Then status 201
  
  Scenario: Create flight - Invalid passengers
    Given request { "passengers": "test", "legs": [{ "departure": "MUC", "destination": "DUB", "class": "premium" }], "distance_unit": "km" }
    When method post
    Then status 500

  Scenario: Create flight - Unauthorized
    Given request { "passengers": 2, "legs": [{ "departure": "MUC", "destination": "DUB", "class": "premium" }], "distance_unit": "km" }
    And header Authorization = ''
    When method post
    Then status 401
