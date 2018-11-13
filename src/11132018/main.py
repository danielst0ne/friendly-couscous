import sys
import time
from textfx import delete_last_lines,delay_print,slow_print,fast_print,fastest_print
from player import Player, load_player
from sequences import user_creation,game
from room import Room
from map import roomlist,cblbrg,castlegate,apple

#rooms
player = load_player("daniel.txt")
player.save()
loop = True
game(loop,player)



