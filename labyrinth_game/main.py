#!/usr/bin/env python3
# labyrinth_game/main.py

from labyrinth_game import constants
from labyrinth_game import player_actions
from labyrinth_game import utils

def main():
    print("Добро пожаловать в Лабиринт сокровищ!")

    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    utils.describe_current_room(game_state) 

    while not game_state['game_over']:
        command = player_actions.get_input() # Получаем команду от игрока
        print(f"Вы ввели команду: {command}") # Временно выводим для отладки

if __name__ == "__main__":
    main()