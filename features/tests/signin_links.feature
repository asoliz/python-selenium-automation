# Created by asoliz at 10/24/25
Feature: Verify all sign in links work
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When User clicks on Account button
    And User clicks on Sign In icon
    And Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
