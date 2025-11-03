# labyrinth_game/utils.py

# Импортируем переменную ROOMS из constants
from labyrinth_game.constants import ROOMS 

# Импортируем функцию get_input
from labyrinth_game.player_actions import get_input

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

# 2. Функция решения загадок
def solve_puzzle(game_state):
  
    # Определяем в какой комнате находимся
    current_room = game_state['current_room']
    
    # Если в комнате есть загадка выводим закадку и предлагаем ответить
    if ROOMS[current_room]['puzzle'] is not None:
       
        # Объявляем переменную puz, в которую считываем загадку из ROOMS
        puz = ROOMS[current_room]['puzzle'][0]
        # Объявляем переменную ans, в которую считываем ответ из ROOMS
        ans = ROOMS[current_room]['puzzle'][1]

        print(f'\nВ комнате есть закадка: {puz}')

        # Объявляем переменную user_ans и запрашиваем ответ пользователя
        user_ans = get_input('\nВаш ответ: ')

        # Проверяем правильность ответа
        if user_ans == ans:
            print('\nЭто правильный ответ!')
            ROOMS[current_room]['puzzle'] = None
        # В случае нажатия ctrl + c фиксируем отказ
        elif user_ans == 'quit': 
             print('\nВы отказались отгадывать загадку')
        else:
            print('\nНеверно. Попробуйте снова.')

    # Если в комнате нет загадок выводим сообщение
    else:
        print('\nЗагадок здесь нет.')

