import tkinter as tk
import random
from tkinter import messagebox
from PIL import ImageTk, Image


# ----------------------------------------------------------


class HangmanGame:
    """implements the hangman game using tkinter. it takes in a user input, updates the gui display as
letters are guessed and manages the game states. once the word is guessed or the player
reaches the maximum amount of attempts, the game ends"""

    def __init__(self):
        """initializes the hangman game object. sets up the main window and positions the widgets/labels/buttons
    on the grid to implement the GUI"""
        self.gameOver = False
        self.mainWin2 = tk.Tk()
        self.mainWin2.title("Hangman Game")
        self.word_to_guess = random.choice(
            ['macalester', 'software', 'squirrel', 'library', 'scots', 'coding', 'solution', 'carnegie', 'python', 'liberal',
             'college', 'headphone', 'programming']).lower()
        self.guessed_letters = []
        self.attempts_left = 6
        self.quitButton = tk.Button(self.mainWin2, text="Quit", bg="SeaGreen", command=self.doQuit, fg="pink",
                                    font='times')
        self.quitButton.grid(row=1, column=0, padx=5, pady=5)
        self.mainWin2.config(bg="DarkSeaGreen")
        self.resetButton = tk.Button(self.mainWin2, text="Reset Game", bg="SeaGreen", command=self.resetGame,
                                     font=('times', 12), fg="pink")
        self.resetButton.grid(row=2, column=0, padx=5, pady=5)
        self.create_widgets()

    def create_widgets(self):
        """creates and configures the widgets/labels/buttons for the main window.
    defines the hangman display and the initial hangman state"""
        self.secret_word = tk.Label(self.mainWin2, text=self.hide_word(), bg="DarkSeaGreen", font=('Times', 18),
                                    fg="brown")
        self.secret_word.grid(row=1, column=0, columnspan=2, pady=10)
        self.hangman_display = tk.Label(self.mainWin2, text="", bg="DarkSeaGreen", font=('Courier', 14), fg="sienna")
        self.hangman_display.grid(row=2, column=0, columnspan=2)
        self.guess_label = tk.Label(self.mainWin2, text="Enter a letter:", bg="DarkSeaGreen", font=('Times', 14),
                                    fg="pink")
        self.guess_label.grid(row=3, column=0, pady=5)
        self.entry = tk.Entry(self.mainWin2, font=('times', 14))
        self.entry.grid(row=3, column=1, pady=5)
        self.entry.bind("<Return>", self.check_guess)
        self.guess_button = tk.Button(self.mainWin2, text="Guess", bg="SeaGreen", command=self.check_guess,
                                      font='times',
                                      fg="pink")
        self.guess_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.message = tk.Label(self.mainWin2, text="", bg="DarkSeaGreen", font=('Georgia', 14), fg="pink")
        self.message.grid(row=5, column=0, columnspan=2)
        self.attempts = tk.Label(self.mainWin2, text=f"Attempts left: {self.attempts_left}", bg="DarkSeaGreen",
                                 font=('times', 14), fg="pink")
        self.attempts.grid(row=6, column=0, columnspan=2)
        self.hangman_states = [
            "  ____\n |    |\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n |    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\   |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\   |\n/     |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\   |\n/ \   |\n      |\n______|"
        ]
        self.current_hangman_state = 0

    def go(self):
        """enters the tkinter mainloop and displays the main window"""
        self.mainWin2.mainloop()

    def hide_word(self):
        """makes a string that represents the hidden word where un-guessed letters are repalced with underscores"""
        hidden = ''
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                hidden += letter
            else:
                hidden += '_'
        return hidden

    def check_guess(self, event=None):
        """checks the users guessed letter and updates the hangman state and
    display based on whether the guess is correct or not. """
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            self.message.config(text="Please enter a single letter.")
        elif guess in self.guessed_letters:
            self.message.config(text="You already guessed this letter...")
        else:
            self.guessed_letters.append(guess)
            if guess not in self.word_to_guess:
                self.attempts_left -= 1
                self.current_hangman_state += 1
            self.update_game_display()

    def update_game_display(self):
        """updates the visible features of the game like the hidden word, hangman display, and attempts left"""
        hidden_word = self.hide_word()
        self.secret_word.config(text=hidden_word)
        if '_' not in hidden_word:
            self.win2 = tk.Toplevel()
            self.img = img = ImageTk.PhotoImage(Image.open("SampleImagesCS/happySquirrel.jpg"))
            panel = tk.Label(self.win2, image=img)
            panel.grid(row=0, column=0)
            messagebox.showinfo(message="Congratulations! You Guessed the Correct Word!")
            self.disable_input()
        else:
            self.update_hangman_display()
            self.attempts.config(text=f"Attempts Left: {self.attempts_left}")
            if self.attempts_left == 0:
                self.win3 = tk.Toplevel()
                self.img = img = ImageTk.PhotoImage(Image.open("SampleImagesCS/sadSquirrel.jpg"))
                panel = tk.Label(self.win3, image=img)
                panel.grid(row=0, column=0)
                messagebox.showinfo(message="Oh no! Reset Game to try again!")
                self.disable_input()

    def update_hangman_display(self):
        """updates the hangman display based on the current state"""
        if self.current_hangman_state < len(self.hangman_states):
            hangman_state = self.hangman_states[self.current_hangman_state]
            self.hangman_display.config(text=hangman_state)

    def disable_input(self):
        """disables the entry field and guess button to prevent any more inputs during certain game states"""
        self.entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

    def resetGame(self):
        """Resets the game to play again."""
        self.word_to_guess = random.choice(
            ['macalester', 'scots', 'squirrel', 'max', 'duprison', 'coding', 'bob', 'Chouse', 'blue', 'orange',
             'dupringle',
             'Bonner']).lower()
        self.guessed_letters.clear()
        self.message.config(text="")
        self.attempts_left = 6
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.update_game_display()
        self.hangman_display.config(text="")
        self.current_hangman_state = 0

    def doQuit(self):
        """Callback function for the Quit button, closes the main window and ends the event loop."""
        self.mainWin2.destroy()

    def run(self):
        self.mainWin2.mainloop()


myGui = HangmanGame()
myGui.run()
