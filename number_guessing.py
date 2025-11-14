import random

print("🎯 Welcome to the Number Guessing Game!")

def choose_difficulty():
    """Return number of attempts based on difficulty."""
    while True:
        print("""
Choose difficulty:
1. Easy   (10 attempts)
2. Medium (7 attempts)
3. Hard   (5 attempts)
        """)

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Try again.\n")


def get_guess():
    """Return a valid number between 1 and 100."""
    while True:
        guess = input("Enter your guess (1–100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Your guess must be between 1 and 100.")
        else:
            print("Invalid input. Enter a number.")


def play_game():
    """Main game logic."""
    attempts = choose_difficulty()
    secret_number = random.randint(1, 100)
    used_attempts = 0

    print("\nI have chosen a number between 1 and 100. Can you guess it?")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = get_guess()
        used_attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {used_attempts} attempts.\n")
            return

        attempts -= 1

    print("\n❌ You're out of attempts!")
    print(f"The correct number was {secret_number}.")
    print(f"You used {used_attempts} attempts.\n")


# Main loop
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again == "no" or again == "n":
        print("Goodbye! 👋")
        break