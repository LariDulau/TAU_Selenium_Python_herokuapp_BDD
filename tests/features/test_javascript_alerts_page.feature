Feature: Test alert, confirm, prompt functionality

  Scenario: Test accept alert
    Given open the alert page
    When the user open alert
    And the user click OK
    Then 'You successfully clicked an alert' is displayed


  Scenario: Test accept confirm
    Given open the alert page
    When the user open confirm
    And the user click OK
    Then 'You clicked: Ok' is displayed


  Scenario: Test dismiss confirm
    Given open the alert page
    When the user open confirm
    And the user click Cancel
    Then 'You clicked: Cancel' is displayed


  Scenario: Test dismiss prompt
    Given open the alert page
    When the user open prompt
    And the user click Cancel
    Then 'You entered: null' is displayed


  Scenario: Test accept with no text prompt
    Given open the alert page
    When the user open prompt
    And the user click OK
    Then 'You entered:' is displayed


  Scenario: Test accept with text prompt
    Given open the alert page
    When the user open prompt
    And the user insert 'Java Alerts'
    And the user click OK
    Then 'You entered: Java Alerts' is displayed