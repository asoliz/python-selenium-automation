# Created by asoliz at 9/10/25
Feature: New empty cart message

  Scenario: Verify empty cart message appears
    Given Open target main page
    When User clicks on cart icon
    Then Verify empty cart message appears
