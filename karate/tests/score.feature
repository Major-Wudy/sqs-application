Feature: Test POST /api/get/score/

  Background:
    * url 'http://web:8000/api/get/score/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')
 
  Scenario: get score - Valid input
    Given request { "unit": "g" }
    When method post
    Then status 200

  Scenario: Get score element - Attempt GET request
    Given request { "unit": "g" }
    When method GET
    Then status 405

  Scenario: get score - Invalid value
    Given request { "anakin": "skywalker" }
    When method post
    Then status 500

  Scenario: get score - Unauthorized
    Given request { "unit": "g" }
    And header Authorization = ''
    When method post
    Then status 401
