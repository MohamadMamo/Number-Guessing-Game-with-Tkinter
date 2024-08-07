import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("350x300")
        self.root.resizable(False, False)  # Disable window resizing
        
        # Game settings
        self.lower_bound = 1
        self.upper_bound = 100
        self.max_attempts = 10
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Instructions
        self.instructions = tk.Label(self.root, text=f"I'm thinking of a number between {self.lower_bound} and {self.upper_bound}.", wraplength=280)
        self.instructions.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry for user guess
        self.guess_entry = tk.Entry(self.root, width=15, font=("Arial", 14))
        self.guess_entry.grid(row=1, column=0, padx=10, pady=10)

        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, width=15)
        self.guess_button.grid(row=1, column=1, padx=10, pady=10)

        # Feedback label
        self.feedback = tk.Label(self.root, text="", wraplength=280)
        self.feedback.grid(row=2, column=0, columnspan=2, pady=10)

        # Attempts remaining
        self.attempts_label = tk.Label(self.root, text=f"Attempts remaining: {self.max_attempts}", font=("Arial", 12))
        self.attempts_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, width=15)
        self.reset_button.grid(row=4, column=0, columnspan=2, pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback.config(text="Please enter a valid integer.")
            return

        if guess < self.lower_bound or guess > self.upper_bound:
            self.feedback.config(text=f"Please guess a number between {self.lower_bound} and {self.upper_bound}.")
            return

        self.attempts += 1
        remaining_attempts = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts remaining: {remaining_attempts}")

        if guess < self.target_number:
            self.feedback.config(text="Too low!")
        elif guess > self.target_number:
            self.feedback.config(text="Too high!")
        else:
            self.feedback.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts!")
            self.guess_button.config(state=tk.DISABLED)
            return

        if self.attempts >= self.max_attempts:
            self.feedback.config(text=f"Sorry, you've used all {self.max_attempts} attempts. The number was {self.target_number}.")
            self.guess_button.config(state=tk.DISABLED)

    def reset_game(self):
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        self.feedback.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.attempts_label.config(text=f"Attempts remaining: {self.max_attempts}")

# Create the main window
root = tk.Tk()
game = NumberGuessingGame(root)

# Run the application
root.mainloop()
