class Observable(object):
	#copied directly from the slides
        def __init__(self):    
                self.observers = []
 
        def add_observer(self, observer):
                if not observer in self.observers:
                        self.observers.append(observer)
 
        def remove_observe(self, observer):
                if observer in self.observers:
                        self.observers.remove(observer)
 
        def remove_all_observers(self):
                self.observers = []
				
	def update(self, player):
		for observer in self.observers:
			observer.update(player)
	def updateNeighborhood(self, house):
		for observer in self.observers:
			observer.update(house);				
	def updateGame(self, x, y):
		for observer in self.observers:
			observer.updateSaved(x, y);		
	def updateHouse(self, creature):
		for observer in self.observers:
			observer.update(creature);

	def updateVictory(self):
		for observer in self.observers:
			observer.updateWin();
