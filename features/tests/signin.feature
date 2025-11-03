# Created by asoliz at 9/10/25
Feature: Log In / Out experience

  Scenario: Logged out user can navigate to Sign In page
    Given Open target main page
    When User clicks on Account button
    When User clicks on Sign In icon
    Then Verify Sign In text is shown
    Then Verify Sign In button is shown

  Scenario: Verify user is logged in
    Given Open target main page
    When User clicks on Account button
    When User clicks on Sign In icon
    When User enters email porrporr@dipan.xyz
    And User selects to continue after email entry
    When User enters password RichyRich098
    And User selects to submit after password entry
    Then Verify sign in is successful

  Scenario: Error message appears for incorrect fields
    Given Open target main page
    When User clicks on Account button
    And User clicks on Sign In icon
    And User enters email porrporr@dipan.xyz
    And User selects to continue after email entry
    And User enters password RichyRich0
    And User selects to submit after password entry
    Then Verify that incorrect password error message appears

