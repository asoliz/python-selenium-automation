# Created by asoliz at 11/2/25
Feature: Help Features

  Scenario: User can select Help topic
    Given Open target returns page
    Then Verify Help Returns page opened
    When Select Promotions & Coupons in Help dropdown menu
    Then Verify Current promotions age opens

