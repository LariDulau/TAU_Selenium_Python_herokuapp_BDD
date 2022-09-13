Feature: Test add remove functionality

  Scenario: Test check add button functionality
    Given open the page
    When the user click add button
    Then add button is displayed


  Scenario: Test elemental selenium link
    Given open the page
    Then the link is displayed
    When the user click on the link
    Then the user is on the elemental selenium link


  Scenario: Test elements on the page
    Given open the page
    Then the title is displayed
    And the user is on the add remove elements page


  Scenario: Test add and delete buttons
    Given open the page
    When the user click add button
    Then is one delete button on the page
    When the user click delete button
    Then no more delete button on the page







