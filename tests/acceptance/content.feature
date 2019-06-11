Feature: Test that page have correct content


#  Scenario: Homepage has a logo
#    Given I am on the homepage
#    Then There is a logo shown on the page
#
#
#
#  Scenario: Homepage has the complete question form
#    Given I am on the homepage
#    Then There is question form shown on the page
#    And There is a form title shown on the page
#    And There is a question shown on the page
#    And There is a next button shown on the page

#  Scenario: Map page loads the map
#   Given I am on the map page
#   And I wait for the page to load
#   Then I can see there is a map on the page
#
#  Scenario: Register page loads the form
#   Given I am on the register page
#   Then I can see there is a register form on the page

#  Scenario: Login page loads the form
#   Given I am on the login page
#   Then I can see there is a login form on the page

  Scenario: Add Algorithm page loads the form and table
    Given I am on the add algorithm page
    Then I can see there is an add algorithm form on the page
    And I can see there is a table on the page
    And I can see there are algorithms in the table
    And Algorithm "Algorithm" is shown on the table




