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
    When User enters password RichyRich098
    Then Verify sign in is successful
