class ghouls(creature):
	attack = 15;
	health = random(41) + 40
	

	attack():
		return random(16) + attack;
	takeDamage(weapon):
		if(weapon.name == "NerdBombs"):
			health = health - (weapon.damage * 5)
		else:
			health = health - weapon.damage

		









