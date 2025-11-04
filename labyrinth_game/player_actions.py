# labyrinth_game/player_actions.py

# Импортируем переменную ROOMS из constants
# Импортируем модуль utils
from labyrinth_game import utils
from labyrinth_game.constants import ROOMS


# 1. Функция отображения инвентаря
def show_inventory(game_state):
    # Выводим перечень инвентаря если он есть
    if game_state['player_inventory']:
         print(f"\nВ наличии следующий инвентарь: {', '.join(game_state['player_inventory'])}")
    # в случае отсутсвия инвентаря сообщаем о его отсутствии
    else:
         print("\nВ наличии инвентаря нет")

 # 2. Функция обработки ввода пользователя      
def get_input(prompt="> "):
    try:
        # Убираем пробелы и меняем регистр на нижний
        command = input(prompt).strip().lower()

        if ' ' in command:
            # Если в команде несколько строк, превращаем в список
            return command.split()
        else:
            # Если одно слово возвращаем команду
            return command
        
    
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
        
# 3. Функция перемещения по комнатам
def move_player(game_state, direction):

    # Объявляем переменную room с помощью цепочки обращений
    room = ROOMS[game_state['current_room']]
    
    # Проверяем условие если выход из комнаты в заданном напралении
    if direction in room['exits']:

        # Если переход осуществляется в treasure_room
        if room['exits'][direction] == 'treasure_room':
            if  'rusty_key' not in game_state['player_inventory']:
                print('\nДверь заперта. Нужен ключ, чтобы пройти дальше.')
                return
            
            else:
                print('\nВы используете найденный ключ, чтобы открыть путь в комнату сокровищ.')
                              
        # Меняем в game_state название комнаты, используем обращение к вложенному словарю
        game_state['current_room']= room['exits'][direction]

        # Увеличиваем на единицу количество шагов
        game_state['steps_taken'] += 1

        # Импортируем функцию описания комнаты
        from labyrinth_game.utils import describe_current_room
        # Выводим описание новой комнаты
        describe_current_room(game_state)
        utils.random_event(game_state)
        
        
    else:
        # Если в данном направлении пойти нельзя, сообщаем об этом 
        print('\nНельзя пойти в этом направлении')
        
# 4. Функция взятия предмета
def take_item(game_state, item_name):

    # Объявляем переменную room с помощью цепочки обращений
    room = ROOMS[game_state['current_room']]

    # Проверяем условие есть ли предмет в комнате
    if item_name in room['items']:
        game_state['player_inventory'].append(item_name)
        room['items'].remove(item_name)
        print(f'\nВы подняли: {item_name}')

    else:
        print('\nТакого предмета нет в комнате')


# 5. Функция использования предмета
def use_item(game_state, item_name):
    # Проверяем есть ли предмет в инвентаре игрока
    if item_name in game_state['player_inventory']:
        match item_name:
            # Выводим сообщение при использовании фонаря
            case 'torch':
                print('\nСтало значительно светлее')

            # Выводим сообщение при использовании меча
            case 'sword':
                print('\nС мечом чувствую себя увереннее')

            # Выводим сообщение при открытии бронзовой шкатулки, добавляем в инвентари ключ при его отсутствии
            case 'bronze_box':
                if ('rusty_key') not in game_state['player_inventory']:
                    game_state['player_inventory'].append('rusty_key')
                    print('\nВ инвентарь добавлен rusty_key')
                else:
                    print('\nПусто!')
                
            # С остальными предментами неизвестноб что делать
            case _:
                print('\nНе знаю, что делать с этим предметом')

    # Выводим сообщение если предмета нет в инвентаре
    else:
        print('\nУ вас нет такого предмета.')



