Feature: Test POST /api/delete/score/

  Background:
    * url 'http://web:8000/api/delete/score/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')
 
  Scenario: delete score - Valid input
    Given request {}
    When method GET
    Then status 200

  Scenario: Get score element - Attempt GET request
    Given request { "Kenobi": "Hello there" }
    When method POST
    Then status 405

  Scenario: get score - Unauthorized
    Given request { "Jar Jar": "Michse nix authorisiert" }
    And header Authorization = ''
    When method post
    Then status 401
