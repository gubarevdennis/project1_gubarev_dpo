# labyrinth_game/constants.py
# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. '
        'По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти".'
        ' Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. '
          'На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance'},
          'items': ['trash'],
          'puzzle': ('Система плит активна. '
          'Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 
          'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. '
          'Где-то здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Зимой и летом одним цветом?" '
          '(ответ одно слово)', 
                     'елка')  
    },
    'armory': {
          'description': 'Старая оружейная комната. '
          'На стене висит меч, рядом — небольшая бронзовая шкатулка.',
          'exits': {'south': 'library', 'west' : 'storage'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. '
          'Дверь заперта — нужен особый ключ.',
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. '
          'Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10')
    },
    'gazebo': {
        'description': ('Беседка в центре сада. Отсюда открывается вид на сад.'),
        'exits': {'south': 'hall'},
        'items': ['telescope'],
        'puzzle': None,
    },
    'storage': {
        'description': ('Захламленный склад. Здесь полно старых ящиков и коробок.'),
        'exits': {'west': 'gazebo'},
        'items': ['old_boots', 'rope', 'treasure_key'],
        'puzzle': None,
    }
}


# Дополнительные константы
COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"
}