# labyrinth_game/player_actions.py

from labyrinth_game import constants, utils


# Юзаем предметы
def use_item(game_state, item_name):
    if item_name in game_state['player_inventory']:
        match item_name:
            case "torch":
                print("Стало светлее.")
            case "sword":
                print("Теперь вы чувствуете себя увереннее.")
            case "bronze_box":
                if "rusty_key" not in game_state['player_inventory']:
                    print("Вы открываете шкатулку и находите ржавый ключ.")
                    game_state['player_inventory'].append("rusty_key")
                else:
                    print("Шкатулка пуста.")
            case _:
                print("Вы не знаете, как это использовать.")
    else:
        print("У вас нет такого предмета.")
        

# Функция перемещения
def move_player(game_state, direction):
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if direction in room['exits']:
        new_room = room['exits'][direction]

        # Проверка на treasure_room и ключ
        if new_room == 'treasure_room':
            if ('rusty_key' in game_state['player_inventory'] or 
                'treasure_key' in game_state['player_inventory']):
                print("Вы используете найденный ключ, " \
                                "чтобы открыть путь в комнату сокровищ.")
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


# Функция взятия предмета
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if item_name in room['items']:
        game_state['player_inventory'].append(item_name)
        room['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

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