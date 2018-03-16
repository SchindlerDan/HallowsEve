class werewolf(creature):
	def _init_():
		attack = 0;
		health = 200;

	attack():
		return random(41);
	takeDamage(weapon, playerDamage):
		if(weapon.name != "chocolateBar" && weapon.name != "sourStraws"):
			health = health - playerDamage;
		
