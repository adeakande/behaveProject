Feature: Swag Labs Login

  Scenario: Login to Swag Labs
    Given user launches the browser
    When user enters the Swag Labs URL
    And user opens the Login page
    And user enters the username "standard_user" and password "secret_sauce"
    And user clicks on the login button
    Then user will be logged in to Swag Labs


  Scenario Outline: Login to Swag Labs with Multiple parameters
    Given user launches the browser
    When user enters the Swag Labs URL
    And user opens the Login page
    And user enters the username "<username>" and password "<password>"
    And user clicks on the login button
    Then user will be logged in to Swag Labs

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
      | standard_user | secret       |
      | standard      | secret_sauce |
      | standard      | secret       |