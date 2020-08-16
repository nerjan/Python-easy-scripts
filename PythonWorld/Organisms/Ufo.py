from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
import random

class Ufo(Animal):

    def __init__(self, ufo=None, position=None, world=None):
        super(Ufo, self).__init__(ufo, position, world)

    def clone(self):
        return Ufo(self, None, None)

    def initParams(self):
        self.power = 5
        self.initiative = 99
        self.liveLength = 10
        self.powerToReproduce = 13
        self.sign = 'U'

    def getNeighboringPositions(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))

    def consequences(self, atackingOrganism):
        result = []
        atackingOrganism.position = atackingOrganism.lastPosition
        return result

    #take all surrounding orgnisms except Ufo
    def filterOrganismsToBeStopped(self):
        positionsWithOtherSpecies = self.world.filterPositionsWithOtherSpecies(self.world.getNeighboringPositions(self.position), Ufo)
        surroundingOrganisms = []
        for pos in positionsWithOtherSpecies:
            if self.world.getOrganismFromPosition(pos) is not None:
                surroundingOrganisms.append(self.world.getOrganismFromPosition(pos))
        return surroundingOrganisms


    def move(self):
        result = []
        pomPositions = self.getNeighboringPositions()
        newPosition = None

        if pomPositions:
            newPosition = random.choice(pomPositions)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
            self.lastPosition = self.position
        #add all surrounding organisms to stop their time
        self.world.timeStopped.extend(self.filterOrganismsToBeStopped())
        return result
