class vampire(creature):
	

	def _init():
		attack = 10;
		health = random(101) + 100;
	
	attack():
		return random(11) + attack;
	takeDamage(weapon, playerDamage):
		if(weapon.name != "ChocolateBar"):
			health = health - playerDamage;

