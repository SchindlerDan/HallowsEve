from creature import creature
class player(creature):
	inventory = [];
	def _init_():
		health = random.randrange(0,25) + 100;
		attack = random.randrange(0,10) + 10;
		startingWeapon = hersheyKisses();
		inventory.add(startingWeapon);
		
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
		
	def attack(weapon):
		return attack * weapon.damage;
	
	def takeDamage(weapon, damage):
		health = health - damage;
