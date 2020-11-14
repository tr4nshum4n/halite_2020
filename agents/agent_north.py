from kaggle_environments.envs.halite.helpers import *

def agent_north(board):
    for ship in board.current_player.ships:
        ship.next_action = ShipAction.NORTH
        
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

print(datetime.now().hour)


