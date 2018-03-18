#https://docs.python.org/2/tutorial/classes.html
from Observable import Observable
import random;
class creature(Observable,object):
	def _init_(self, house):
		attack=0;#compiler said to initialize these
		health=0;
		self.addObserver(house);
	def takeDamage(weapon):
		pass
	def attack():
		return attack;

	def getHealth():
		return health;

