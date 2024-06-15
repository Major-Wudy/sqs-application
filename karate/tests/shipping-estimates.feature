Feature: Test POST /api/get/estimate/shipping/

  Background:
    * url 'http://web:8000/api/estimate/shipping/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Get shipping estimate - Successful request
    Given request {"type": "shipping","weight_value": "123.45","weight_unit": "g","distance_value": "500.01","distance_unit": "km","transport_method": "plane"}
    When method POST
    Then status 201

  Scenario: Get shipping estimate - Attempt GET request
    Given request {"type": "shipping","weight_value": "123.45","weight_unit": "g","distance_value": "500.01","distance_unit": "km","transport_method": "plane"}
    When method GET
    Then status 405

  Scenario: Invalid request - Missing required fields
    Given request {}
    When method POST
    Then status 500

  Scenario: Unauthorized request - Missing or invalid token
    Given request {"type": "shipping","weight_value": "123.45","weight_unit": "g","distance_value": "500.01","distance_unit": "km","transport_method": "plane"}
    And header Authorization = 'Bearer invalid-token'
    When method POST
    Then status 401