# Number Guessing Game

## Overview

The Number Guessing Game is a simple Python application with a graphical user interface (GUI) built using the `tkinter` library. The game prompts the user to guess a randomly generated number within a specified range. The user has a limited number of attempts to guess the number correctly.

## Features

- Random number generation within a specified range.
- User feedback for guesses (too high, too low, or correct).
- Limited number of attempts.
- Ability to reset the game and start a new round.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python's standard library)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MohamadMamo/Number-Guessing-Game-with-Tkinter.git
   ```
2. **Navigate to the project directory:**

   ```bash
   cd number-guessing-game
   ```

### Running the Game

1. **Run the application:**

   ```bash
   python number_guessing_game.py
   ```

   This will open a graphical window where you can start playing the game.

## How It Works

1. The game initializes with a random target number between 1 and 100.
2. The user is prompted to enter guesses.
3. The application provides feedback on each guess:
   - "Too low!" if the guess is lower than the target number.
   - "Too high!" if the guess is higher than the target number.
   - "Congratulations!" if the guess matches the target number.
4. The user has a maximum number of attempts to guess the number.
5. If the user guesses correctly or exhausts all attempts, the game provides appropriate feedback and disables further guessing.

## Code Overview

- **`number_guessing_game.py`**: Contains the main game logic and GUI implementation using `tkinter`.

### Main Components

- `NumberGuessingGame` class: Encapsulates the game logic and GUI elements.
- `create_widgets` method: Sets up the GUI elements.
- `check_guess` method: Handles user input and provides feedback.
- `reset_game` method: Resets the game for a new round.

## Contributing

1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them with descriptive messages.
4. **Push your changes** to your forked repository.
5. **Create a pull request** to merge your changes into the main repository.

## License

## Acknowledgments

- **Tkinter**: For providing the GUI framework.
- **Python**: For being the programming language used in this project.

### Additional Files

- **LICENSE**: If a license (e.g., MIT License) is included, add a `LICENSE` file to your repository with the appropriate text.

## Screenshots

![Screenshot](screenshot.png)
