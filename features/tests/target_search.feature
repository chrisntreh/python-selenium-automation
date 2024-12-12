# Created by chris at 12/4/2024
#Feature: Test for search
#
#  Scenario: User can search for a products
#    Given Open target main page
#    When Search for tea
#    Then verify search results shown


#Feature: Test for target shopping cart
#
#  Scenario: User can access target and find cart
#    Given Open target main page
#    When click cart icon
#    Then verify empty sign is showing


Feature: Test for target sign in
  Scenario: User can access target sin in
    Given Open target main page
    When click sign in
    Then verify sign in form is open

