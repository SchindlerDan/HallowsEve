from creature import creature
class werewolf(creature):
	def _init_():
		attack = 0;
		health = 200;

	def attack():
		return random.randrange(0,40);
	def takeDamage(weapon, playerDamage):
		if(weapon.name != "chocolateBar" and weapon.name != "sourStraws"):
			health = health - playerDamage;
		if(health <= 0):
			update();
	def getName():
		return "werewolf "
