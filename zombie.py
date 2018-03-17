from creature import creature
class zombie(creature):
	def _init_():
		attack = 10;
		health = random.randrange(0,50) + 50

	def attack():
		return random.randrange(0,attack);
	def takeDamage(weapon, playerDamage):
		#thepythonguru.com/python-strings/
		if(weapon.name == "SourStraws"):
			health = health - (2 * playerDamage);
		else:
			health = health - playerDamage;
