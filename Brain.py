import random


class Brain:
    directions = []
    step = 0

    def __init__(self, nr):
        self.directions = [-1] * nr
        self.randomize()

    def randomize(self):
        for i in range(len(self.directions)):
            self.directions[i] = int(random.random() * 2)

    def clone(self):
        clone_brain = Brain(len(self.directions))
        for i in range(len(self.directions)):
            clone_brain.directions[i] = self.directions[i]
        return clone_brain

    # mutates the brain by setting some of the directions to random vectors
    def mutate(self):
        mutation_rate = 0.01 # chance that any vector in directions gets changed
        for i in range(len(self.directions)):
            rand = random.random()
            if rand < mutation_rate:
                self.directions[i] = int(random.random() * 2)
