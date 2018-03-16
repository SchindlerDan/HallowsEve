class zombie(creature):
	def _init_():
		attack = 10;
		health = random(51) + 50

	attack():
		return random(attack);
	takeDamage(weapon, playerDamage):
		#thepythonguru.com/python-strings/
		if(weapon.name == "SourStraws"):
			health = health - (2 * playerDamage);
		else:
			health = health - playerDamage;
