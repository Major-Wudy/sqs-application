Feature: Test POST /api/get/estimate/flight/

  Background:
    * url 'http://web:8000/api/estimate/flight/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Get flight estimate - Successful request
    Given request {"type": "flight","passengers": "2","legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_unit": "km"}
    When method POST
    Then status 201

  Scenario: Get flight estimate - Attempt GET request
    Given request {"type": "flight","passengers": "2","legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_unit": "km"}
    When method GET
    Then status 405

  Scenario: Invalid request - Missing required fields
    Given request {}
    When method POST
    Then status 500

  Scenario: Unauthorized request - Missing or invalid token
    Given request {"type": "flight","passengers": "2","legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_unit": "km"}
    And header Authorization = 'Bearer invalid-token'
    When method POST
    Then status 401