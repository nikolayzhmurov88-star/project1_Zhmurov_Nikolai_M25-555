# labyrinth_game/player_actions.py

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
        

