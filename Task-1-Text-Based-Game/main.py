import random

print("=" * 40)
print("Welcome to Number Guessing Game")
print("=" * 40)

secret_number = random.randint(1, 100)

attempts = 0

print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations! You guessed the correct number.")
            print(f"You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")
