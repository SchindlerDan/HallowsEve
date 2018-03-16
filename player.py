class player(creature):
	inventory = [];
	def _init_():
		health = random(26) + 100;
		attack = (11) + 10;
		startingWeapon = hersheyKisses();
		inventory.add(startingWeapon);
		
		for(i = 1; i < 10; i++):
			startingGear = random(3);
			
			if(startingGear == 0):
				candy = chocolateBars();
				inventory.add(candy);
			else if(startingGear == 1):
				candy = nerdBombs();

				inventory.add(candy);
			else:
				candy = sourStraw();
				inventory.add(candy);
		
	attack(weapon):
		return attack * weapon.damage;
	
	takeDamage(weapon, damage):
		health = health - damage;
