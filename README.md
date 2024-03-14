# Hangman game
## Implement a basic hangman game flow. You can use any (even a constant) word to guess, focus on the guessing logic and the termination of the game.

    1. The game requires the user to guess all the letters belonging to a word.

    2. The initial game state is displayed as _ _ _ _ _ _ _ _ (one underscore for each letter in word).

    3. The game state is displayed as _ o d _ _ o o _ if letters 'd' and 'o' are revealed.

    4. It is possible to make guesses, and letters that occur in the word are revealed.

    5. When a guessed letter does not occur in word, the player loses one life.

    6. When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens.

    7. When a guess is wrong (either a new or a repeated letter), the previous wrong letters are shown to the user.

    8. The player wins when all letters in word are revealed.

    9. The player loses when the number of wrong guesses is higher than the initial value of lives parameter (not counting repeated guesses).

    10. When the player types 'quit' as input, the program says good-bye and terminates.


## Case sensitivity
    1. The gameplay is case insensitive, the word display is case sensitive.

    2. Both uppercase and lowercase letters are considered valid input.

    3. Uppercase and lowercase letter guesses reveal the same letters (e.g. both c and C guesses reveal all the cs in the word, regardless of their case).

    4. Letters of different cases behave as if they were the same when checking repetitions (e.g. entering c after a C would count as a repetition).

    5. On the displaying side, however, letters are revealed as they originally appear in word (e.g. successfully guessing c shows C _ _ _ c _ _ _ for Codecool).


## Graphics
    1. Add ASCII art to visualize lives left.

    2. The game state display is accompanied by an ASCII art depending on the number of lives left.

    3. The art sequence is adapted to the starting value of the lives parameter (at least between 3 and 7) – this means that the game over art is always the same.


## Load words
    1. The game uses a random word from a pre-defined word collection.

    2. The game randomly picks a word at each run.

    3. The game randomly picks a country from countries-and-capitals.txt.


## Different levels
    1. The program allows the user to play on different levels.

    2. The game asks the user to pick a difficulty before starting

    3. The word-pool and the number of lives depend on the chosen level.




