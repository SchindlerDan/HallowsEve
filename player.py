from creature import creature
from weapon import weapon
from HersheyKisses import HersheyKisses
from sourStraw import sourStraw
from chocolateBars import chocolateBars
from nerdBombs import nerdBombs
from Observable import Observable
import random
class player(creature):
	inventory = [];
	health = 0;
	attack = 0;
	
	def __init__(self, game):
		Observable.__init__(self);
		self.add_observer(game);
		self.health = random.randrange(0,25) + 100;
		self.attack = random.randrange(0,10) + 10;
		startingWeapon = HersheyKisses();
		self.inventory.append(startingWeapon);
		
		for i in range (0,9):
			startingGear = random.randint(0, 2);
			
			if(startingGear == 0):
				candy = chocolateBars();
				self.inventory.append(candy);
			elif(startingGear == 1):
				candy = nerdBombs();

				self.inventory.append(candy);
			else:
				candy = sourStraw();
				self.inventory.append(candy);
		
	def getAttack(self, number):
		modifier=self.inventory[number].damage;
		weapon.use(self.inventory[number]);
		#https://stackoverflow.com/questions/9754729/remove-object-from-a-list-of-objects-in-python
		if (self.inventory[number].uses==0):
			del self.inventory[number];
		return self.attack * modifier;
	
	def takeDamage(self, damage):
		self.health = self.health - damage;
		#intentional. 0 health means you are on death's doorstep
		if(self.health < 0):
			self.update(self);	

	def printInventory(self):
		count = 1;
		for x in self.inventory:
			print count,
			print x.name;
			count = count + 1;
	def getNumberOfWeapons(self):
		return len(self.inventory);
	def getWeapon(self, number):
		return self.inventory[number];
	def getHealth(self):
		return self.health
