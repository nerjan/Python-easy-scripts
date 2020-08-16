from Position import Position
from Organisms.Plant import Plant
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Turtle import Turtle
from Organisms.Ufo import Ufo

class World(object):

	def __init__(self, worldX, worldY):
		self.__worldX = worldX
		self.__worldY = worldY
		self.__turn = 0
		self.__organisms = []
		self.__newOrganisms = []
		self.__separator = ' '
		self.__eatenTurtles = []
		self.__newEatenTurtles = []
		self.__timeStopped = []

	@property
	def worldX(self):
		return self.__worldX

	@property
	def worldY(self):
		return self.__worldY

	@property
	def turn(self):
		return self.__turn

	@turn.setter
	def turn(self, value):
		self.__turn = value

	@property
	def organisms(self):
		return self.__organisms

	@organisms.setter
	def organisms(self, value):
		self.__organisms = value

	@property
	def newOrganisms(self):
		return self.__newOrganisms

	@newOrganisms.setter
	def newOrganisms(self, value):
		self.__newOrganisms = value

	@property
	def separator(self):
		return self.__separator

	@property
	def eatenTurtles(self):
		return self.__eatenTurtles

	@eatenTurtles.setter
	def eatenTurtles(self, value):
		self.__eatenTurtles = value

	@property
	def newEatenTurtles(self):
		return self.__newEatenTurtles

	@newEatenTurtles.setter
	def newEatenTurtles(self,value):
		self.__newEatenTurtles = value

	@property
	def timeStopped(self):
		return self.__timeStopped

	@timeStopped.setter
	def timeStopped(self, value):
		self.__timeStopped = value

	def makeTurn(self):
		actions = []
		#unfreez time for all organisms
		self.timeStopped = []
		for org in self.organisms:
			if self.positionOnBoard(org.position) and org not in self.timeStopped:
				actions = org.move()
				for a in actions:
					self.makeMove(a)
				actions = []
				if self.positionOnBoard(org.position):
					actions = org.action()
					for a in actions:
						self.makeMove(a)
					actions = []

		#turtles are spitted out
		for turtle in self.eatenTurtles:
			if turtle.animalWhichEatMe not in self.timeStopped:
				actions = turtle.move()
				for a in actions:
					self.makeMove(a)
				self.eatenTurtles.remove(turtle)
				self.organisms.append(turtle)
				actions = []

		self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]
		for o in self.organisms:
			if o not in self.timeStopped:
				o.liveLength -= 1
				o.power += 1
				if o.liveLength < 1:
					print(str(o.__class__.__name__) + ': died of old age at: ' + str(o.position))
		self.organisms = [o for o in self.organisms if o.liveLength > 0]

		self.newOrganisms = [o for o in self.newOrganisms if self.positionOnBoard(o.position)]
		self.organisms.extend(self.newOrganisms)
		self.organisms.sort(key=lambda o: o.initiative, reverse=True)
		self.newOrganisms = []
		self.eatenTurtles.extend(self.newEatenTurtles)
		self.newEatenTurtles = []
		self.ochronaPrzyrody()
		self.turn += 1

	def makeMove(self, action):
		print(action)
		if action.action == ActionEnum.A_ADD:
			self.newOrganisms.append(action.organism)
		elif action.action == ActionEnum.A_INCREASEPOWER:
			action.organism.power += action.value
		elif action.action == ActionEnum.A_MOVE:
			action.organism.position = action.position
		elif action.action == ActionEnum.A_REMOVE:
			action.organism.position = Position(xPosition=-1, yPosition=-1)

	def addOrganism(self, newOrganism):
		newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)

		if self.positionOnBoard(newOrgPosition):
			self.organisms.append(newOrganism)
			self.organisms.sort(key=lambda org: org.initiative, reverse=True)
			return True
		return False

	def positionOnBoard(self, position):
		return position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY

	def getOrganismFromPosition(self, position):
		pomOrganism = None

		for org in self.organisms:
			if org.position == position:
				pomOrganism = org
				break
		if pomOrganism is None:
			for org in self.newOrganisms:
				if org.position == position:
					pomOrganism = org
					break
		return pomOrganism

	def getNeighboringPositions(self, position):
		result = []
		pomPosition = None

		for y in range(-1, 2):
			for x in range(-1, 2):
				pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
				if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
					result.append(pomPosition)
		return result

	def filterFreePositions(self, fields):
		result = []

		for field in fields:
			if self.getOrganismFromPosition(field) is None:
				result.append(field)
		return result

	# filter all free positiona on board
	def filterAllFreePositions(self):
		result = []
		for y in range(0, self.worldX):
			for x in range(0, self.worldY):
				field = Position(xPosition = x,yPosition = y)
				if self.getOrganismFromPosition(field) is None:
					result.append(field)
		return result

	# show all free positiona on board
	def showAllFreePositions(self):
		freePositions = self.filterAllFreePositions()
		freePositionsCoords = []
		for pos in freePositions:
			freePositionsCoords.append((pos.x, pos.y))
		return freePositionsCoords

	# function to add organism by hand by user from main
	def userAddOrganism(self, organism, position):
		if organism == 1:
			newOrg = Antelope(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 2:
			newOrg = Dandelion(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 3:
			newOrg = Grass(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 4:
			newOrg = Sheep(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 5:
			newOrg = Toadstool(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 6:
			newOrg = Turtle(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 7:
			newOrg = Ufo(position=position, world=self)
			self.addOrganism(newOrg)
		elif organism == 8:
			newOrg = Wolf(position=position, world=self)
			self.addOrganism(newOrg)

	def filterPositionsWithoutAnimals(self, fields):
		result = []
		pomOrg = None

		for filed in fields:
			pomOrg = self.getOrganismFromPosition(filed)
			if pomOrg is None or isinstance(pomOrg, Plant):
				result.append(filed)
		return result

	def filterPositionsWithOtherSpecies(self, fields, species):
		result = []
		for filed in fields:
			pomOrg = self.getOrganismFromPosition(filed)
			if not isinstance(pomOrg, species):
				result.append(filed)
		return result

	#Sorts organims base on number of their memebers, return sorted list from most to least
	def sortOrganisms(self):
		countOrganisms = {"Wolf":0, "Ufo":0, "Turtle":0, "Toadstool":0,"Sheep":0, "Grass":0, "Dandelion":0, "Antelope":0}
		for org in self.organisms:
			countOrganisms[org.__class__.__name__]+=1
		sortedCountOrganisms = sorted(countOrganisms.items(), key=lambda x: x[1], reverse=True)
		while sortedCountOrganisms and not sortedCountOrganisms[-1][1]:
			if sortedCountOrganisms[-1][1] == 0:
				sortedCountOrganisms.pop()
		return sortedCountOrganisms

	#sort organism by its number, if difference between the most common and the lest is more than 3 kill 1 most
	#common, sort organisms and check the condition again. 0 number species are not taken into account
	def ochronaPrzyrody(self):
		sortedOrganisms = self.sortOrganisms()
		if sortedOrganisms:
			while (sortedOrganisms[0][1] - sortedOrganisms[-1][1])>=3:
				sortedOrganisms = self.sortOrganisms()
				for org in self.organisms:
					if org.__class__.__name__ == sortedOrganisms[0][0]:
						print("{0} from: {1} removed from the wolrd due to nature defence".format(org.__class__.__name__, org.position))
						org.position = Position(xPosition=-1, yPosition=-1)
						break
				self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]

	def __str__(self):
		result = '\nturn: ' + str(self.__turn) + '\n'
		for wY in range(0, self.worldY):
			for wX in range(0, self.worldX):
				org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
				if org:
					result += str(org.sign)
				else:
					result += self.separator
			result += '\n'
		return result
