import random

class HangmanApp:

    def __init__(self, interface):
        self.wordlist = ["python", "programming", "computer", "game", "challenge"]
        self.interface = interface
        self.secretword = random.choice(self.wordlist).lower()
        self.letter_list = list(self.secretword)
        self.new_list = ["_"] * len(self.secretword)
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

    def guess(self):
        while self.incorrect_guesses < self.max_incorrect_guesses and "_" in self.new_list:
            self.interface.display(self.new_list)
            print(f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
            print(f"Guessed letters: {', '.join(sorted(self.interface.guessed_letters))}")
            hasattr
            guess = self.interface.get_guess(self.interface.guessed_letters)
            self.interface.guessed_letters.add(guess)

            if guess in self.letter_list:
                for i, letter in enumerate(self.letter_list):
                    if letter == guess:
                        self.new_list[i] = guess
                self.interface.correct(self.new_list)
            else:
                self.incorrect_guesses += 1
                self.interface.incorrect(self.new_list)

        if self.incorrect_guesses >= self.max_incorrect_guesses:
            print(f"Sorry, you've run out of guesses. The word was: {self.secretword}")
        else:
            print(f"Congratulations! You've guessed the word: {self.secretword}")

class textInterface:

    def __init__(self):
        self.guessed_letters = set()
        print("Welcome to Hangman!")

    def get_guess(self, already_guessed):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            elif guess in already_guessed:
                print("You already guessed that letter. Try again.")
            else:
                return guess

    def display(self, word):
        string = ' '.join(word)
        print(string)

    def incorrect(self, word):
        print("Nope, try again.")
        self.display(word)

    def correct(self, word):
        print("Correct!")
        self.display(word)

def main():
    inter = textInterface()
    app = HangmanApp(inter)
    app.guess()

if __name__ == "__main__":
    main()
