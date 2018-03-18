from weapon import weapon
import random
class nerdBombs(weapon):
	name = "NerdBomb";
	damage = ((random.randrange(0,250) + 300) / 100);
	uses = 1;
