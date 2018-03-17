from creature import creature
from Observer import Observer
from Observable import Observable
import random
class house(Observable,Observer):
	population = random.randrange(0,10);
	monsterMash = []
	#http://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/
	def _init_():
		for i in range (0,population):
			pickMonster = random(4)
			if(pickMonster == 0):
				monster = ghoul();
				monsterMash.add(monster);
			elif(pickMonster == 1):
				monster = vampire();
				monsterMash.add(monster);
			elif(pickMonster == 2):
				monster = zombie();
				monsterMash.add(monster);
			else:
				monster = werewolf();
				monsterMash.add(monster);






