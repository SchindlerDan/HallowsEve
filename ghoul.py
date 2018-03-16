class ghouls(creature):
	def _init_():
		attack = 15;
		health = random(41) + 40
	

	attack():
		return random(16) + attack;
	takeDamage(weapon, playerDamage):
		if(weapon.name == "NerdBombs"):
			health = health - (playerDamage * 5)
		else:
			health = health - playerDamage

		









