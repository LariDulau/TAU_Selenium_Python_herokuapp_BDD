Feature: Test context menu functionality

  Scenario: Accept alert
    Given open the context menu page
    When the user click on the menu
    And the user click accept alert
    Then the user is on the context menu page


  Scenario: Check if message is displayed
    Given open the context menu page
    When the user click on the menu
    Then 'You selected a context menu' message is displayed


