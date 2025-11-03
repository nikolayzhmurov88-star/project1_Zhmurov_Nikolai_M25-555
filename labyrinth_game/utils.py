# labyrinth_game/utils.py

# Импортируем переменную ROOMS из constants
from labyrinth_game.constants import ROOMS 

# 1. Функция описания комнаты с аргументом game_state
def describe_current_room(game_state):
    
    # Объявляем переменную room с помощью цепочки обращений
    room = ROOMS[game_state['current_room']]

    # Выводим название комнаты в верхнем регистре с помощью метода .upper()
    print(f"\n== {game_state['current_room'].upper()} ==")
    
    # Выводим описание комнаты
    print(f"\n{room['description']}")
    
    # Выводим список видимых предметов, если список будет пуст [], то вывода не будет, join объединяет все предметы в одну строку
    if room['items']:
        print(f"\nЗаметные предметы: {', '.join(room['items'])}")
    
    # Выводим доступные выходы, join объединяет строки, keys выводит ключи словаря
    print(f"\nВыходы: {', '.join(room['exits'].keys())}")
    
    # Выводим сообщение о наличии загадки, если она есть, при значении none вывода не будет
    if room['puzzle']:
        print("\nКажется, здесь есть загадка (используйте команду solve).")
