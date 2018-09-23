Feature: Authenticating a user

  Scenario: Authenticating an existing user with the wrong password 
    Given that I am authenticating a user
    When the user is "micaela"
      And the password is "incorrect password"
    Then I should find that the user is authenticated
  
  Scenario: Authenticating an existing user
    Given that I am authenticating a user
      And I enter a username "micaela"
      And I enter a password "signorelli"
    When I check that the user is authenticated
    Then I should find the user is authenticated

  Scenario: Authenticating a non-existent user
    Given that I am authenticating a user
    When the username is "someone"
      And the password is "whodoesntexist"
    Then I should find that the user is not authenticated
    
