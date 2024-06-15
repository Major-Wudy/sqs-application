Feature: Test POST /api/get/estimate/fuel/

  Background:
    * url 'http://web:8000/api/estimate/fuel/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Get fuel estimate - Successful request
    Given request {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": "500.00"}
    When method POST
    Then status 201

  Scenario: Get fuel estimate - Attempt GET request
    Given request {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": "500.00"}
    When method GET
    Then status 405

  Scenario: Invalid request - Missing required fields
    Given request {}
    When method POST
    Then status 500

  Scenario: Unauthorized request - Missing or invalid token
    Given request {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": "500.00"}
    And header Authorization = 'Bearer invalid-token'
    When method POST
    Then status 401