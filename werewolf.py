class werewolf(creature):
	attack = 0;
	health = 200;

	attack():
		return random(41);
	takeDamage(weapon):
		if(weapon.name != "chocolateBar" && weapon.name != "sourStraws"):
			health = health - weapon.damage;
		
