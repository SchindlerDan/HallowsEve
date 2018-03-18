from Observer import Observer
#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python	
class neighborhood(Observer):
	houses = [];
	hauntedHouses = 0;
	
	def _init_(self, game, rows, columns):
		hauntedHouses = rows * columns;
		#houses = [[house() for x in range(columns)] for y in range(rows)];
		#This nested for loop will fill the board with new houses in a grid.
		for x in range(0, columns):
			houses.append([]);
			for y in range(0, rows):
				newHome = house(x, y);
				newHome.addObserver(self);
				houses[x].append(newHome);
	
	def update(house):
		hauntedHouses = hauntedHouses - 1;
		if(hauntedHouses <= 0):
			updateGame(self, house.getX(), house.getY());
	def getHouse(x, y):
		return houses[x][y];
