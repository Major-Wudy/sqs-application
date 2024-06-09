Feature: Test POST /api/create/electricity/

  Background:
    * url 'http://web:8000/api/create/electricity/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')
 
  Scenario: Create electricity - Valid input
    Given request { "value": 100.5, "country": "us", "state": "fl", "unit": "kwh" }
    When method post
    Then status 201

  Scenario: Create electricity - Invalid value
    Given request { "value": "test", "country": "us", "state": "fl", "unit": "kwh" }
    When method post
    Then status 500

  Scenario: Create electricity - Unauthorized
    Given request { "value": 100.5, "country": "us", "state": "fl", "unit": "kwh" }
    And header Authorization = ''
    When method post
    Then status 401
