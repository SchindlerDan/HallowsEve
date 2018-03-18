#https://docs.python.org/2/tutorial/classes.html
from Observable import Observable
import random;
class creature(Observable,object):
	def _init_(self, house):
		name = "Default"
		attack=0;#compiler said to initialize these
		health=0;
		Observable.__init__(self);
		self.add_observer(house);
	def takeDamage(self, weapon):
		pass
	def attack(self):
		return self.attack;

	def getHealth(self):
		return self.health;
	def getName(self):
		return self.name;
