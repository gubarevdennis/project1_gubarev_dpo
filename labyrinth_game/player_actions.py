# labyrinth_game/player_actions.py
def show_inventory(game_state):
    if game_state['player_inventory']:
        print("Ваш инвентарь:")
        for item in game_state['player_inventory']:
            print(f"  - {item}")
    else:
        print("Ваш инвентарь пуст.")

def get_input(prompt="> "):
    try:
        user_input = input(prompt)
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"