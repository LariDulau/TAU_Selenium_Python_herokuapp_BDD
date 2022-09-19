Feature: Test iframe page

  Scenario: Test insert text
    Given open the iframe page
    When the user write "The car is new"
    Then "The car is new" is displayed


  Scenario: Test iframe page caracters
    Given open the iframe page
    Then the user is on the iframe page
    And the subtitle is displayed



