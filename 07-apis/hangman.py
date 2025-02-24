import requests
import json 

# Retrieve a random word from an API and keep it in secret
response = requests.get('https://random-word-api.herokuapp.com/word')
data = json.loads(response.text)
secret = data[0]
# secret = "obligation"
print(secret)

# Create the display word with underscores
display_word = secret[0] + ("_" * (len(secret)-2)) + secret[-1]


correct = []
wrong = []

# Repeat until word found OR hanged
while True:
    print(display_word)

    # Ask user to guess
    guess = input("Guess: ")

    # Check guess and put it in correct or wrong list
    if guess in secret and guess not in correct:
        correct.append(guess)
        # if correct, update the display word
        display_word = secret[0]
        for i in range(1, len(secret)-1):
            if secret[i] in correct:
                display_word += secret[i]
            else:
                display_word += "_"
        display_word += secret[-1]
    elif guess not in secret and guess not in wrong:
        wrong.append(guess)

    # if display word is equal to the secret, FOUND and STOP
    if display_word == secret:
        print("Congratulations! FOUND")
        break

    # if wrong guesses are 6, HANGED and STOP
    if len(wrong) == 6:
        print("Sorry, you are HANGED.")
        break