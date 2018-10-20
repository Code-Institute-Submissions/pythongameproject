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
- Submit a Riddle, where the User is allowed to add a Riddle which will be moderated and therefore added or not.
- Leaderboard, where the high scores are presented.


### Features Left to Implement
- Another feature idea

## Technologies Used

- HMTL language, for writing the webpage layout. 

- CSS language to style the layout of the game

- Bootstrap 4 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    This framework was used for responsiveness of the site 

- Bootswatch Minty (https://bootswatch.com/minty/)
    Theme for Bootstrap that allows for a simple yet attractive design to be applied to the project

- Python, backend language, to create the server of the game application.

- Sqlite3, Database engine. 
    This Database stores the Users, Riddles and Scores for the Leaderboard. 

- Behave, for Behavior Driven Deployment or BDD.
    Behave creates tests, which were used for testing the Game and Authentication features.

- Font Awesome (https://fontawesome.com/)
    Font and Icon toolkit


## Testing
Testing was performed through automated and manual tests. 
Unit Testing was performed with Python scripts, and Behave was used for testing 
Behavior Driven Development. 

User Stories for the Behavior Driven Development were as follows:
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

Media Queries were defined to improve responsiveness of the webpage. This was 
extensively tested in different browsers, screen sizes and Operative Systems, 
since it was originally designed in a Mac Laptop.

Manual testing was performed through acting like a user in the webpage, utilizing all 
the features. Through attemplting User Creation, Login, recording and retrieving Scores, and 
extensive playing, said features were confirmed to work correctly.

In this section, you need to convince the assessor that you have conducted enough testing to 
legitimately believe that the site works well. Essentially, in this part you will want to go 
over all of your user stories from the UX section and ensure that they all work as intended, 
with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This project was deployed through Github pages.
The submitted and deployed versions are identical.

The deployed project can be found here:

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The background image was made by me.

### Acknowledgements

I received inspiration for this project from:
 - File Input/Output module of Course Institute: https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+BD101+2017_T1/courseware/22fb100b5f5846e3b4f2db18683b08bb/f4521923f14f4f98b3ec161db66773e6/?child=first)
 - Inspiration for Sqlite Login Function: https://www.youtube.com/watch?v=ngynJQ0iVwM - - - https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
 - Inspiration for Creating User functionality: https://www.youtube.com/watch?v=NKHUPhfBaW0