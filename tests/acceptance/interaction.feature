Feature: Test that forms work correctly



#  Scenario: Register page registers user
#    Given I am on the register page
#    When I enter "tester" in the "username" field
#    And I enter "tester@gmail.com" in the "email" field
#    And I enter "tester1234" in the "password" field
#    And I enter "tester1234" in the "confirm" field
#    And I press the submit button
#    Then I am on the homepage


#  Scenario: Login page login user
#    Given I am on the login page
#    When I enter "tester@gmail.com" in the "email" login field
#    And I enter "tester1234" in the "password" login field
#    And I press the submit button
#    Then I am on the homepage
#
#
  Scenario: Filled form gives answer
    Given I am on the homepage
    When I choose a first answer
    When I press the Next button
    And I wait for a second
    And I choose a first answer
    And I press the Next button
    And I wait for a second
    And I choose a first answer
    And I press the Next button
    And I wait for a second
    And I choose a first answer
    And I press the Next button
    And I wait for a second
    And I choose a first answer
    And I press the Complete button
    And I wait for a second
    Then I can see there are results on the page


#
#
#  Scenario: Suggested Algorithm goes to database
#    Given I am on the suggest page
#    When I type "testing" in "algorithm" field
#    And I type "testing" in "description" field
#    And I press suggest algorithm button
#    Then Algorithm "testing" is shown in the table
#

