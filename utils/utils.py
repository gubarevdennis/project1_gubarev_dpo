# labyrinth_game/utils.py

import math

from labyrinth_game import constants, player_actions

EVENT_PROBABILITY = 10  # Вероятность случайного события
TRAP_DAMAGE_THRESHOLD = 3  # Порог урона для ловушки


def describe_current_room(game_state):
    """Описывает текущую комнату."""
    room_name = game_state['current_room']
    room = constants.ROOMS[room_name]

    print(f"== {room_name.upper()} ==")
    print(room['description'])

    if room['items']:
        print("Заметные предметы:")
        for item in room['items']:
            print(f"  - {item}")

    if room['exits']:
        print("Выходы:")
        for direction, exit_room in room['exits'].items():
            print(f"  - {direction}: {exit_room}")

    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    """Предлагает решить загадку в текущей комнате."""
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if room['puzzle'] is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = room['puzzle']
    print(question)
    answer = player_actions.get_input("Ваш ответ: ")

    # Альтернативные варианты ответа
    alternative_answers = {'10': ['десять']}

    if (
        answer.lower() == correct_answer.lower()
        or (
            correct_answer in alternative_answers
            and answer.lower() in alternative_answers[correct_answer]
        )
    ):
        print("Верно!")
        room['puzzle'] = None  # Убираем загадку, чтобы нельзя было решить дважды

        # Награда в зависимости от комнаты
        match current_room:
            case 'hall':
                print("Вы получаете сокровищницу: 'treasure_key'.")
                game_state['player_inventory'].append("treasure_key")
            case 'library':
                print("Вы получаете ключ: 'rusty_key'.")
                game_state['player_inventory'].append("rusty_key")
            case _:
                print("Вы ничего не получили.")  # Для других комнат
    else:
        print("Неверно. Попробуйте снова.")
        if current_room == 'trap_room':
            trigger_trap(game_state)


def attempt_open_treasure(game_state):
    """Пытается открыть сундук с сокровищами."""
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if 'treasure_chest' not in room['items']:
        print("Сундук уже открыт или отсутствует.")
        return

    if (
        'treasure_key' in game_state['player_inventory']
        or 'rusty key' in game_state['player_inventory']
    ):
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        choice = player_actions.get_input(
            "Сундук заперт. Хотите попробовать ввести код? (да/нет): "
        )
        if choice.lower() == 'да':
            code = player_actions.get_input("Введите код: ")
            if room['puzzle'] and code.lower() == room['puzzle'][1].lower():
                print("Вы вводите правильный код, и сундук открывается!")
                room['items'].remove('treasure_chest')
                print("В сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
            else:
                print("Неверный код.")
        else:
            print("Вы отступаете от сундука.")


def show_help():
    """Выводит список доступных команд."""
    from labyrinth_game import constants  # Moved import here

    print("\nДоступные команды:")
    for command, description in constants.COMMANDS.items():
        print(f"  {command:<16} - {description}")


def pseudo_random(seed, modulo):
    """Генерирует псевдослучайное число в диапазоне [0, modulo)."""
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = x - math.floor(x)
    return int(fractional_part * modulo)


def trigger_trap(game_state):
    """Имитирует срабатывание ловушки."""
    print("Ловушка активирована! Пол стал дрожать...")
    if game_state['player_inventory']:
        index = pseudo_random(
            game_state['steps_taken'], len(game_state['player_inventory'])
        )
        lost_item = game_state['player_inventory'].pop(index)
        print(f"Вы потеряли: {lost_item}")
    else:
        damage = pseudo_random(game_state['steps_taken'], 10)
        if damage < TRAP_DAMAGE_THRESHOLD:
            print("Вы не смогли удержаться и упали в пропасть. Игра окончена!")
            game_state['game_over'] = True
        else:
            print("Вам удалось удержаться! Вы получили легкий ушиб.")


def random_event(game_state):
    """Реализует случайные события."""
    if pseudo_random(game_state['steps_taken'], EVENT_PROBABILITY) == 0:
        event = pseudo_random(game_state['steps_taken'], 3)  # 3 - количество сценариев
        match event:
            case 0:
                print("Вы нашли на полу монетку!")
                current_room = game_state['current_room']
                constants.ROOMS[current_room]['items'].append('coin')
            case 1:
                print("Вы слышите шорох...")
                if 'sword' in game_state['player_inventory']:
                    print("Вы обнажили меч и отпугнули существо.")
            case 2:
                if (
                    game_state['current_room'] == 'trap_room'
                    and 'torch' not in game_state['player_inventory']
                ):
                    print("Вы чувствуете опасность...")
                    trigger_trap(game_state)
