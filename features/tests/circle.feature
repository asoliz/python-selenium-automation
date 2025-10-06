# Created by asoliz at 9/18/25
Feature: UI test to verify that Circle page displays benefits

  # Create a test case that will open the Target Circle page
  #https://www.target.com/circle, and verify there are at least 10 benefit cells
  Scenario: User is able to see the Target Circle Benefits
    Given Open Target Circle page
    Then Verify at least 10 benefit cells display

