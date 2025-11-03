# labyrinth_game/player_actions.py

# Импортируем переменную ROOMS из constants
from labyrinth_game.constants import ROOMS 

# 1. Функция отображения инвентаря
def show_inventory(game_state):
    # Выводим перечень инвентаря если он есть
    if game_state['player_inventory']:
         print(f"\nВ наличии следующий инвентарь: {' '.join(game_state['player_inventory'])}")
    # в случае отсутсвия инвентаря сообщаем о его отсутствии
    else:
         print(f"\nВ наличии инвентаря нет")

 # 2. Функция обработки ввода пользователя      
def get_input(prompt="> "):
    try:
        # Убираем пробелы и меняем регистр на нижний
        command = input(prompt).strip().lower()
        # Если в команде больше одного слова, формируем список
        if ' ' in command:
            
            return command.split()
        # Если в команде одно слово возвращаем строку
        else:

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
       
        # Меняем в game_state название комнаты, используем обращение к вложенному словарю
        game_state['current_room']= room['exits'][direction]

        # Увеличиваем на единицу количество шагов
        game_state['steps_taken'] += 1

        # Импортируем функцию описания комнаты
        from labyrinth_game.utils import describe_current_room
        # Выводим описание новой комнаты
        describe_current_room(game_state)

    
    else:
        # Если в данном направлении пойти нельзя, сообщаем об этом
        print(f'\nНельзя пойти в этом направлении')
        

