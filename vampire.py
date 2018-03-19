from creature import creature
from Observable import Observable
import random
class vampire(creature, Observable):
	health = 0;
	attack = 0;
	name = "";
	def __init__(self, house):
		self.attack = 10;
		self.health = random.randrange(0,100) + 100;
		Observable.__init__(self);
		self.add_observer(house);
		self.name = "vampire"
	def attacking(self):
		return random.randrange(0,10) + self.attack;
	def takeDamage(self, weapon, playerDamage):
		if(weapon.name != "Chocolate Bar"):
			self.health = self.health - playerDamage;
		if(self.health <= 0):
			self.updateHouse(self);
