# Riddle Game Project

This is the third Milestone Project, the Practical Python Unit, for Code Institute's Full Stack Web Developer Course.
The objective of this project is to design and execute a Riddle-Me-This game, applying the backend coding language Python.

## UX

This website is designed for an informal gamer who can, through a friendly and clear interphase, 
Create a user, answer Riddles, Submit their own Riddles to the game and see the top scores in the Leaderboard. 

User Stories were used for Behavior-Driven Development, such as:
- As a user, I am answering a Riddle, a Riddle question is asked. 
- The Riddle has a correct answer, the correct answer is given, the given answer is then correct.


## Features

### Existing Features
- User Creation: A player is allowed and promted to get a user before playing the game, with the objective of recording their scores.
- Login, which allows said storage of data for the user score to be displayed in the Leaderboard.
- Play, where Riddles will be asked to the User.
- Submit a Riddle, where the User is allowed to add a Riddle which will be moderated and therefore added or not.
- Leaderboard, where the high scores are presented.


### Features Left to Implement
- Another feature idea

## Technologies Used

- HMTL language, for writing the webpage layout. 
- Bootstrap 4 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    This was used for responsiveness of the site 

- Bootswatch Minty (https://bootswatch.com/minty/)
    Bootswatch allows for a simple yet attractive design to be applied to the project

- Python, backend language, to create the server of the game application.

- Sqlite3, Database engine. 
    This Database stores the Users, Riddles and Scores for the Leaderboard. 

- Behave, for Behavior Driven Deployment or BDD.


## Testing
Testing was performed through automated and manual tests. 
Unit Testing was performed with Python scripts, and Behave was used for testing Behavior Driven Development. 

The responsiveness and performance of the webpage were tested in different browsers, screen sizes and Operative Ststems, since it was originally designed in a Mac Laptop.

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
- The photos used in this site were obtained from ...

### Acknowledgements

I received inspiration for this project from:
 - File Input/Output module of Course Institute: https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+BD101+2017_T1/courseware/22fb100b5f5846e3b4f2db18683b08bb/f4521923f14f4f98b3ec161db66773e6/?child=first)
 - Inspiration for Sqlite Login Function: https://www.youtube.com/watch?v=ngynJQ0iVwM - - - https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
 - Inspiration for Creating User functionality: https://www.youtube.com/watch?v=NKHUPhfBaW0