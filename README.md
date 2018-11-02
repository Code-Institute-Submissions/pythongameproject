# Riddle Game Project

This is the Practical Python Unit Milestone Project, for Code Institute's Full Stack Web Developer Course.
The objective of this project is to design and execute a Riddle-Me-This game, applying the backend coding language Python.

## UX

This website is designed for an informal gamer who can, through a friendly, simple and clear interphase, perform different actions such as Creating a User,
Login to their Account, Answer Riddles, Submit their own Riddles to the game and see the top scoring users in the Leaderboard. 

User Stories were used for Behavior-Driven Development, such as:
- As a user, I am answering a Riddle, a Riddle question is asked. 
- The Riddle has a correct answer, the correct answer is given, the given answer is then correct.


## Features

### Existing Features
- User Creation: A player is allowed and promted to get a user before playing the game, with the objective of recording their scores.
- Login, which allows said storage of data for the user score to be displayed in the Leaderboard.
- Play, where Riddles will be asked to the User, who will answer.
- When a Riddle is answered, the user is given the correct response.
- When the User plays, the game shows them an Unanswered Riddle.
- Submit a Riddle, where the User is allowed to add a Riddle which will be moderated and therefore added or not.
- Leaderboard, where the high scores are presented.


### Features Left to Implement
- In the future, I would implement allowing spelling mistakes.

## Technologies Used

- HMTL language, for writing the webpage layout. 

- CSS language to style the layout of the game

- Font Awesome (https://fontawesome.com/)
    Font and Icon toolkit

- Bootstrap 4 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    This framework was used for responsiveness of the site 

- Bootswatch Minty (https://bootswatch.com/minty/)
    Theme for Bootstrap that allows for a simple yet attractive design to be applied to the project

- Python, backend language, to create the server of the game application.

- Sqlite3, Database engine. 
    This Database stores the Users, Riddles and Scores for the Leaderboard. 

- Behave, for Behavior Driven Deployment or BDD.
    Behave creates tests, which were used for testing the Game and Authentication features.

- Flake (http://flake8.pycqa.org/en/latest/index.html#quickstart) 
    For validation of Python code.



## Testing

Testing was performed through automated and manual tests. 

- Validity of Python code was tested through Flake. 

- Behave was used for testing Behavior Driven Development. 

- User Stories for the Behavior Driven Development were as follows:

        ⋅⋅* Feature: Authenticating a user
        
        ⋅⋅*   Scenario: Authenticating an existing user with the wrong password 
            ⋅⋅* Given that I am authenticating a user
            ⋅⋅* When the user is "micaela"
              ⋅⋅* And the password is "incorrect password"
            ⋅⋅* Then I should find that the user is not authenticated
          
          ⋅⋅* Scenario: Authenticating an existing user
            ⋅⋅* Given that I am authenticating a user
              ⋅⋅* And I enter a username "micaela"
              ⋅⋅* And I enter a password "signorelli"
            ⋅⋅* When I check that the user is authenticated
            ⋅⋅* Then I should find the user is authenticated
        
          ⋅⋅* Scenario: Authenticating a non-existent user
            ⋅⋅* Given that I am authenticating a user
            ⋅⋅* When the username is "someone"
              ⋅⋅* And the password is "whodoesntexist"
            ⋅⋅* Then I should find that the user is not authenticated
            
    ----------------------------------------------------------------------------
    
        ⋅⋅* Feature: Checking an answer is correct 
          
          ⋅⋅* Scenario: a correct answer
            ⋅⋅* Given we are answering a riddle
                ⋅⋅* And the riddle "what is the colour" is asked
                ⋅⋅* And the correct answer is "yellow"
            ⋅⋅* When we give the answer "yellow"
            ⋅⋅* Then answer is correct
            
          ⋅⋅* Scenario: an incorrect answer
            ⋅⋅* Given we are answering a riddle
                ⋅⋅* And the riddle "what is the colour" is asked
                ⋅⋅* And the correct answer is "yellow"
            ⋅⋅* When we give the answer "red"
            ⋅⋅* Then answer is incorrect
            
The initial test was developed to fail, written as follows:
        
        ⋅⋅* Scenario: a correct answer
               ⋅⋅* Given we are answering a riddle
                   ⋅⋅* And the riddle "what is the colour" is asked
                   ⋅⋅* And the correct answer is "yellow"
               ⋅⋅* When we give the answer "what is breakfast"
               ⋅⋅* Then answer is incorrect


During the Behave implementation, there was an unexpected error message for 
Authentication.py test, where Behave could not find Flask. After changing the 
import information from "User" to "user" it worked again. My mentor told me there 
were conventions of Python concerning upper and lower cases, I presume the mistake 
was fixed when the uppercase was lowered due to said conventions.  
I changed every file to underscore accordingly. 

- Media Queries were defined to improve responsiveness of the webpage, particularly 
for smartphones and tablets. This was extensively tested in different browsers, 
screen sizes and Operative Systems, since it was originally designed in a Mac Laptop.

- Manual Browser testing was performed through acting like a user in the webpage, 
utilizing all the features. Through attemplting User Creation, Login, recording 
and retrieving Scores, and extensive playing, said features were confirmed to 
work correctly.


An example of a manual test was User creation.
1. User Creation:
    1. Go to Home page
    2. Submit a user name usertest
    3. Submit a password userpass
    4. See a welcome message in the Navbar
    5. Be allowed to play the Riddle Game
    6. Logout with Logout link+icon in Navbar

Another manual test was retrieving Scores
1. Retrieving Scores:
    1. Go to Leaderboard page
    2. Cofirm it is empty
    3. Login with a username and password
    4. Answer several riddles
    5. See the highscore published in the leaderboard



## Deployment
This project was deployed through Github pages from the project Git master branch,
it can be found here: https://mgsignorelli.github.io/pythongameproject/
The submitted and deployed versions are identical.


## Credits

- Most Riddles were taken from: 
https://www.everythingmom.com/parenting/45-riddles-and-brain-teasers-for-kids

### Media
- The background image was made by me.

### Acknowledgements

I received inspiration for this project from:
 - File Input/Output module of Course Institute: https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+BD101+2017_T1/courseware/22fb100b5f5846e3b4f2db18683b08bb/f4521923f14f4f98b3ec161db66773e6/?child=first)
 - Inspiration for Sqlite Login Function: https://www.youtube.com/watch?v=ngynJQ0iVwM - - - https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
 - Inspiration for Creating User functionality: https://www.youtube.com/watch?v=NKHUPhfBaW0
 - For Behavior Driven Development, https://behave.readthedocs.io/en/latest/tutorial.html