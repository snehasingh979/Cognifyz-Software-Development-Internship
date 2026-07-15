import random

print("=" * 40)
print("🎮 Welcome to Number Guessing Game 🎮")
print("=" * 40)

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    try:
        guess = int(input("\nEnter a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("❌ Please enter a number between 1 and 10.")
            continue

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the correct number.")
            break

        elif guess < secret_number:
            print("📉 Too Low!")

        else:
            print("📈 Too High!")

        attempts -= 1

        if attempts > 0:
            print(f"💡 Attempts Left: {attempts}")

    except ValueError:
        print("❌ Invalid input! Please enter a number only.")

else:
    print("\n😔 Game Over!")
    print(f"The correct number was: {secret_number}")

print("\n✨ Thank you for playing!")
