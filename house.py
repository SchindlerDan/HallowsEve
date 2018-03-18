class house(Observable,Observer):
	population = random(11);
	humansSaved = 0;
	monsterMash = []
	#http://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/
	def _init_():
		for(i = 0; i < random; i++):
			pickMonster = random(4)
			if(pickMonster == 0):
				monster = ghoul();
				monsterMash.add(monster);
			else if(pickMonster == 1):
				monster = vampire();
				monsterMash.add(monster);
			else if(pickMonster == 2):
				monster = zombie();
				monsterMash.add(monster);
			else:
				monster = werewolf();
				monsterMash.add(monster);





	def attackMonsters(weapon, damage):
		for(x in monsterMash):
			x.attack(weapon, damage);
			print "monsters need to update to let house know when they die";

		if(humansSaved == population):
			print "FIXME! House needs to notify neighborhood";
