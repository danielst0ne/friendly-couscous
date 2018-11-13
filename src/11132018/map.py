import sys
import time
from textfx import delete_last_lines,delay_print,slow_print,fast_print,fastest_print
from room import Room
from items import Item, Weapon, Consumable,Key

bog = Room("STRANGE BOG","Bazinga, you fell for my inviting title. Sample Text Here",1,0,[],[],False)
foyer = Room("CASTLE FOYER","You are in the foyer of the castle.\nYou are in awe of the size of it.",0,2,[],[],True)
key = Key("key","a","A large,rusty iron key.",foyer)
castlegate = Room("CASTLE GATE","You're in front of a wrought iron gate.",0,1,[key],[],True)
key2 = Key("key","a","A small bronze key",castlegate)
apple = Consumable("apple","an",1,"a pink lady apple.")

cblbrg = Room("COBBLESTONE BRIDGE","In front of you,to the north, is a gate to an enormous castle.\nTo the east is a strange looking bog",0,0,[apple,key],[],False)
itemlist = [key,key2,apple]
roomlist = [cblbrg,castlegate,bog,foyer]

 