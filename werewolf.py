from creature import creature
from Observable import Observable
import random
class werewolf(creature, Observable):
	health = 0;
	attack = 0;
	name = "";
	def __init__(self, house):
		self.attack = 0;
		self.health = 200;
		Observable.__init__(self);
		self.add_observer(house);
		self.name = "werewolf"
	def attacking(self):
		return random.randrange(0,40);
	def takedamage(self, weapon, playerdamage):
		if(weapon.name != "Chocolate Bar" and weapon.name != "Sour Straws"):
			self.health = self.health - playerdamage;
		if(self.health <= 0):
			self.updatehouse(self);
