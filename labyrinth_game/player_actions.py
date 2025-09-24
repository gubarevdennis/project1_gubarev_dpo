# labyrinth_game/player_actions.py

from labyrinth_game import constants
from labyrinth_game import utils

def move_player(game_state, direction):
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if direction in room['exits']:
        new_room = room['exits'][direction]
        game_state['current_room'] = new_room
        game_state['steps_taken'] += 1
        utils.describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def show_inventory(game_state):
    if game_state['player_inventory']:
        print("Ваш инвентарь:")
        for item in game_state['player_inventory']:
            print(f"  - {item}")
    else:
        print("Ваш инвентарь пуст.")

def get_input(prompt="> "):
    try:
        user_input = input(prompt)
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"