# labyrinth_game/utils.py

# Импортируем переменную ROOMS из constants
from labyrinth_game.constants import ROOMS 

# Импортируем константу EVENT_PROBABILITY
from labyrinth_game.constants import EVENT_PROBABILITY

# Импортируем константу EVENT_COUNT
from labyrinth_game.constants import EVENT_COUNT

# Импортируем константу DEMAGE_LIMIT
from labyrinth_game.constants import DEMAGE_LIMIT

# Импортируем константу PUZZLE_ALTERNATIVES
from labyrinth_game.constants import PUZZLE_ALTERNATIVES

# Импортируем константу PUZZLE_REWARDS
from labyrinth_game.constants import PUZZLE_REWARDS

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
        
        # Если функция get_input вернула словарь, то делаем опять строку
        if isinstance(user_ans, list):
            user_ans = ' '.join(user_ans)
            

        # Проверяем правильность ответа
        if user_ans == ans or user_ans in PUZZLE_ALTERNATIVES[current_room]:
            print('\nЭто правильный ответ!')

            # Удаляем загадку из игры
            ROOMS[current_room]['puzzle'] = None

            # Выводим сообщение о награде
            print(f'\nВы получаете награду {PUZZLE_REWARDS[current_room]}')

            # Добавляем награду в инвентарь
            game_state['player_inventory'].append(PUZZLE_REWARDS[current_room])

        # В случае нажатия ctrl + c фиксируем отказ
        elif user_ans == 'quit': 
             print('\nВы отказались отгадывать загадку')
        else:
            # Если не находимся в trap_room то посто фиксируем неверный ответ
            if current_room != 'trap_room':
                print('\nНеверно. Попробуйте снова.')

            # Если в trap_room, то срабатывает ловушка
            else:
                trigger_trap(game_state)


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
        ROOMS['treasure_room']['items'].remove('treasure_chest')
        
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
                        ROOMS['treasure_room']['items'].remove('treasure_chest')
                              
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


# 4. Функция для случайных собитий (генерация случайных чисел)
def pseudo_random(seed, modulo):
    # Берем синус от seed, умноженного на константу с дробной частью
    x = math.sin(seed * 12.9898)

    # "Размазываем" значения, умножая на другую константу
    x *= 43758.5453

    # Вычитаем целую часть, чтобы получить дробную часть (число в [0, 1))
    fractional_part = x - math.floor(x)

    # Масштабируем к нужному диапазону [0, modulo)
    result = int(fractional_part * modulo)
    return result


# 5. Функция срабатывания ловушки
def trigger_trap(game_state):

    # Сообщении о том, что сработала ловушка
    print('\nЛовушка активирована! Пол стал дрожать...')

    # Проверяем есть ли что-то в инвентаре, если есть забираем случайный предмет
    if game_state['player_inventory'] != []:

        # Считаем количество предметов в инвентаре
        inventory_count = len(game_state['player_inventory'])

        # Генерируем индекс предмета, который будем удалять
        del_item = pseudo_random(game_state['steps_taken'], inventory_count)
        
        # Удаляем предмет из инвентаря 
        print(f'Из инвентаря пропал {game_state['player_inventory'][del_item]}')
        del game_state['player_inventory'][del_item]
        

    # Если инвентарь пуст
    else:
        # Генерируем число определяющее урон
        demage = pseudo_random(game_state['steps_taken'], EVENT_PROBABILITY)
        
        # Если число ниже порога, игрок погибает и игра заканчивается
        if demage < DEMAGE_LIMIT:
            print('\nВы получили критический урон и проиграли!\n\nИгра окончена!\n')
            game_state['game_over'] = True

        # Иначе выводим сообщение, что грок уцелел
        else:
            print('\nВы получили урон но уцелели!')


# 6. Функция обработки случайных событий
def random_event(game_state):

    # Определяем произойдет ли событие вообще
    event = pseudo_random(game_state['steps_taken'], EVENT_PROBABILITY)
    if event == 5:

        # Определяем какое имненно событие случится
        event_num = pseudo_random(game_state['steps_taken'], EVENT_COUNT)
    
        # Обрабатываем события для разных случайных чисел
        match event_num:

            # Нашли монетку
            case 0:
                print('\nВы увидели монетку на полу, ее можно подобрать!')
                room = ROOMS[game_state['current_room']]
                room['items'].append('coin')
            
            # Услишал шорох
            case 1:
                print('\nВ темноте послышался шорох, жутко ...')
                if 'sword' in game_state['player_inventory']:
                    print('\nВы отпугнули странное существо мечом')

            # Срабатывание ловушки
            case 2:
                if game_state['current_room'] == 'trap_room' and 'torch' not in game_state['player_inventory']:
                    trigger_trap(game_state)

  
   
# Функция помощи
def show_help(COMMANDS):
    print('\n== КОМАНДЫ ИСПОЛЬЗУЕМЫЕ В ИГРЕ ==\n')
    print("=" * 66)
    for key, value in COMMANDS.items():
        print(f'{key:<16} - {value}')
    print("=" * 66)
      

