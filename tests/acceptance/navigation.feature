Feature: Test navigation between pages


  Scenario: Home can go to Map
    Given I am on the homepage
    When I click on the "SCIKIT MAP" link
    Then I am on the map page

#  Scenario: Map can go to Home
#    Given I am on the map page
#    When I click on the "BACK TO MAIN PAGE" link
#    Then I am on the homepage
#
#  Scenario: Home can go Suggest
#    Given I am on the homepage
#    When I click on the "SUGGEST" link
#    Then I am on the suggest page
#
#  Scenario: Suggest can go Home
#    Given I am on the suggest page
#    When I click on the "BACK TO MAIN PAGE" link
#    Then I am on the homepage
#
#  Scenario: Home can go to Login
#    Given I am on the homepage
#    When I click on the dropdown menu
#    Given I wait for the dropdown to load
#    When I click on the login
#    Then I am on the login page
#
#   Scenario: Home can go to Signup
#    Given I am on the homepage
#    When I click on the dropdown menu
#    Given I wait for the dropdown to load
#    When I click on the "Sign In" link
#    Then I am on the signup page
#
#   Scenario: Home can go to Logout
#    Given I am on the homepage
#    When I click on the dropdown menu
#    Given I wait for the dropdown to load
#    When I click on the "Log Out" link
#    Then I am on the login page
#
#

