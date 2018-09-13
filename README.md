# Stream Two Practical Python Project
 
## Create web application word based guessing game - Hangman.

I decided for this project to build a version of the children's classic classroom game, Hangman.
	
	The main aims of the application are: 
		
	1. To allow a user to play their own unique instance of the game.
	2. To be user friendly and simple to use.
	3. To track a users performance and individual score.
	4. To display a historical leaderboard of user scores.

## Demo

A live demo of the site is available at https://stream-two-hangman.herokuapp.com/. 

A github repo of the application is available at https://github.com/darchard1984/stream-two-practical-python-project.

## Getting Started/Deployment

* If you wish to run this site locally, please clone or download this repo. Navigate to your local directory and then run "hangman.py" in your terminal.
* If you wish to deploy a live version of this site, then you will need to create your own Heroku repo/app (or the same on a similar hosting platform) and re-deploy the repo.

## Built With 

**VSCODE, HTML, CSS, SASS/SCSS, BOOTSTRAP, JAVASCRIPT, PYTHON3, FLASK, JINJA, PHOTOSHOP, BALSAMIQ.**

## UX Design

Details of the UX design and research process is available in the repo "documentation" folder. The documents show how I approached the design of the site using the 5 layers approach. (Strategy, Structure,Scope, Skeleton, Surface). 

## Build Approach

1. I began the build by first concentrating on the Python logic and functionality. I used a TDD approach, unit testing each function as I progressed. As the application grew I decided to split off the script into separate modules to make the codebase more readable.
2. To test the progress of the Python app I used the console for the most part, but created basic Flask routes to display HTML templates of the information I eventually wanted the user to see, albeit with no styling. Until happy with the Python functionality I decided not to proceed with any work on the frontend.
3. I decided to store the game's key information in 4 text files. One for usernames, one with a list of 1000 words, one for in game tracking of correct guesses and incorrect guesses, and one for the users score. These files are referenced/written to at different stages of the application.
4. Initially I used AJAX requests to return HTML templates displaying the result of user interaction. For example, a Flask Route returning an HTML template displaying the dashes array of the generated word. However, I eventually refactored the Python code, HTML and JS to return JSON objects rather than HTML. I decided on this approach for various reasons. Returning data instead of HTML is inline with standard practice, and aided in maintaining a better separation of concerns in my code. Keeping data and the logic on the backend, and markup/rendering of information on the frontend. Returning JSON also gave me more control when displaying data on the front-end. 
5. I wanted to style the application to reflect the nature of the Hangmans origins. The classroom. I opted to keep the styles basic, a blackboard background (a free to use resource) and two chalk based fonts. Both fonts are free to use .tff files. I feel this decision helps to give the game it's character, and enhances the user experience. 
6. JS was used to compliment the Python logic and to enhance the feel of the app. For example, I use JS to make sure that data will only be passed to the back-end via an AJAX request if a certain condition is met. This means that the game will only begin AFTER certain user interaction has taken place. I have used functions like this to control the flow of the game in order to mitigate unexpected results from user interaction.
7. I used Bootstrap for it's grid system. Other than that, all SCSS styles are my own.
8. I used http://pleeease.io/play/ to generate vendor prefixes once the building of the application was complete. This allowed me to concentrate on writing clean SCSS until the end of the project and ready for submission/deployment.

## Testing

Automated, manual and technical testing of the site was undertaken and passed. 

1. Python Unit Tests were undertaken as I built the logic of the game. All tests pass.
2. Chrome/Firefox dev tools used throughout to test JS, responsiveness and function.
3. Testing the site across different devices in real world scenarios. Mobiles, Tablets, Laptops, and Desktops.
4. Giving the applcation to third party users to get feedback, and see if they could "break" the application.
5. W3C code validator to pass HTML, CSS and JS. 

## Authors

**Dafydd Archard** - this application was created as part of Code Institute's Web Development Online Full-Stack Course in April 2018.

## Acknowledgments

1. http://pleeease.io/play/
2. w3c Validator service
3. Stack Overflow







