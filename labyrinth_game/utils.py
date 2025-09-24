# labyrinth_game/utils.py
import math
from labyrinth_game import constants, player_actions

# Случайности не случайны
def random_event(game_state):
    if pseudo_random(game_state['steps_taken'], 10) == 0:
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
                if game_state['current_room'] == 'trap_room' and 'torch' not in game_state['player_inventory']:
                    print("Вы чувствуете опасность...")
                    trigger_trap(game_state)

# Ловушки повсюду
def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    if game_state['player_inventory']:
        index = pseudo_random(game_state['steps_taken'], len(game_state['player_inventory']))
        lost_item = game_state['player_inventory'].pop(index)
        print(f"Вы потеряли: {lost_item}")
    else:
        damage = pseudo_random(game_state['steps_taken'], 10)
        if damage < 3:
            print("Вы не смогли удержаться и упали в пропасть. Игра окончена!")
            game_state['game_over'] = True
        else:
            print("Вам удалось удержаться! Вы получили легкий ушиб.")

# Немного случайности в путешествии
def pseudo_random(seed, modulo):
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = x - math.floor(x)
    return int(fractional_part * modulo)

# Условие победы
def attempt_open_treasure(game_state):
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if 'treasure_chest' not in room['items']:
        print("Сундук уже открыт или отсутствует.")
        return

    if 'treasure_key' in game_state['player_inventory'] or 'rusty_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        choice = player_actions.get_input("Сундук заперт. Хотите попробовать ввести код? (да/нет): ")
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

# Функция решения загадок
def solve_puzzle(game_state):
    current_room = game_state['current_room']
    room = constants.ROOMS[current_room]

    if room['puzzle'] is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = room['puzzle']
    print(question)
    answer = player_actions.get_input("Ваш ответ: ")

    # Если вдруг введут слово ДЕСЯТЬ прописью
    if answer == 'десять': 
        answer = '10'

    if answer.lower() == correct_answer.lower():
        print("Верно!")
        room['puzzle'] = None  # Убираем загадку, чтобы нельзя было решить дважды

        # Награда:
        print("Вы получаете золотые монеты.")
        game_state['player_inventory'].append("горсть золотых монет")
    else:
        print("Неверно. Попробуйте снова.")

# Описание текущей комнаты
def describe_current_room(game_state):
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

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")