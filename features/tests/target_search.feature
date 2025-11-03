# Created by asoliz at 9/10/25
Feature: Search capability

  # Update Target product search test case and add Behave variables.
  Scenario: User can search for coffee in Target
    Given Open target main page
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tool tip is shown
