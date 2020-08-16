from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Wolf import Wolf
from Position import Position
import random

class Antelope(Animal):

	def __init__(self, antelope=None, position=None, world=None):
		super(Antelope, self).__init__(antelope, position, world)

	def clone(self):
		return Antelope(self, None, None)

	def initParams(self):
		self.power = 3
		self.initiative = 3
		self.liveLength = 10
		self.powerToReproduce = 6
		self.sign = 'A'

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

	def getNeighboringWolf(self):
		neighboringPositions = self.world.getNeighboringPositions(self.position)
		for pos in neighboringPositions:
			if isinstance(self.world.getOrganismFromPosition(pos), Wolf):
				return self.world.getOrganismFromPosition(pos)

	#New definition of move for Antelope. If near is Wolf then newPosition is 2 fields away,
	# if it is on board it is new position, if not go to Wolf position. Else behave normally as sheep
	def move(self):
		result = []
		pomPositions = self.getNeighboringPositions()
		newPosition = None
		neighboringWolf = self.getNeighboringWolf()
		if neighboringWolf:
			diffPosition = (self.position.x - neighboringWolf.position.x, self.position.y - neighboringWolf.position.y)
			newPosition = Position(xPosition=self.position.x + 2 * diffPosition[0], yPosition=self.position.y + 2 * diffPosition[1])
			if not self.world.positionOnBoard(newPosition):
				newPosition = neighboringWolf.position
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		elif pomPositions:
			newPosition = random.choice(pomPositions)
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		return result
