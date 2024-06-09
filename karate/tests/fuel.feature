Feature: Test POST /api/create/fuel/

  Background:
    * url 'http://web:8000/api/create/fuel/'
    * header Authorization = 'Bearer ' + java.lang.System.getenv('TOKEN_UNIT_TEST')

  Scenario: Create fuel - Valid input
    Given request { "source": "Natural Gas", "value": 500 }
    When method post
    Then status 201

  Scenario: Get fuel estimate - Attempt GET request
    Given request { "source": "Natural Gas", "value": 500 }
    When method GET
    Then status 405

  Scenario: Create fuel - Invalid value
    Given request { "source": "Natural Gas", "value": "test" }
    When method post
    Then status 500

  Scenario: Create fuel - Unauthorized
    Given request { "source": "Natural Gas", "value": 500 }
    And header Authorization = ''
    When method post
    Then status 401
