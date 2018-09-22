Feature: Checking an answer is correct 
  
  Scenario: a correct answer
    Given we are answering a riddle
        And the riddle "what is the colour" is asked
        And the correct answer is "yellow"
    When we give the answer "yellow"
    Then answer is correct
    
  Scenario: an incorrect answer
    Given we are answering a riddle
        And the riddle "what is the colour" is asked
        And the correct answer is "yellow"
    When we give the answer "red"
    Then answer is incorrect
 
# USE ONLY IS TESTING THAT TESTS FAIL AS THEY SHOULD
#   Scenario: a correct answer
#       Given we are answering a riddle
#           And the riddle "what is the colour" is asked
#           And the correct answer is "yellow"
#       When we give the answer "what is breakfast"
#       Then answer is incorrect



