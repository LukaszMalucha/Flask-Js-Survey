Feature: Test that page have correct content


  Scenario: Map page has a correct title
    Given I am on the map page
    Then There is a title shown on the page
    And The title tag has content "ML Selector"

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "ML Selector"

  Scenario: Homepage has all questions
    Given I am on the homepage
    Then There are all questions shown on the page

  Scenario: Map page loads the map
   Given I am on the map page
   And I wait for the page to load
   Then I can see there is a map on the page

  Scenario: Signup page loads the form
   Given I am on the signup page
   Then I can see there is a signup form on the page

  Scenario: Login page loads the form
   Given I am on the login page
   Then I can see there is a login form on the page




