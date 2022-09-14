Feature: Swag Labs Login

  Background: common steps
    Given user launches the browser
    When user enters the Swag Labs URL
    And user opens the Login page
    And user enters the username "standard_user" and password "secret_sauce"
    And user clicks on the login button

  Scenario: Login to Swag Labs
    Then user will be logged in to Swag Labs

  Scenario: Search product
    Then user will be logged in to Swag Labs
    Then products should be displayed on the page

  Scenario: Search for app logo
    Then user will be logged in to Swag Labs
    Then app logo should be displayed on the page

