from Observer import Observer
from Observable import Observable
from house import house
#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python	
class neighborhood(Observer, Observable):
	houses = [];
	hauntedHouses = 0;
	r = 1;
	c = 1;
	def __init__(self, game, rows, columns):
		hauntedHouses = rows * columns;
		#houses = [[house() for x in range(columns)] for y in range(rows)];
		#This nested for loop will fill the board with new houses in a grid.
		Observable.__init__(self);
		r = rows
		c = columns
		self.add_observer(game);
		for x in range(0, c):
			self.houses.append([]);
			for y in range(0, r):
				newHome = house(self, x, y);
				newHome.add_observer(self);
				self.houses[x].append(newHome);
	
	def update(house):
		hauntedHouses = hauntedHouses - 1;
		if(hauntedHouses <= 0):
			updateGame(self, house.getX(), house.getY());
	def getHouse(self, x, y):
		return self.houses[x][y];
