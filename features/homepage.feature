Feature: Yatra - Holiday
  To check the holiday button on the Yatra website
  @regression @smoke
  Scenario: Validate holiday button
    Given user is on the homepage
    When user clicks on holiday button
    And user clicks on search holidays button
    Then redirected to holiday search listing page
    And user scrolls the page

