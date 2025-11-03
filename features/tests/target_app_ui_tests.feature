# Created by asoliz at 10/16/25
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When User clicks on Account button
    And User clicks on Sign In icon
    And Click Privacy Policy Link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window
