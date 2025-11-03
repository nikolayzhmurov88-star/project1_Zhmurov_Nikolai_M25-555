#!/usr/bin/env python3

# Выполняем необходимые импорты
from labyrinth_game import constants as const
from labyrinth_game import utils
from labyrinth_game import player_actions as pa

# Задаем функцию
def main():
    #print('Первая попытка запустить проект!')

    # Объявляем переменную game_state, описывающую состояние игры
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }

    utils.describe_current_room(game_state)

# Вызываем ее только при запуске модуля как программы
if __name__ == "__main__":
    main()