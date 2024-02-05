Hangman is a classic word game in which the user must guess the hidden word before they run out of attempts.

This project was implemented as a final project for my COMP 123 class: Core Concepts of Computer Science. 
We worked in groups in order to accomplish our first-ever CS game.

As a team:

We learned and familiarized ourselves with TKinter. By using a GUI to display our Hangman Game, we were able to play around with positioning, buttons, and labels. 
When running into errors and debugging, we problem-solved and learned to identify issues in our code. This helped to hone our skills in troubleshooting and overcoming coding challenges. 
The overall concept of the game worked out the way it thought it would. The functionalities and idea of the game wasn’t too complicated since we all had a good grasp of how the game works. 
It was surprising to see how we could enrich our GUI by incorporating different aspects and components. Initially, we had not expected such versatility but as we worked on it we found 
potential to include more and more creative elements; the images, music, and hangman figure in particular. Also, it was interesting to observe how the placement of the image at different 
locations in the code would either make it work or fail. From this we learned how important it is to understand the context and order of the code. Next time something we would do differently 
is offer the user a more personalized experience by providing them with the option to choose from multiple themed dictionaries. Once they pick a theme, the user can guess words associated 
with that theme. As for future extensions, we would like to have fixed up how the win/lose squirrel image resets along with the game instead of collecting multiple. If given more time we would 
like to have implemented a larger window with more aesthetically pleasing GUI display visuals

Here are some key characteristics of the game: 

- Interactive Graphic User Interface (GUI): On a graphic screen, the game randomly selects a word that the user must guess. Each correct letter of the word pops up on the screen with every correct attempt throughout the game. If the guess is incorrect, an illustration of a hangman progressively appears with every wrong attempt until the game is over. 
- Illustrative Images: If a user successfully guesses the word, an image of a happy squirrel will appear on the screen. If a user does not successfully guess the correct word, an image of a sad squirrel will appear. 
- Descriptive labels: In the top part of the window, a representation of the hidden word with dashes indicates that its letters have not yet been guessed, and when guessed, it will update, revealing the letter and its position. Each dash represents a hidden letter of the word. At the bottom, a label with the number of attempts for each game is located. The label updates with every attempt, decreasing from 6 until 0. 
