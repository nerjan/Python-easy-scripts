from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Toadstool import Toadstool

class Turtle(Animal):

	def __init__(self, turtle=None, position=None, world=None):
		super(Turtle, self).__init__(turtle, position, world)
		self.animalWhichEatMe = None

	def clone(self):
		return Turtle(self, None, None)

	def initParams(self):
		self.power = 1
		self.initiative = 1
		self.liveLength = 20
		self.powerToReproduce = 15
		self.sign = 'O'

	def getNeighboringPositions(self):
		if self.animalWhichEatMe:
			return self.findPositionAfterBeingSpittedOut()
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

	def findPositionAfterBeingSpittedOut(self):
		newPosition = self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.animalWhichEatMe.position))
		self.animalWhichEatMe = None
		return newPosition

	def consequences(self, atackingOrganism):
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
			#if turtle is eaten then it goes to eatenTurtle list to resurect in next turn with animal which eat him attached
			if atackingOrganism.__class__.__name__ != Toadstool.__class__.__name__:
				self.animalWhichEatMe = atackingOrganism
				self.world.newEatenTurtles.append(self)
		return result
