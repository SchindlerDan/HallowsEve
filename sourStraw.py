from weapon import weapon
import random
class sourStraw(weapon):
	name = "Sour Straw";
	damage = (random.randrange(0,75) + 100)/ 100;
	uses = 2;
