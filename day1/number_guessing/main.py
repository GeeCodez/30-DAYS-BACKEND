from db.connection import initialize_database
from game.logic import play_game, show_history

print("🎯 Welcome to the Number Guessing Game (Version 6 - Structured)")

# create tables
initialize_database()

player_name = input("Enter your name: ").strip()

while True:
    print("""
Menu:
1. Play Game
2. View History
3. Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        play_game(player_name)
    elif choice == "2":
        show_history(player_name)
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid option.\n")
