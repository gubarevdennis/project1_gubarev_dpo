# labyrinth_game/utils.py
from labyrinth_game import constants

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