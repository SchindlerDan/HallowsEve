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
	def takeDamage(self, weapon, playerDamage):
		if(weapon.name != "chocolateBar" and weapon.name != "sourStraws"):
			self.health = self.health - playerDamage;
		if(self.health <= 0):
			update();
