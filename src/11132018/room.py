import sys
import time
from textfx import delete_last_lines,delay_print,slow_print,fast_print,fastest_print


class Room(object):
  def __init__(self,name,desc,x,y,items,life,islocked):
    self.name = name
    self.desc = desc
    self.x = x
    self.y = y
    self.items = items
    self.life = life
    self.islocked = islocked


  def touching(self,room):
    if room in self.borders:
      return true
    else: return false

  def getinfo(self):
    items = ""
    for item in self.items:
      items+=item.name+","
    delay_print("{}\n{}\nITEMS: {}".format(self.name,self.desc,items))
