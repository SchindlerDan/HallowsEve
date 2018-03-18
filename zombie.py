from creature import creature
from Observable import Observable	
import random
class zombie(creature):
	name = ""
	health = 0;
	attack = 0;

	def __init__(self, house):
		self.attack = 10;
		self.health = random.randrange(0,50) + 50
		Observable.__init__(self);
		self.add_observer(house);
		self.name = "zombie"
	def attacking(self):
		return random.randrange(0, self.attack);
	def takeDamage(self, weapon, playerDamage):
		#thepythonguru.com/python-strings/
		if(weapon.name == "SourStraws"):
			self.health = self.health - (2 * playerDamage);
		else:
			self.health = self.health - playerDamage;

		if(self.health <= 0):
			self.updateHouse(self);
	
