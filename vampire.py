class vampire():
	attack = 10;
	health = random(101) + 100;
	
	attack():
		return random(11) + attack;
	takeDamage(weapon):
		if(weapon.name != "ChocolateBar"):
			health = health - weapon.damage;

