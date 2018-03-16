class zombie(creature):
	attack = 10;
	health = random(51) + 50

	attack():
		return random(attack);
	takeDamage(weapon):
		#thepythonguru.com/python-strings/
		if(weapon.name == "SourStraws"):
			health = health - (2 * weapon.damage);
		else:
			health = health - weapon.damage;
