
from textfx import delay_print,slow_print,fast_print,fastest_print,mvmtverbs,nverbs,sverbs,everbs,wverbs,dirverbs,instruct,idleverbs,getverbs,giveverbs
from items import Item,Key,Consumable
from map import roomlist, itemlist
import time
import json
class Player(object):
  def __init__(self,name,level,inventory,x,y):
    self.name = name
    self.level = level
    self.inventory = inventory
    self.x = x
    self.y = y
    self.inventorylimit = 5
    self.slotsleft = self.inventorylimit -len(self.inventory)
    self.cmd = "No Command"
    self.xp = 0
    self.room = "Not Loaded"
    self.hp = 20


  def encumbered(self):
    if len(self.inventory)>=self.inventorylimit-1:
      return True
    else:
      return False
  def __getstate__(self):
    dictlist = []
    for item in self.inventory:
      dictlist.append(item.__dict__)
    return { 'name': self.name, 'level': self.level, 'inventory':dictlist,'x':self.x,'y':self.y}
  def save(self):
    # file = open("{}.json".format(self.name),"w")
    # file.write(self.__dict__)
    # file.close()
    

    with open('{}.txt'.format(self.name), 'w') as outfile:
        json.dump(self.__getstate__(), outfile)


  def update(self,looped):
    #print ("Location: x = {} , y = {}".format(self.x,self.y))
    self.find_location()
    if not looped:
      self.room.getinfo()
    self.prompt()
    if self.cmd[0] in instruct:
      self.get_help()
    if self.cmd[0] == "quit":
      return False
    self.is_interitem()
    if self.is_moving():
      self.move()
    if not self.find_location() or self.room.islocked:
      if self.room.islocked:
        if self.unlock():
          self.find_location()
        else:
          delay_print("This room is locked. Find the key to proceed.")
          self.undo_move()
          self.find_location()
      else:
        delay_print("Blocked")
        self.undo_move()
        self.find_location()
      
    else:
      self.find_location()
    self.room.getinfo()
    self.room = "not loaded"
    return True


  def prompt(self):
    cmd = input(">")
    self.cmd = cmd.lower().split(" ")
    return self.cmd


# movement
  def find_location(self):
    for room in roomlist:
      if self.x == room.x and self.y == room.y:
        self.room = room
        return True


    
  def is_moving(self):
    for verb in mvmtverbs:
      if self.cmd[0] == verb: 
        return True
  def move(self):
    #checking for the lists of directional verbs, adds to player x and y.
    for dirs in dirverbs:  
      if self.cmd[1] in dirs:
        if dirs[0].startswith("n"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          slow_print("Moving {}.....".format(dirs[0]))
          self.move_north()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("s"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          slow_print("Moving {}.....".format(dirs[0]))
          self.move_south()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("e"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          slow_print("Moving {}.....".format(dirs[0]))
          self.move_east()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("w"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          slow_print("Moving {}.....".format(dirs[0]))
          self.move_west()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        else:
          delay_print("Fail")
  def undo_move(self):
    #checking for the lists of directional verbs, adds to player x and y.
    for dirs in dirverbs:  
      if self.cmd[1] in dirs:
        if dirs[0].startswith("n"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          self.move_south()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("s"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          self.move_north()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("e"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          self.move_west()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        elif dirs[0].startswith("w"):
          # delay_print("Pre add : {},{}".format(self.x,self.y))
          self.move_east()
          # delay_print("Post add : {},{}".format(self.x,self.y))
        else:
          delay_print("Fail")
  def move_north(self):
    self.y+=1
  def move_south(self):
    self.y-=1
  def move_east(self):
    self.x+=1
  def move_west(self):
    self.x-=1
# item transactions
  def is_interitem(self):
    if self.cmd[0] in getverbs:
      for item in self.room.items:
        if self.cmd[len(self.cmd)-1] == item.name:
          self.add_item(item)
    elif self.cmd[0] in giveverbs:
      for item in self.inventory:
        if self.cmd[len(self.cmd)-1] == item.name:
          self.drop_item(item)
    elif self.cmd[0] in idleverbs:
      for item in self.inventory:
        if self.cmd[len(self.cmd)-1] == item.name:
          delay_print(item.give_info())
        elif self.cmd[len(self.cmd)-1] == "inventory":
          for item in self.inventory:
            delay_print(item.give_info())
  def add_item(self,item):
    if not self.encumbered():
      self.inventory.append(item)
      self.room.items.remove(item)
      self.slotsleft = self.inventorylimit -len(self.inventory)
      delay_print("You picked up {} {}. You have {} slots left in your inventory".format(item.pronoun,item.name,self.slotsleft))
    else:
      delay_print("You don't have enough room for that. Try dropping something in order to pick it up.")
  def drop_item(self,item):
    if item in self.inventory:
      self.inventory.remove(item)
      self.room.items.append(item)
      self.slotsleft = self.inventorylimit -len(self.inventory)
      delay_print("You dropped {} {}. You have {} slots left in your inventory.".format(item.pronoun,item.name,self.slotsleft))
# help
  def get_help(self):
    delay_print("HELP")
    time.sleep(2)
    delay_print("use compass directions to move, be specific")
    #delete_last_lines(1)
# key interactions
  def unlock(self):
    for item in self.inventory:
      if isinstance(item,Key):
        if item.unlocks == self.room:
          self.inventory.remove(item)
          self.room.islocked = False
          delay_print("*CHONK* The door unlocks.")
          return True
        else:
          delay_print("This key doesn't fit.")



def load_player(ofile):
  # for some reason i can't do the next two steps in one ???
  file = open(ofile,'r')
  data = json.load(file)
  items = []
  for itemdict in data['inventory']:
    for item in itemlist:
      if itemdict == item.__dict__:
        items.append(item)

  player = Player(data['name'],data['level'],items,data['x'],data['y'])
  return player
