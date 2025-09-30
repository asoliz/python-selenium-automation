# Created by asoliz at 9/10/25
Feature: Search capability

  # Update Target product search test case and add Behave variables.
  Scenario Outline: User can search for coffee in Target
    Examples:
      | product | expected_product |
      | coffee  | coffee           |
    Given Open target main page
    When Search for a <product>
    Then Verify search results are shown for <expected_product>


