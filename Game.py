#https://stackoverflow.com/questions/2042426/compile-python-py-file-without-executing
#https://askubuntu.com/questions/244378/running-python-file-in-terminal
#!/usr/bin/python
#https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules
from Observer import Observer
from creature import creature
from house import house
from player import player
from ghoul import ghoul
from vampire import vampire
from weapon import weapon
from werewolf import werewolf
from neighborhood import neighborhood
from nerdBombs import nerdBombs
from HersheyKisses import HersheyKisses
from sourStraw import sourStraw
from chocolateBars import chocolateBars



print "running Game";
class game(Observer):
	clearedHouses = [];
	gameOn = True;
	

	def updateVictory():
		self.gameOn = False;
		print "Congratulations on saving your neighborhood!"


	def updateSaved(self, house):
		#coordinateSaved = []
		#coordinateSaved.append(x);
		#coordinateSaved.append(y);
		self.clearedHouses.append(house);
		#print "we've saved a house at the following coordinates: ",
		#print coordinateSaved;	
	def update(self, player):	
		self.gameOn = False;
		print "Sorry, your journey is at an end. You have died";
	def main(self):
		#http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
		rows = 0;
		columns = 0;
		playerCoordinateX = 0;
		playerCoordinateY = 0;
		
		movement = ""
		weaponPick = -1;

		rows = input("Please state how tall your neighborhood is: ");
		columns = input("Please state how wide your neighborhood is: ");
		
		myNeighborhood = neighborhood(self, rows, columns);
		


		myPlayer = player(self);
		playerCoordinateX = input("How many houses to the right is your home? ");
		while(playerCoordinateX > columns or playerCoordinateX < 0):
			playerCoordinateX = input("Oops, that was too far! Try again please. ");
		playerCoordinateY = input("How many houses down is your home? ");
		while(playerCoordinateY > rows or playerCoordinateY < 0):
			playerCoordinateY = input("Oops, that was too far! Try again please. ");



		print "After waking from a sugar crash, you discover that your friends and family have all turned into horrible monsters! Can you survive and return everyone to normal?";
		print "Houses with monsters remaining will be marked by M, Houses that have been cleared will be marked by X, and the home you are in will be marked with P"
		
		#this loop actually runs the game
		while(self.gameOn):
			#this nested loop prints the board
			for y in range(0, rows):
				for x in range(0, columns):
					cleared = False;
					#playerCoordinates are weird, x is x here but x is y just a few lines down, DO NOT TOUCH PLEASE
					for z in self.clearedHouses:
						if(z.getX() == x and z.getY() == y and not (playerCoordinateX == x and playerCoordinateY == y)):
							print "X ",
							cleared = True;
					#Don't touch this please
					if(x == playerCoordinateX and y == playerCoordinateY):
						print "P ",
						
					elif(not cleared):
						print "M ",
				print "\n";
			
			print "Health of monsters in this House:";
			myNeighborhood.getHouse(playerCoordinateX, playerCoordinateY).reportStatus();

			print "\n your health: ",
			print myPlayer.getHealth();
			movement = raw_input( "Would you like to stay in this house, or move to a different home? W to go north, A to go west, S to go south, D to go east, or any other input to stay here and fight.");
			
			if(movement == "W" or movement == "w"):
				if(playerCoordinateY == 0):
					print "Don't abandon your neighborhood! Staying in this house\n"
				else:
					print "You bravely venture north\n"
					playerCoordinateY = playerCoordinateY - 1;
			elif(movement == "s" or movement == "S"):
				if(playerCoordinateY == rows - 1):
					print "Don't leave your neighbors to this cruel fate! Staying in this house\n"
				else:
					print "You cautiously Travel south\n"
					playerCoordinateY = playerCoordinateY + 1;
			elif(movement == "a" or movement == "A"):
				if(playerCoordinateX == 0):
					print "You'd really leave these people to an afterlife of being monsters? Your conscience forces you to remain in the same house for this turn\n"
				else:
					print "Avoiding any trouble in the streets, you stealthily move to the west\n"
					playerCoordinateX = playerCoordinateX - 1;
					
			elif(movement == "d" or movement == "D"):
				if(playerCoordinateX == columns - 1):
					print "While a Katana might help you in this situation, you can't go far enough east. Best just stay in this house\n"

				else:
					print "Traveling through the darkness of night, you travel east\n"
					playerCoordinateX = playerCoordinateX + 1;
				
			else:
				print "You decided to stay in this house\n"
		
				weaponPick = -1;
				print "Which weapon shall you use? Use the weapon's number in your inventory that you'd like to use"
				myPlayer.printInventory();
				while(weaponPick < 0):
					weaponPick = input("I'll choose weapon number...") - 1;
				
				if(weaponPick > myPlayer.getNumberOfWeapons()):
					weaponPick = -1;
					print "oops, that weapon doesn't exist! Try again.";
	
				myNeighborhood.getHouse(playerCoordinateX, playerCoordinateY).attackMonsters(myPlayer.getWeapon(weaponPick), myPlayer.getAttack(weaponPick));
				
				myPlayer.takeDamage(myNeighborhood.getHouse(playerCoordinateX, playerCoordinateY).monstersAttack())
			
			
			if(len(self.clearedHouses) == rows * columns):
				print "With one final sugar rush, you manage to defeat your final foe. VICTORY!"
				gameOn = False;





Game = game();
Game.main();
