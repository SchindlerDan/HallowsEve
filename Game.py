class game(Observer):
	clearedHouses = [];
	gameOn = True;
	def updateGame(neighborhood, x, y):
		clearedHouses.append([x,y]);
		
	def update(player):	
		gameOn = False;
		print "Sorry, your journey is at an end. You have died";
	def main():
		
		#http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
		rows = 0;
		columns = 0;
		playerCoordinateX = 0;
		playerCoordinateY = 0;
		
		movement = ""
		weaponPick = 0;

		rows = input("Please state how tall your neighborhood is: \n");
		columns = input("Please state how wide your neighborhood is: \n");

		neighborhood = neighborhood(self, rows, columns);
		player = player(self);
		playerCoordinateX = input("How many houses to the right is your home?\n");
		while(playerCoordinateX > columns):
			playerCoordinateX = input("Oops, that was too far! Try again please. \n");
		playerCoordinateY = input("How many houses down is your home?\n");
		while(playerCoordinateY > rows):
			playerCoordinateY = input("Oops, that was too far! Try again please.\n");



		print "After waking from a sugar crash, you discover that your friends and family have all turned into horrible monsters! Can you survive and return everyone to normal?\n";
		print "Houses with monsters remaining will be marked by M, Houses that have been cleared will be marked by X, and the home you are in will be marked with P\n"


		while(gameOn):
			for x in rows:
				for y in columns:
					if([x,y] in clearedHouses):
						print "X "
					elif(x == playerCoordinateX and y == playerCoordinateY):
						print "P "
					else:
						print "M "
				print "\n";
			
			print "Health of monsters in this House: \n";
			neighborhood.getHouse[playerCoordinateX, playerCoordinateY].getStatus();

			print "\n your status: "
			print player.getHealth();
			print "\n"
			movement = input( "Would you like to stay in this house, or move to a different home? W to go north, A to go west, S to go south, D to go east, or any other input to stay here.\n");
			
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
		
			
			print "Which weapon shall you use? Use the weapon's number in your inventory that you'd like to use\n"
			player.printInventory();
			while(weaponPick == 0):
			weaponPick = input("I'll choose weapon number...\n");
			
			if(weaponPick > player.getNumberOfWeapons()):
				weaponPick = 0;
				print "oops, that weapon doesn't exist! Try again.";

			neighborhood.getHouse(playerCoordinateX, playerCoordinateY).attackMonsters(player.getWeapon(weaponPick), player.getAttack());
			
			player.takeDamage(neighborhood.getHouse(playerCoordinateX, playerCoordinateY).monstersAttack();	
			
			
			if(clearedHouses.size() == rows * columns):
				print "With one final sugar rush, you manage to defeat your final foe. VICTORY!"
				gameOn = False;






