from weapon import weapon
import random
class chocolateBars(weapon):
	name = "Chocolate Bar";
	#https://docs.python.org/2/library/random.html
	damage = ((random.randrange(0,40) + 200)/ 100)
	uses = 4
