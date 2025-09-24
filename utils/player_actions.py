# labyrinth_game/player_actions.py

from labyrinth_game import constants, utils


def move_player(game_state, direction):
    """Перемещает игрока в указанном направлении."""
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if direction in room['exits']:
        new_room = room['exits'][direction]

        # Проверка на treasure_room и ключ
        if new_room == 'treasure_room':
            if (
                'rusty key' in game_state['player_inventory']
                or 'treasure_key' in game_state['player_inventory']
            ):
                print(
                    "Вы используете найденный ключ, чтобы открыть путь в комнату"
                    " сокровищ."
                )
                game_state['current_room'] = new_room
                game_state['steps_taken'] += 1
                utils.describe_current_room(game_state)
                utils.random_event(game_state)  # Вызываем случайное событие
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
        else:
            game_state['current_room'] = new_room
            game_state['steps_taken'] += 1
            utils.describe_current_room(game_state)
            utils.random_event(game_state)  # Вызываем случайное событие
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """Позволяет игроку взять предмет из текущей комнаты."""
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if item_name in room['items']:
        game_state['player_inventory'].append(item_name)
        room['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def show_inventory(game_state):
    """Показывает содержимое инвентаря игрока."""
    if game_state['player_inventory']:
        print("Ваш инвентарь:")
        for item in game_state['player_inventory']:
            print(f"  - {item}")
    else:
        print("Ваш инвентарь пуст.")


def get_input(prompt="> "):
    """Получает ввод от пользователя."""
    try:
        user_input = input(prompt)
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def use_item(game_state, item_name):
    """Использует предмет из инвентаря игрока."""
    if item_name in game_state['player_inventory']:
        match item_name:
            case "torch":
                print("Стало светлее.")
            case "sword":
                print("Вы чувствуете себя увереннее.")
            case "bronze box":
                if "rusty key" not in game_state['player_inventory']:
                    print("Вы открываете шкатулку и находите ржавый ключ.")
                    game_state['player_inventory'].append("rusty key")
                else:
                    print("Шкатулка пуста.")
            case _:
                print("Вы не знаете, как это использовать.")
    else:
        print("У вас нет такого предмета.")
