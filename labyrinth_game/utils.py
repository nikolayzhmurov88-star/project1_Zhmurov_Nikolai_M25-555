# labyrinth_game/utils.py

# Импортируем переменную ROOMS из constants
from labyrinth_game.constants import ROOMS 

# Импортируем функцию get_input
from labyrinth_game.player_actions import get_input

# Импортируем math
import math

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
        
# 3. Функция определяющая логику победы в игре
def attempt_open_treasure(game_state):
    
    # Проверяем есть ли в инвентаре игрока treasure_key
    if 'treasure_key' in game_state['player_inventory']:
        
        # Выводим сообщение, что сундук открыт
        print('\nВы применяете ключ, и замок щёлкает. Сундук открыт!')
        
        # Удаляем сундук из предметов комнаты
        ROOMS['treasure_room']['items'][0] = None
        
        # Сообщаем о победе
        print('\nВ сундуке сокровище! Вы победили!\n')
        
		# Завершаем игру
        game_state['game_over'] = True

	# Если ключа нет, другой порядок действий    
    else: 
        
		# Сообщаем, что сундук заперт и спрашиваем хочет ли игрок ввести код
        command = get_input('\nСундук заперт. ... Ввести код? (да/нет) ')
        
		#  Используем match/case для перебора условий
        match command:
            #Если ответ да
            case 'да' | 'yes':
                
                # Объявляем переменную puz, в которую считываем загадку из ROOMS
                puz = ROOMS['treasure_room']['puzzle'][0]
            
                # Объявляем переменную ans, в которую считываем ответ из ROOMS
                ans = ROOMS['treasure_room']['puzzle'][1]
            
			    # Объявляем переменную для ответа пользоватея
                user_ans = ' ' 
                
				#Объявляем цикл, чтобы при неверном ответе не выбрасывало опять к вводу команды solve            
                while user_ans != ans:
                    # Выводим запрос на ввод кода
                    print(f'\n{puz}')
                 
				    # Присваиваем переменной user_ans ответ пользователя
                    user_ans = get_input('\nВведите код: ')
                    
				    # Проверяем правильность ответа, если ответ правильный
                    if user_ans == ans:
                         
				        # Выводим сообщение о правильном ответе  и победе
                        print('\nЭто правильный ответ! В сундуке сокровище! Вы победили!\n')
                              
                        # Удаляем сундук из предметов комнаты
                        ROOMS['treasure_room']['items'][0] = None
                              
                        #Завершаем игру
                        game_state['game_over'] = True
                    
					# В случае нажатия ctrl + c фиксируем отказ
                    elif user_ans == 'quit': 
                        print('\nВы отказались вводить код')
                        break
                    
					# В случае неправильного ответа ссобщаем, что ответ не верный и переходим к повторному вводу
                    else:
                        print('\nКод неверный. Попробуйте снова.')
                

		    # Если игрок изначально отказался вводить код        
            case 'нет'|'no'|'quit':
                print('\nВы отступаете от сундука.')
                
             
            # Если игрок вводит ни да, ни нет
            case _:
                print('\nНепонятный ответ! Вы отступаете от сундука!') 

# 4. Функция для случайных событий
   
def pseudo_random(seed, modulo) -> int:
    # Берем синус от seed, умноженного на константу с дробной частью
    x = math.sin(seed * 12.9898)
    # "Размазываем" значения, умножая на другую константу
    x *= 43758.5453
    # Вычитаем целую часть, чтобы получить дробную часть (число в [0, 1))
    fractional_part = x - math.floor(x)
    # Масштабируем к нужному диапазону [0, modulo)
    result = int(fractional_part * modulo)
    return result



       
# Функция помощи
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
	

