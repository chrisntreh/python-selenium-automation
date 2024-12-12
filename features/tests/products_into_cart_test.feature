# Created by chris at 12/10/2024
Feature: open the Target page
  Scenario: User can access Target’s product into the cart
    Given Open target page
    And Search for tea
    When Add to cart
    And access cart
    Then verify 1 item is added to cart