Feature: Test POST /api/get/estimate/electricity/

  Background:
    * url 'http://web:8000/api/estimate/electricity/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Get electricity estimate - Successful request
    Given request { type: 'electricity', electricity_unit: 'kwh', electricity_value: 123.45, country: 'us', state: 'fl' }
    When method POST
    Then status 201

  Scenario: Get electricity estimate - Attempt GET request
    Given request { type: 'electricity', electricity_unit: 'kwh', electricity_value: 123.45, country: 'us', state: 'fl' }
    When method GET
    Then status 405

  Scenario: Invalid request - Missing required fields
    Given request {}
    When method POST
    Then status 500

  Scenario: Unauthorized request - Missing or invalid token
    Given request { type: 'electricity', electricity_unit: 'kwh', electricity_value: 123.45, country: 'us', state: 'fl' }
    And header Authorization = 'Bearer invalid-token'
    When method POST
    Then status 401

