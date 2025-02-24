import requests
import json 

class Hangman:
    def __init__(self):
        self.secret = ''
        self.display_word = ''
        self.wrong = []
        self.correct = []

    def new_game(self):
        response = requests.get('https://random-word-api.herokuapp.com/word')
        data = json.loads(response.text)
        self.secret = data[0]
        self.display_word = self.secret[0] + ("_" * (len(self.secret)-2)) + self.secret[-1]
        self.wrong = []
        self.correct = []

    def found(self):
        return self.secret == self.display_word
    
    def hanged(self):
        return len(self.wrong) == 6
    
    def display(self):
        print(self.display_word)

    def update_display_word(self):
        self.display_word = self.secret[0]
        for i in range(1, len(self.secret)-1):
            if self.secret[i] in self.correct:
                self.display_word += self.secret[i]
            else:
                self.display_word += "_"
        self.display_word += self.secret[-1]

    def play(self, guess):
        if guess in self.secret and guess not in self.correct:
            self.correct.append(guess)
            self.update_display_word()
        elif guess not in self.secret and guess not in self.wrong:
            self.wrong.append(guess)


hangman = Hangman()
hangman.new_game()

while not hangman.found() and not hangman.hanged():
    hangman.display()
    guess = input("Guess: ")
    hangman.play(guess)

if hangman.found():
    print("Congratulations! FOUND")
elif hangman.hanged():
    print("Sorry, you are HANGED.")