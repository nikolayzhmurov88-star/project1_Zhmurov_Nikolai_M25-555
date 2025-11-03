# labyrinth_game/player_actions.py

# 1. Функция отображения инвентаря
def show_inventory(game_state):
    # Выводим перечень инвентаря если он есть
    if game_state['player_inventory']:
         print(f"\nВ наличии следующий инвентарь: {' '.join(game_state['player_inventory'])}")
    # в случае отсутсвия инвентаря сообщаем о его отсутствии
    else:
         print(f"\nВ наличии инвентаря нет")
