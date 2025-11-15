import random
from models.result import save_result, get_history

def choose_difficulty():
    while True:
        print("""
Choose difficulty:
1. Easy   (10 attempts)
2. Medium (7 attempts)
3. Hard   (5 attempts)
        """)
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return "Easy", 10
        elif choice == "2":
            return "Medium", 7
        elif choice == "3":
            return "Hard", 5
        else:
            print("Invalid choice. Try again.\n")


def get_guess():
    while True:
        guess = input("Enter your guess (1–100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Guess must be between 1 and 100.")
        else:
            print("Invalid input. Enter a number.")


def play_game(player):
    difficulty, attempts = choose_difficulty()
    secret_number = random.randint(1, 100)
    max_attempts = attempts
    used_attempts = 0

    print("\nI have chosen a number between 1 and 100. Try to guess it!")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = get_guess()
        used_attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {used_attempts} attempts.\n")

            save_result(player, difficulty, used_attempts, max_attempts, secret_number, "WIN")
            return

        attempts -= 1

    print("\n❌ You're out of attempts!")
    print(f"The correct number was {secret_number}.")
    print(f"You used {used_attempts} attempts.\n")

    save_result(player, difficulty, used_attempts, max_attempts, secret_number, "LOSE")


def show_history(player):
    print("\n📜 Your Game History:\n")
    rows = get_history(player)

    if not rows:
        print("No records found.\n")
        return

    for row in rows:
        print(f"""
Game ID: {row[0]}
Player: {row[1]}
Difficulty: {row[2]}
Attempts Used: {row[3]} / {row[4]}
Secret Number: {row[5]}
Status: {row[6]}
Time: {row[7]}
-----------------------------------------
        """)
