Feature: Test dropdown functionality


  Scenario: Test select option and elements
    Given open the dropdown page
    When the user select 'Option 1'
    Then the selected option is the first one
    When the user select 'Option 2'
    Then the selected option is the second one
    And the subtitle is 'Dropdown List'
    And the user is on the current url
