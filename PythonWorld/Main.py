from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Turtle import Turtle
from Organisms.Ufo import Ufo

import os


if __name__ == '__main__':
	pyWorld = World(8, 8)

	newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=0, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Dandelion(position=Position(xPosition=0, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Wolf(position=Position(xPosition=7, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Toadstool(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Turtle(position=Position(xPosition=6, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Ufo(position=Position(xPosition=5, yPosition=5), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Antelope(position=Position(xPosition=3, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 100):
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
		answer = input("Do you want to add another organism?")
		if answer == "yes":
			print("1. Antelope 2. Dandelion 3. Grass 4. Sheep 5. Toadstool 6.Turtle 7. Ufo 8. Wolf")
			organism = int(input("Which organism?"))
			if isinstance(organism, int) and organism >=1  and organism <= 8:
				print("List of free positions")
				print(pyWorld.showAllFreePositions())
				print("Where?")
				positionX = int(input("x = "))
				positionY = int(input("y = "))
				if (positionX, positionY) in pyWorld.showAllFreePositions():
					pyWorld.userAddOrganism(organism, Position(xPosition=positionX, yPosition=positionY))
				else:
					print("Bad data")
