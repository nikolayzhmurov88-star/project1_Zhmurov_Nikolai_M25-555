#!/usr/bin/env python3

# Выполняем необходимые импорты
from labyrinth_game import constants as const
from labyrinth_game import utils
from labyrinth_game import player_actions as pa

# 1. Задаем основную функцию
def main():
    #print('Первая попытка запустить проект!')
    print("\nДобро пожаловать в Лабиринт сокровищ!")

    # Объявляем переменную game_state, описывающую состояние игры
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }
    
    # Вызываем функцию описания комнаты
    utils.describe_current_room(game_state)

    # Объявляем цикл с условием окончание игры равно False
    while not game_state['game_over']:
        # Вызываем функцию обработки команд пользователя
        command = pa.get_input(f'\nВведите команду: ')
        process_command(game_state, command)
      
    
# 2. Задаем функцию обработки команд
def process_command(game_state, command):

    # Обрабатывем команду игрока с помощью match / case
    match command:

        # Вызываем функцию отображения инвентаря
        case 'inventory':
            pa.show_inventory(game_state)

        # Вызываем функцию перемещения по комнатам
        case ['go', direction]:
            # Проверяем, что направление введено корректно
            if direction in ['north', 'south', 'east', 'west']:
                pa.move_player(game_state, direction)
            else:
                print(f'\nУточните направление')

        # Вызываем функцию осмотра комнаты
        case 'look':
            utils.describe_current_room(game_state)

        # Вызываем функцию взятия предмета
        case ['take', item]:
            
            # Добавляем отдельное условие для попытки поднятия сундука
            if item == 'treasure_chest':
                print('\nВы не можете поднять сундук, он слишком тяжелый.')
                
            # Если поднимаем не сундук, то выполняюм стандартную функцию взятия предмета
            else:
                pa.take_item(game_state, item)

        # Вызываем функцию использования предмета
        case ['use', item]:
            pa.use_item(game_state, item)
            
        # Вызвываем функцию попмощи (список команд)
        case 'help':
            utils.show_help()
        
        # Вызываем функцию решения загадок
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                utils.attempt_open_treasure(game_state)
            else:
                utils.solve_puzzle(game_state)
        
		# Если возвращается команда quit или exit завершаем игру
        case 'quit' | 'exit':
            print(f'\nИгра закончена! Спасибо!')
            game_state['game_over'] = True

        # Если команда не распознана выводим сообщение
        case _:
            print(f'\nНеизвестная команда')



# Вызываем ее только при запуске модуля как программы
if __name__ == "__main__":
    main()