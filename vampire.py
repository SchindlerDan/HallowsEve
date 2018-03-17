from creature import creature
class vampire(creature):
	

	def _init():
		attack = 10;
		health = random.randrange(0,100) + 100;
	
	def attack():
		return random.randrange(0,10) + attack;
	def takeDamage(weapon, playerDamage):
		if(weapon.name != "ChocolateBar"):
			health = health - playerDamage;

