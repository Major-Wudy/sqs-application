Feature: Test POST /api/create/shipping/

  Background:
    * url 'http://web:8000/api/create/shipping/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Create shipping - Valid input
    Given request {"weight_value": 123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}
    When method post
    Then status 201

  Scenario: Create shipping - Invalid input
    Given request {"weight_value": "test","weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}
    When method post
    Then status 500

  Scenario: Create shipping - Unauthorized
    Given request {"weight_value": 123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}
    And header Authorization = ''
    When method post
    Then status 401
