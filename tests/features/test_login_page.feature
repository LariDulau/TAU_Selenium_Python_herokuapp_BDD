Feature: Test login functionality

  Scenario: Test login successfully
    Given open the login page
    When the user type username 'tomsmith'
    And the user type password 'SuperSecretPassword!'
    And the user click login button
    Then the welcome message appears on page
    And the user is on the secure page
    And "You logged into a secure area!" success message is displayed


  Scenario Outline: Check error message with wrong credentials
    Given open the login page
    When the user type username '<username>'
    And the user type password '<password>'
    And the user click login button
    Then '<error>' error message is displayed
    And the user is on the login page

    Examples: Username and password and error
    | username | password | error |
    | tomsmith | password1234 | Your password is invalid! |
    | smithtom | password1234 | Your username is invalid! |
    | smithtom | SuperSecretPassword! | Your username is invalid! |