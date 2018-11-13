import sys
import time
from textfx import delete_last_lines,delay_print,slow_print,fast_print,fastest_print
from player import Player
	
def user_creation():
	delay_print("Welcome to Castle Darkspur, Traveller")
	time.sleep(2)

	delay_print("This Game was made for you. Enjoy it.")
	time.sleep(2)
	name = input("Username: ")
	delay_print("Welcome, {}.".format(name))
	return name

def game(loop,player):
	looped = False
	while loop:
		loop = player.update(looped)
		looped = True
		player.save()