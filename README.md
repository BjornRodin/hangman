# Hangman 3000

## Introduction
This is a Hangman game where you can guess the hidden word and get scores depending on your performance. It's made to be attractive for the user and provide some fun for both first time players and veterans. 

[View the live project here](https://hangman-3000.herokuapp.com/)

[Link to Github Repository](https://github.com/BjornRodin/hangman)


![Am I Responsive?](documentation/readme-images/introduction-image.JPG)

## Table of Content
- [Introduction](#introduction)
- [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
        - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Returning Visitor Goals](#returning-visitor-goals)
        - [Administrators](#administrators)
    - [Design](#design)
        - [Graphics](#graphics)
        - [Flowchart](#flowchart)
- [Features](#features)
    - [Existing Features](#existing-features)

    - [Future Features](#future-features)
- [Testing](#testing)
    - [User Stories Testing](#user-stories-testing)
       - [As a first time visitor I want to quickly find and understand the rules](#as-a-first-time-visitor-i-want-to-quickly-find-and-understand-the-rules)
       - [As a first time visitor I want to know how to start the game](#as-a-first-time-visitor-i-want-to-know-how-to-start-the-game)
       - [As a first time visitor I want to get feedback along the way of the game](#as-a-first-time-visitor-i-want-to-get-feedback-along-the-way-of-the-game)
       - [As a returning visitor I want to see the top scores so I can try to beat it](#as-a-returning-visitor-i-want-to-see-the-top-scores-so-i-can-try-to-beat-it)
       - [As a returning visitor I want to be able to quickly restart the game when it's over](#as-a-returning-visitor-i-want-to-be-able-to-quickly-restart-the-game-when-its-over)
       - [As a returning visitor I want to have a calm background and game with pleasing design](#as-a-returning-visitor-i-want-to-have-a-calm-background-and-game-with-pleasing-design)
       - [As a administrator I want to provide the users with a game that is easy to navigate](#as-a-administrator-i-want-to-provide-the-users-with-a-game-that-is-easy-to-navigate)
       - [As a administrator I want to provide simple functions to not overcomplicate things](#as-a-administrator-i-want-to-provide-simple-functions-to-not-overcomplicate-things)
       - [As a administrator I want to provide a design and feedback that is fun and engages with the user](#as-a-administrator-i-want-to-provide-a-design-and-feedback-that-is-fun-and-engages-with-the-user)
    - [Automated Testing](#automated-testing)
        - [W3C Markup Validation Service](#w3c-markup-validation-service)
        - [W3C CSS Validation Service](#w3c-css-validation-service)
        - [JSHint Javascript Validator](#jshint-javascript-validator)
        - [Google Lighthouse Performance Test](#google-lighthouse-performance-test)
            - [Warnings](#warnings)
    - [Manual Testing](#manual-testing)
        - [Features Test](#features-test)
        - [Browser](#browser)
        - [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Technologies](#technologies)
- [Deployment](#deployment)
    - [Deployment Github Pages](#deployment-github-pages)
    - [Cloning Repository](#cloning-repository)
    - [Open Cloned Repository](#open-cloned-repository)
    - [Version Control](#version-control)
- [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
- [Acknowledgements](#acknowledgements)


## User Experience (UX)

### Introduction
The goal for this website is to provide people with a fun game to spend some time but not having to invest hours upon hours of gametime. Play the game wherever you are and whenever you feel like it. The hidden words is chosen from a list of 450+ unique nouns and within each game the same word can't be chosen twice. The difficulty is random, due to the length of the words, but thanks to a adaptive scoring system you will get more points if the word is harder.
In the end of the game you can either chose to play again and guess another word (and further increase your score) or to end the game. Whenever the game is ended you will be updated if you are in the top 5 or not and then the scoreboard is printed.
Enjoy!

### User Stories

#### First Time Visitor Goals
As a first time visitor I want to:
- quickly find and understand the rules.
- know how to start the game.
- get feedback along the way of the game.

#### Returning Visitor Goals
As a returning visitor I want to:
- be able to quickly restart the game when it's over.
- see the top scores so I can try to beat it.
- have a calm background and game with pleasing design.

#### Administrators
As a administrator I want to:
- provide the users with a game that is easy to navigate.
- provide simple functions to not overcomplicate things.
- provide a design and feedback that is fun and engages with the user.

### Design

#### Graphics
The graphics of the hangman was designed from how I used to play the game as a kid when doing it on a whiteboard at school. By using "/", "\", "0" & "|" I could replicate a simple, but useful, graphic that updates over time in the game.

![Hangman-graphics](documentation/readme-images/hangman-graphic.JPG)

#### Flowchart
To create the general idea of how the game logically should be running I made a simple flowchart with [Lucidchart](https://www.lucidchart.com). By doing this I had something to lean back on when programming to I had something to guide me. I was almost certain that it was not going to be made exactly as I made the chart, as I have never done one before, but I am happy with the result. It's pretty close to the end product as well so it definitely was a good thing to spend time on. If anything I would probably spend more time on that in the future for other projects, but due to some time-constraints on my end this time I couldn't spend more time on it. 

![Flowchart](documentation/readme-images/flowcharthangman.JPG)

## Features

### Existing Features
- The game-info is presented as the page is loaded to give the user clear information that there is going to be information presented in that area when the game is running.This area is updated as the game is running to give the user real-time feedback.
    
    ![Game-info](documentation/readme-images/game-info.JPG)
- The mole-area is presented with 9 squares, all with a pile of dirt in them to clearly show the user where the game-area is and where to expect the mole to appear. Directly under the level of difficulty is shown for the user to chose as they please.

    ![Mole-area](documentation/readme-images/mole-area%26difficulty.JPG)
- The control-area is from where the user can either click on a button to read the rules or start the game.

    ![control-area](documentation/readme-images/control-area.JPG)
    
    ![Howtoplay](documentation/readme-images/howtoplay.JPG)
- When the game has finished the user is presented with a popup-window with a message that changes depending on how well the user performed, their score clearly visible, a question if they want to play again and then the corresponding buttons to either play again or close the popup-window to change the difficulty settings.

    ![Gameover](documentation/readme-images/gameover.JPG)

- A 404.html is also added in case it's needed, the page has styling similar to the index.html and a return button to go back to the game instead of having to press the return button in the browser.

    ![404html](documentation/readme-images/404html.JPG)


### Future Features
- Adding a Highscore scoreboard.
- More custom messages for the gameover popup.
    - Chosen randomly depending on what level of difficulty the user is playing and what score they got.
    - Also adding another message depending on how many moles that are missed.
- Counting the moles that are getting away, right now we calculate if the user hit or miss the mole or not but not the moles that are getting away so to speak.
- In the gameover popup the total number of appeared moles could be presented (as it changes due to the random calculation for how long the mole is visible).
- Making the user able to change the gametime between 30 or 60 seconds depending if they want a shorter game or not. 
- Adding sound to the game.
- When the game is started the user could be presented with a short countdown from 3 to be even more ready when the game actually start running.

## Testing

### User Stories Testing

#### As a first time visitor I want to quickly find and understand the rules
- As soon as the game is loaded the user can easily see the rules printed on the screen.

#### As a first time visitor I want to know how to start the game
- As soon as the game is loaded the cursor is set to the bottom of the page, asking for the users username. As this is the only thing the user can interact with it is logical for the user to start there.
- When username is entered and accepted the user is presented with a message saying "press Enter to start the game...".
- When the user lost all their guesses or guessed the word correctly the game prompts the user with a choice if they want to play again or not.

#### As a first time visitor I want to get feedback along the way of the game
- Every time the user enters some input that input is validated in the code, if not valid the user is presented with what they have to do.
- When guessing wrong or correct letter the user get printed messages showing what their input was and if it was wrong/correct.
- When the input has been checked for wrong/correct then the corresponding graphics is updated accordingly.
- This continues all the way until remaining guesses is "0" or the word is guessed correctly, depending on which the feedback changes.

#### As a returning visitor I want to see the top scores so I can try to beat it
- When the game is over and the user chooses to stop playing, the game check if the score that is accumulated is in the top 5 scores overall. If it is their result is added to the board. It doesn't matter if the user is in the top 5 or not, when this is checked the scoreboard is printed.

#### As a returning visitor I want to be able to quickly restart the game when it's over
- As mentioned earlier, when there is no more guesses or the word is guessed correctly the game prompts the user with a choice to play again or to stop.

#### As a returning visitor I want to have a calm background and game with pleasing design
- As there is not much design specifically in the game, that is not the primary goal of this project, it is not much to mention.
- The game is kept simple and logical, some graphics is added to make it more fun to look at and it also works as feedback for the user.
- However, the background is black, text is white, so the contrast between those two is very good and hence make it calmer for the eyes.

#### As a administrator I want to provide the users with a game that is easy to navigate
- As the game is run in a command-window the navigation is very simple. Any inputs asked for is always entered at the bottom of the page and the cursor is always automatically moved along.
- The messages for what information to input is simple and if something is wrong a message to correct the misstake is printed so the user can correct their input.

#### As a administrator I want to provide simple functions to not overcomplicate things
- It is very simple as the user can't deviate from the premade path of the game.

#### As a administrator I want to provide a design and feedback that is fun and engages with the user
- Regarding the design I've done what I could to make it as pleasing as possible aswell as provide utility to the user.
- The hangman graphics is updated depending on how many guesses there is left which make the game way more fun than if it was not present.
- Having the scoreboard printed in the end of the game is probably one of the most important parts to make a user want to play again to either beat their own score or someone elses.

### Automated Testing

#### W3C Markup Validation Service
- index.html
    - Result
        - According to the image below there is no errors or warnings to show.

    ![Index.html test](documentation/readme-images/indexhtml-htmlchecker.JPG)
- 404.html
    - Result
        - According to the image below there is no errors or warnings to show.

    ![Index.html test](documentation/readme-images/indexhtml-htmlchecker.JPG)

#### W3C CSS Validation Service
- style.css
    - Result
        - According to the image below there is no errors to show.
        - According to the image below there is a few warnings to show, more about those under "Warnings".

    ![style.css test](documentation/readme-images/stylecss-cssvalidation.JPG)

    ![style.css test](documentation/readme-images/stylecss-csswarnings.JPG)

#### JSHint Javascript Validator
- script.js
    - Result
        - According to the image below there is no errors or warnings.

    ![script.js test](documentation/readme-images/scriptjs-jshintchecker.JPG)

#### Google Lighthouse Performance Test
The tests are all made in the same way:
1. In incognito-mode
2. The same configuration is used, showed in below image. Only 'Device' was changed in between the tests.
    
    ![Lightouse Configuration](documentation/readme-images/Lighthouse-configuration.JPG)

- Desktop

    ![desktoplighthouse](documentation/readme-images/desktoplighthouse.JPG)
- Mobile

    ![mobilelighthouse](documentation/readme-images/mobilelighthouse.JPG)

#### Warnings
- CSS Warnings
    - The first warning is just that the W3C validator can't validate the imported style sheet. So it's fine to leave it as it is.
        - Source: [Stackoverflow](https://stackoverflow.com/questions/25946111/importing-css-is-ending-up-with-an-error)
    - The second and third warning is only a "heads-up" that they might not be working on older browsers. According to this [source](https://stackoverflow.com/questions/52490004/what-are-all-of-these-w3c-css-validation-warnings-about) it is fine to leave these aswell.
    - The fourth warning is another "heads-up" that it might not be supported on certain browsers. However, according to this [source](https://stackoverflow.com/questions/41406627/css-pointer-events-and-appearance-properties-not-recognized-by-css-validator) this happens because the property hasn't yet achieved a high official status in the W3C validator but is nonetheless supported by major browsers. So I will leave it.

### Manual Testing
Tested according to below image and passing everything.

![testingmanual](documentation/readme-images/manualtesting.JPG)

#### Responsiveness
All the pages was tested with different screen sizes through Developer Tools in the Google Chrome Browser. Below is also a link to 'amiresponsive' where it is also possible to see how the site look on different screen sizes at the same time.

[Am I Responsive?](https://ui.dev/amiresponsive?url=https://bjornrodin.github.io/whac-a-mole/)

![manualresponsiveness](documentation/readme-images/manualresponsiveness.JPG)

## Bugs
- One of the more major bugs I encountered was to make the mole rotate to one side whenever it was hit. For the better part of the project I let it be but in the end I really wanted to solve the issue. The issue was that whenever I tried adding another background image or rotate the existing mole it either totaly overid the existing backgrounds or the image was distorted. After much trial and error I got it working.
- When adding the difficulty selecting feature the mole kept running the same speed  even though another level was set. It took a while for me to realize to add the variables into the randomBox function aswell so it actually changed the speed depending on what the user is choosing. Now it works.

## Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML) was used as the main language for the project.
- [CSS](https://en.wikipedia.org/wiki/CSS) was used to style the HTML elements.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used during this project.
- [GitHub](https://github.com/) is the host which is used to store the code.
- [Git](https://git-scm.com/) was used to commit and push the code to the GitHub repository and works as a version control software. 
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts that was used.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during the whole project, especially while debugging and making it responsive for different screen-sizes.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code in the end of the project.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code in the end of the project.
- [JSHint Javascript Validator](https://jshint.com/) was used to check for errors in the JavaScript code.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used when testing the site.
- [W3C School](https://www.w3schools.com/) was used to aid in coding.
- [Pixabay](https://pixabay.com/) was used to find images for the site.
- [IMGBIN](https://imgbin.com/) was used to find images for the site.
- [Vecteezy](https://www.vecteezy.com/) was used to find images for the site.
- [Adobe Color](https://color.adobe.com/sv/create/image) was used to extract colors from the 'background-field.jpg' image.
- [My ColorSpace](https://mycolor.space/) Was used to find matching colors for those extracted in Adobe Color.
- [Contrast Grid](https://contrast-grid.eightshapes.com/) Was used to see how the different color would contrast against black and white texts.
- [RedKetchup Image Resizer](https://redketchup.io/image-resizer) was used to resize images to improve performance.
- [Am I Responsive](https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.dev) was used to give the reader a quick and easy way to see the responsiveness of the site and also to have a image for the introduction of the Readme.md.
- [Favicons](https://favicon.io/) was used to add a favicon to the browser.

## Deployment 

### Deployment Github Pages
1. Navigate to the [repository](https://github.com/BjornRodin/programmers-meetup-hub)
2. Click on 'Settings' (found in the top/middle of the page).
3. Click on 'Pages' in the menu on the left which will open 'GitHub Pages'.
4. From the dropdown menu 'Source' under the header 'Build and Deployment', select 'Deploy from a Branch'.
5. From the dropdown menu under 'Branch', select 'main' and the folder to the right to 'root'. 
6. Click Save.
7. The page should refresh and the deployment link should appear above 'Build and deployment'.

### Cloning Repository
1. Navigate to the [repository](https://github.com/BjornRodin/programmers-meetup-hub)
2. Click on the 'Code' button on top of the repository and copy the HTTPS link. 
3. Open Git Bash
4. Type 'git clone' and then paste or type the link.
5. Press Enter
The project is now cloned.

### Open Cloned Repository
1. After cloning, type 'ls' and hit 'enter' to locate your repository on your computer.
2. Locate the folder on your computer.
3. Open the folder and double-click the 'index' file to open.

### Version Control
- A repository was made on Github with Code Institutes Template.
- Coding for the site was done on the [Gitpod](https://www.gitpod.io/) platform.
- Code was added to the staging area with the 'git add .' command.
- The changes in the staging area was committed with the 'git commit -m " "' command.
- All committed code was pushed to Github repository with the 'git push' command.

## Credits
### Media
All pictures was downloaded from these three websites, the authors are also included.
- [Pixabay](https://pixabay.com/)
    - In this case I took the image "pileofdirt.png" from the the user [OpenClipart-Vectors](https://pixabay.com/users/openclipart-vectors-30363/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=576447).
- [IMGBIN](https://imgbin.com/)
    - In this case I took the image "molefigure.png" from the user [FireDoidaum](https://imgbin.com/user/FireDoidaum).
- [Vecteezy](https://www.vecteezy.com/)
    - In this case i took the image "background-field.png" from the user [annieart0](https://www.vecteezy.com/members/annieart0).


### Code
- The code that was used in the project was mostly learnt via [Code Institute](https://codeinstitute.net/se/) and their Full Stack Software Development course.
- [W3 School](https://www.w3schools.com/) was mostly used to solve issues or alternate ways to do the coding.

### Content
- The content was designed and written by me.

## Acknowledgements
- Thank you to my family, especially Joakim Rödin, who have supported, pushed and encouraged me during the project.
- Gratitude to my mentor Jack Wachira for the support he has given me.
- The Slack community.