from creature import creature
from Observer import Observer
from Observable import Observable
from ghoul import ghoul
from vampire import vampire
from werewolf import werewolf
from zombie import zombie
from human import human
import random
#https://docs.python.org/2/library/random.html
class house(Observable,Observer):
	population = random.randrange(0, 10, 1);
	humansSaved = 0;
	
	
	#https://developers.google.com/edu/python/lists
	
	myX = 0;
	myY = 0;
	#http://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/
	#http://www.pythonforbeginners.com/super/working-python-super-function
	def __init__(self, neighborhood, x, y):
		Observable.__init__(self);
		self.population = random.randrange(0, 10, 1);
		self.monsterMash = [];
		self.humansSaved = 0;	
		
		
		
		
		self.add_observer(neighborhood);
		for i in range (0, self.population):
			pickMonster = random.randint(0,3)
			monsterMash = self.monsterMash
			if(pickMonster == 0):
				monster = ghoul(self);
				monsterMash.append(monster);
			elif(pickMonster == 1):
				monster = vampire(self);
				monsterMash.append(monster);
			elif(pickMonster == 2):
				monster = zombie(self);
				monsterMash.append(monster);
			else:
				monster = werewolf(self);
				monsterMash.append(monster);
		self.myX = x;
		self.myY = y;




	def attackMonsters(self, weapon, damage):
		for x in self.monsterMash:
			x.takeDamage(weapon, damage);
			

#		if(self.humansSaved == self.population):
#			self.updateNeighborhood();
			
	def update(self, monster):
		self.humansSaved = self.humansSaved + 1;
		self.monsterMash[self.monsterMash.index(monster)] = human();
		if(self.humansSaved == self.population):
			self.updateNeighborhood(self);




	def monstersAttack(self):
		totalDamage = 0;
		for x in self.monsterMash:
			totalDamage = totalDamage + x.attacking();
			
		return totalDamage;
	def getX(self):
		return self.myX;
	def getY(self):
		return self.myY;
	def reportStatus(self):
		print "There are ",
		print len(self.monsterMash),
		print " Monsters in this house"
		#https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
		for x in self.monsterMash:
			print x.getName(),
			print ": ",
			print  x.getHealth()	
	
