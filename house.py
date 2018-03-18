from creature import creature
from Observer import Observer
from Observable import Observable
import random
class house(Observable,Observer):
	population = random(11);
	humansSaved = 0;
	#https://developers.google.com/edu/python/lists
	monsterMash = []
	myX = 0;
	myY = 0;
	#http://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/
	def _init_(self, neighborhood, x, y):
		self.addObserver(neighborhood);
		for i in range (0,population):
			pickMonster = random(4)
			if(pickMonster == 0):
				monster = ghoul(self);
				monsterMash.add(monster);
			elif(pickMonster == 1):
				monster = vampire(self);
				monsterMash.add(monster);
			elif(pickMonster == 2):
				monster = zombie(self);
				monsterMash.add(monster);
			else:
				monster = werewolf(self);
				monsterMash.add(monster);
		myX = x;
		myY = y;




	def attackMonsters(weapon, damage):
		for x in monsterMash:
			x.takeDamage(weapon, damage);
			print "monsters need to update to let house know when they die";

		if(humansSaved == population):
			updateNeighborhood();
			print "FIXME! House needs to notify neighborhood";
	def update(monster):
		humansSaved = humansSaved + 1;
		monsterMash[monsterMash.index(monster)] = human();
	def monstersAttack():
		totalDamage = 0;
		for x in monsterMash:
			totalDamage = totalDamage + x.attack();
		return totalDamage;
	def getX():
		return myX;
	def getY():
		return myY;
	def reportStatus():
		for x in monsterMash:
			print x.getName
			print ": "
			print  x.getHealth	
			print "\n"
