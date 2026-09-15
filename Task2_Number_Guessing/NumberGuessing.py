import random

secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")
print("Guess a number between 1 and 100")

while True:
    attempts += 1

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("You guessed it in", attempts, "attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")