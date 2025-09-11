# Created by asoliz at 9/10/25
Feature: Search capability
  # Enter feature description here

  Scenario: User can search for a product in Target
    Given Open target main page
    When Search for a product
    Then Verify search results are shown

