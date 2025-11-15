import random
from models.results import save_result, get_history

# Dictionary to track ongoing games
# Format: {player_name: {"secret_number": int, "attempts_left": int, "difficulty": str, "max_attempts": int, "used_attempts": int}}
active_games = {}

def start_game_api(player: str, difficulty: str):
    difficulties = {"Easy": 10, "Medium": 7, "Hard": 5}
    if difficulty not in difficulties:
        return {"error": "Invalid difficulty"}
    
    max_attempts = difficulties[difficulty]
    secret_number = random.randint(1, 100)
    
    active_games[player] = {
        "secret_number": secret_number,
        "attempts_left": max_attempts,
        "difficulty": difficulty,
        "max_attempts": max_attempts,
        "used_attempts": 0
    }
    
    return {"message": f"Game started for {player}", "difficulty": difficulty, "max_attempts": max_attempts}

def make_guess_api(player: str, guess: int):
    if player not in active_games:
        return {"error": "No active game found for this player. Start a game first."}

    game = active_games[player]
    game["used_attempts"] += 1
    game["attempts_left"] -= 1
    secret_number = game["secret_number"]

    if guess < secret_number:
        result = "Too low"
    elif guess > secret_number:
        result = "Too high"
    else:
        result = "Correct"
        save_result(player, game["difficulty"], game["used_attempts"], game["max_attempts"], secret_number, "WIN")
        del active_games[player]  # End the game
        return {"result": result, "message": f"🎉 You guessed the number {secret_number}!", "attempts_used": game["used_attempts"]}

    if game["attempts_left"] == 0:
        save_result(player, game["difficulty"], game["used_attempts"], game["max_attempts"], secret_number, "LOSE")
        del active_games[player]  # End the game
        return {"result": result, "message": f"❌ Out of attempts! The number was {secret_number}"}

    return {"result": result, "attempts_left": game["attempts_left"]}
