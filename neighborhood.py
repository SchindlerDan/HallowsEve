from Observer import Observer
#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python	
class neighborhood(Observer):
	houses = [[]]
	
	def _init_(rows, columns):
		houses = [[house() for x in range(columns)] for y in range(rows)];
	
	
	
	
