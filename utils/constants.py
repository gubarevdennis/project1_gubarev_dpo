# labyrinth_game/constants.py

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None,
    },
    'hall': {
        'description': (
            'Большой зал с эхом. По центру стоит пьедестал'
            ' с запечатанным сундуком.'
        ),
        'exits': {
            'south': 'entrance',
            'west': 'library',
            'north': 'treasure_room',
            'east': 'kitchen',
        },
        'items': [],
        'puzzle': (
            'На пьедестале надпись: "Назовите число, которое идет'
            ' после девяти". Введите ответ цифрой или словом.',
            '10',
        ),
    },
    'trap_room': {
        'description': (
            'Комната с хитрой плиточной поломкой. На стене видна'
            ' надпись: "Осторожно — ловушка".'
        ),
        'exits': {'west': 'entrance', 'south': 'sewer'},
        'items': ['rusty key'],
        'puzzle': (
            'Система плит активна. Чтобы пройти, назовите слово "шаг"'
            ' три раза подряд (введите "шаг шаг шаг")',
            'шаг шаг шаг',
        ),
    },
    'library': {
        'description': (
            'Пыльная библиотека. На полках старые свитки. Где-то здесь'
            ' может быть ключ от сокровищницы.'
        ),
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient book'],
        'puzzle': (
            'В одном свитке загадка: "Что растет, когда его съедают?"'
            ' (ответ одно слово)',
            'резонанс',
        ),
    },
    'armory': {
        'description': (
            'Старая оружейная комната. На стене висит меч, рядом'
            ' — небольшая бронзовая шкатулка.'
        ),
        'exits': {'south': 'library', 'east': 'storage'},
        'items': ['sword', 'bronze box'],
        'puzzle': None,
    },
    'treasure_room': {
        'description': (
            'Комната, на столе большой сундук. Дверь заперта'
            ' — нужен особый ключ.'
        ),
        'exits': {'south': 'hall'},
        'items': ['treasure chest'],
        'puzzle': (
            'Дверь защищена кодом. Введите код (подсказка:'
            ' это число пятикратного шага, 2*5= ? )',
            '10',
        ),
    },
    'kitchen': {
        'description': (
            'Кухня. На столе остатки еды, в углу стоит огромный котел.'
        ),
        'exits': {'west': 'hall'},
        'items': ['knife', 'rotten apple'],
        'puzzle': None,
    },
    'sewer': {
        'description': (
            'Темный и сырой туннель канализации. Слышны звуки капающей'
            ' воды.'
        ),
        'exits': {'north': 'trap_room', 'east': 'dungeon'},
        'items': ['rat'],
        'puzzle': None,
    },
    'dungeon': {
        'description': (
            'Мрачное подземелье. Стены покрыты плесенью, в углу виднеется'
            ' скелет.'
        ),
        'exits': {'west': 'sewer'},
        'items': ['chains'],
        'puzzle': None,
    },
    'garden': {
        'description': (
            'Заброшенный сад. Цветы давно увяли, но воздух все еще свеж.'
        ),
        'exits': {'west': 'treasure_room', 'north': 'gazebo'},
        'items': ['shovel'],
        'puzzle': None,
    },
    'gazebo': {
        'description': (
            'Беседка в центре сада. Отсюда открывается вид на окрестности.'
        ),
        'exits': {'south': 'garden'},
        'items': ['telescope'],
        'puzzle': None,
    },
    'storage': {
        'description': (
            'Захламленный склад. Здесь полно старых ящиков и коробок.'
        ),
        'exits': {'west': 'armory'},
        'items': ['old boots', 'rope'],
        'puzzle': None,
    },
}

COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение",
}