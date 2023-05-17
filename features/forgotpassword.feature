Feature: Forgot password
  To check forgot password functionality and bus button
  @smoke @comfort
  Scenario: Enter Email ID
    Given user is on the homepage
    And user clicks on My Account button
    When user clicks on Login button
    Then user can enter email id on login page

  @comfort
  Scenario: Select Bus Button
    Given user is on the homepage
    When user clicks on bus button
    And user press search bus button
    Then redirected to search listing page

