


class Item(object):
	def __init__(self,name,pronoun,value,desc):
		self.name = name
		self.pronoun = pronoun
		self.value = value
		self.desc = desc
	def give_info(self):
		return ("{}\n{}".format(self.name,self.desc))


class Weapon(Item):
	def __init__(self,name,pronoun,value,desc,damage):
		super().__init__(name,pronoun,value,desc)
		self.damage = damage

class Consumable(Item):
	def __init__(self,name,pronoun,value,desc):
		super().__init__(name,pronoun,value,desc)

class Key(Item):
	def __init__(self,name,pronoun,desc,unlocks):
		self.name = name
		self.pronoun = pronoun
		self.desc = desc
		self.unlocks = unlocks
		
