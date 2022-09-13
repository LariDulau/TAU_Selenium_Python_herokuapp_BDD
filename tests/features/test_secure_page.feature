Feature: Test logout button functionality

    Scenario: Check logout button
        Given open the login page
        When the user is logging in
        And the user click on logout button
        Then "You logged out of the secure area!" success message is displayed

