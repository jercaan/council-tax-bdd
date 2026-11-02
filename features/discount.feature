Feature: Council tax single person discount
  As a resident who lives alone
  I want to check if I qualify for the single person discount
  So that I know how much council tax I need to pay

  Scenario: Resident living alone receives the discount
    Given the annual council tax charge is £1800
    When the resident enters "1" as the number of adults
    Then the resident should be eligible for the discount
    And the amount to pay should be £1350.00

  Scenario: Household with two adults does not receive the discount
    Given the annual council tax charge is £1800
    When the resident enters "2" as the number of adults
    Then the resident should not be eligible for the discount
    And the amount to pay should be £1800.00

  Scenario Outline: Invalid number of adults is rejected
    Given the annual council tax charge is £1800
    When the resident enters "<adults>" as the number of adults
    Then an error message should say "<message>"

    Examples:
      | adults | message                                  |
      | 0      | Number of adults must be at least 1      |
      | -2     | Number of adults must be at least 1      |
      | abc    | Number of adults must be a whole number  |