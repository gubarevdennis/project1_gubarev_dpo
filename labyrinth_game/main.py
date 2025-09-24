#!/usr/bin/env python3
# labyrinth_game/main.py

from labyrinth_game import constants
from labyrinth_game import player_actions
from labyrinth_game import utils

# Обработка команд
def process_command(game_state, command):
    parts = command.split()
    action = parts[0]
    argument = ' '.join(parts[1:]) if len(parts) > 1 else None

    # Разрешаем движение по односложным командам (north, south, ...)
    directions = ['north', 'south', 'east', 'west']
    if action in directions:
        argument = action
        action = 'go'

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
        case "use":
            # Проверка условия победы, если игрок в комнате с сокровищами
            if (
                game_state['current_room'] == "treasure_room" and argument == "treasure_chest"
            ):
                utils.attempt_open_treasure(game_state)
            elif argument:
                player_actions.use_item(game_state, argument)
            else:
                print("Укажите, что использовать.")
        case "inventory":
            player_actions.show_inventory(game_state)
        case "solve":
            if game_state['current_room'] == 'treasure_room':
                utils.attempt_open_treasure(game_state)
            else:
                utils.solve_puzzle(game_state)
        case "quit" | "exit":
            game_state['game_over'] = True
        case "help":
            utils.show_help()
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")

def main():
    print("Добро пожаловать в Лабиринт сокровищ!")

    # Состояние игрока
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    # Описываем первую комнату
    utils.describe_current_room(game_state)

    # Основной цикл игры
    while not game_state['game_over']:
        command = player_actions.get_input()
        if command:
            process_command(game_state, command)

if __name__ == "__main__":
    main()