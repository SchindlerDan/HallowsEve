from creature import creature
class human(creature):
	attack = 0;
	health = 100;
	def _init_():
		attack = -1;
		health = 100;



	def takeDamage(self, weapon, playerDamage):
		pass

	def attacking(self):
		return -1;

	def getName(self):
		return "Saved Human" 
