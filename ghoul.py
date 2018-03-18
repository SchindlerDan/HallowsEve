from creature import creature
from Observable import Observable
import random
class ghoul(creature, Observable):
	name = ""
	health = 0;
	attack = 0
	def __init__(self, house):
		self.attack = 15;
		self.health = random.randrange(0,40) + 40
		Observable.__init__(self);
		self.add_observer(house);
		self.name = "ghoul"
	def attacking(self):
		return random.randrange(0,15) + self.attack;
	def takeDamage(self, weapon, playerDamage):
		if(weapon.name == "NerdBombs"):
			self.health = self.health - (playerDamage * 5)
		else:
			self.health = self.health - playerDamage
		if(self.health <= 0):
			self.update();







