import random 

r = random.randint(1, 100)
print(r)


guess = 0
guesses = 0

while guess != r:
    guess = int(input("Guess: "))
    guesses = guesses + 1

    if guess > r:
        print("GO DOWN")
    elif guess < r:
        print("GO UP")
    else:
        print("FOUND! In", guesses, "Guesses")
