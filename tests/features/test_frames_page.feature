Feature: Test frames page

  Scenario: Test frames page elements
    Given open the frames page
    Then the user is on the current url
    And the subtitle is displayed


  Scenario: Test nested frames link
    Given open the frames page
    When the user click on nested frames link
    Then the user is not on the current url


