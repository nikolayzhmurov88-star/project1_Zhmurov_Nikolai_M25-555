# labyrinth_game/constants.py

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room', 'east': 'garden'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance', 'south': 'secret_passage'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')  
    },
    'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10')

	# Новые комнаты
    },
    'garden': {
          'description': 'Заброшенный сад с фонтаном. Вода давно высохла, но в центре фонтана что-то блестит.',
          'exits': {'west': 'hall', 'north': 'observatory'},
          'items': ['silver_key'],
          'puzzle': ('На фонтане выгравировано: "Что принадлежит вам, но другие используют это чаще?" (ответ в именительном падеже)', 'имя')
    },
    'observatory': {
          'description': 'Круглая комната с разбитым телескопом. Звездные карты покрывают стены.',
          'exits': {'south': 'garden'},
          'items': ['star_chart'],
          'puzzle': ('На одной из карт надпись: "Сколько планет в Солнечной системе?" (ответ цифрой)', '8')
    },
    'secret_passage': {
          'description': 'Узкий темный коридор. В углу виден маленький сундук, покрытый пылью.',
          'exits': {'north': 'trap_room'},
          'items': ['treasure_key'],
          'puzzle': (
              ('Сундук закрыт на замок. На нем написано: "Я легкий как перо, но даже самый '
               'сильный человек не может удержать меня долго. Что я?'),
            'дыхание')
    }
}


# Константа для функции случайных событий
EVENT_PROBABILITY = 10

# Константа порог ущерба
DEMAGE_LIMIT = 3

# Константа количество случайных событий (в нашем случае равна трем для трех видов событий)
EVENT_COUNT = 3

# Константа словарь команд в функции show_help

COMMANDS = {
    "north/south/east/west": "перейти в соответствующем направлении",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>":  "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve":  "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"       
    }


PUZZLE_ALTERNATIVES = {
    'hall': ['10', 'десять', 'ten', 'десять'],
    'trap_room': ['шаг шаг шаг', 'step step step', 'steps steps steps', 'шагшагшаг'],
    'library': ['резонанс', 'resonance', 'эхо', 'echo', 'звук'],
    'garden': ['имя', 'name', 'мое имя', 'my name'],
    'observatory': ['8', 'восемь', 'eight', '8 планет'],
    'secret_passage': ['дыхание', 'breath', 'breathing', 'воздух']
}


PUZZLE_REWARDS = {
    'hall': 'gold_coin',
    'trap_room': 'secret_map',
    'library': 'ancient_book',
    'garden': 'crystal_flower',
    'observatory': 'telescope_lens',
    'secret_passage': 'hidden_key'
}