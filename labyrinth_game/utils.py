# labyrinth_game/utils.py
from labyrinth_game import constants, player_actions

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