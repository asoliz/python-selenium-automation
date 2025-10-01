# Created by asoliz at 9/10/25
Feature: Cart behavior

  Scenario: Verify empty cart message appears
    Given Open target main page
    When Click on cart icon
    Then Verify empty cart message appears

  Scenario Outline: HW 4.3 - User can add a product to the cart and verify it's there
    Examples:
      |product  |
      |tv stand           |
    Given Open target main page
    When Search for a <product>
    And Click Add to cart on first product in search results
    And Click Add to cart from side navigation
    And Click on cart icon
    Then Verify <product> is added to cart


  # Create a test case to add any Target’s product into the cart, and make sure it’s
  #there (check that your cart has individual cart items OR the total price, up to you!)
  Scenario: Verify that any Target product can be added to the cart
    Given Open target main page
