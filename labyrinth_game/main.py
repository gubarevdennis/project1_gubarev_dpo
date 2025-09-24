#!/usr/bin/env python3
# labyrinth_game/main.py

from labyrinth_game import constants
from labyrinth_game import player_actions
from labyrinth_game import utils

def process_command(game_state, command):
    parts = command.split()
    action = parts[0]
    argument = ' '.join(parts[1:]) if len(parts) > 1 else None

    match action:
        case "look":
            utils.describe_current_room(game_state)
        case "go":
            if argument:
                player_actions.move_player(game_state, argument)
            else:
                print("Укажите направление.")
        case "take":
            if argument:
                player_actions.take_item(game_state, argument)
            else:
                print("Укажите, что взять.")
        case "inventory":
            player_actions.show_inventory(game_state)
        case "quit" | "exit":
            game_state['game_over'] = True
        case "help":
            utils.show_help()  # Добавим эту функцию позже
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")

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
        command = player_actions.get_input()
        if command:
            process_command(game_state, command)

if __name__ == "__main__":
    main()