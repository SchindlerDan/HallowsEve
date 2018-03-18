from creature import creature
class player(observable, creature):
	inventory = [];
	health = 0;
	attack = 0;
	
	def _init_(game):
		health = random.randrange(0,25) + 100;
		attack = random.randrange(0,10) + 10;
		startingWeapon = hersheyKisses();
		inventory.add(startingWeapon);
		self.addObserver(game);
		for i in range (0,9):
			startingGear = random(3);
			
			if(startingGear == 0):
				candy = chocolateBars();
				inventory.add(candy);
			elif(startingGear == 1):
				candy = nerdBombs();

				inventory.add(candy);
			else:
				candy = sourStraw();
				inventory.add(candy);
		
	def attack(number):
		return attack * inventory[number].damage;
	
	def takeDamage(damage):
		health = health - damage;
		#intentional. 0 health means you are on death's doorstep
		if(health < 0):
			update(self);	

	def printInventory():
		for x in inventory:
			print x.name;
			print "\n"
	def getNumberOfWeapons():
		return inventory.size();
	def getWeapon(number):
		return inventory[number];
	def getHealth():
		return health
