from creature import creature
class ghouls(creature):
	def _init_():
		attack = 15;
		health = random.randrange(0,40) + 40
	

	def attack():
		return random.randrange(0,15) + attack;
	def takeDamage(weapon, playerDamage):
		if(weapon.name == "NerdBombs"):
			health = health - (playerDamage * 5)
		else:
			health = health - playerDamage

		









