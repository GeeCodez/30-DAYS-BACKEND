from fastapi import APIRouter
from pydantic import BaseModel
from game.logic import start_game_api, make_guess_api
from models.results import get_history

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the Number Guessing Game API"}

@router.get("/history/{player}")
def history(player: str):
    rows = get_history(player)
    return {"player": player, "history": rows}

class StartGameRequest(BaseModel):
    player: str
    difficulty: str

@router.post("/game/start")
def start_game(request: StartGameRequest):
    return start_game_api(request.player, request.difficulty)

class GuessRequest(BaseModel):
    player: str
    guess: int

@router.post("/game/guess")
def make_guess(request: GuessRequest):
    return make_guess_api(request.player, request.guess)
