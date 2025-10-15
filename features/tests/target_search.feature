# Created by asoliz at 9/10/25
Feature: Search capability

  # Update Target product search test case and add Behave variables.
  Scenario: User can search for coffee in Target
    Given Open target main page
    When Search for tea
    Then Verify search results are shown for tea

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods
    Then Verify that every product has a name and an image


