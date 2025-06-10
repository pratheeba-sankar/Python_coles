# Created by pratheeba at 2/06/2025
Feature: Coles online shopping automation

  Background:
    Given I have launched the Coles website
    And I have a valid Coles account


  Scenario: Login and add items to cart
    When I login to the Coles account
    Then I should see a login result
    And I write the login result to the excel file

    When I navigate to the specials section and add fruit and milk to the cart
    And I view the cart and get the total price
    Then I verify the total price is correct
    Then I write the total price to the excel file