from goldenBabies import GoldenBabies
import random


class Population:
    babies = []
    fitnessSum = 0
    gen = 1
    bestDot = 0  # the index of the best dot in the dots[]
    minStep = 1000

    def __init__(self, size):
        for i in range(size):
            self.babies.append(GoldenBabies())

    def update(self):
        for i in range(len(self.babies)):
            if self.babies[i].brain.step > self.minStep:
                # if the dot has already taken more steps than the best dot has taken to reach the goal
                self.babies[i].dead = True
            else:
                self.babies[i].update()

    def calculateFitness(self):
        for i in range(len(self.babies)):
            self.babies[i].calculateFitness()

    def allDotsDead(self):
        for i in range(len(self.babies)):
            if not self.babies[i].dead and not self.babies[i].reachedGoal:
                return False
        return True

    def naturalSelection(self):
        # newBabies = GoldenBabies[dots.length]; // next gen
        new_babies = [None] * len(self.babies)
        best_baby = self.setBestBaby()
        self.calculateFitnessSum()

        # the champion lives on
        new_babies[0] = self.babies[best_baby].gimmeBaby()
        new_babies[0].isBest = True

        for i in range(len(new_babies)):
            parent = self.selectParent()
            new_babies[i] = parent.gimmeBaby()

        self.babies = new_babies

        self.gen += 1

    def calculateFitnessSum(self):
        self.fitnessSum = 0
        for i in range(len(self.babies)):
            self.fitnessSum += self.babies[i].fitness

    # chooses dot from the population to return randomly(considering fitness)
    # this function works by randomly choosing a value between 0 and the sum of all the fitnesses
    # then go through all the dots and add their fitness to a running sum and
    # if that sum is greater than the random value generated that dot is chosen since dots
    # with a higher fitness function add more to the running sum then they have a higher chance of being chosen
    def selectParent(self):
        rand = random.random()*self.fitnessSum

        runningSum = 0
        for i in range(len(self.babies)):
            runningSum += self.babies[i].fitness
            if runningSum > rand:
                return self.babies[i]

    def mutateDemBabies(self):
        for i in range(len(self.babies)):
            self.babies[i].brain.mutate()

    def setBestBaby(self):
        max = 0

        maxIndex = 0
        for i in range(len(self.babies)):
            if self.babies[i].fitness > max:
                max = self.babies[i].fitness
                maxIndex = i
                # print("Found new best baby: " + str(i) + " : " + str(max))

        bestDot = maxIndex

        # if this dot reached the goal then reset the minimum number of steps it takes to get to the goal
        if self.babies[bestDot].reachedGoal:
            minStep = self.babies[bestDot].brain.step
            print("step:", minStep)

        return bestDot

    def show_results(self):
        for i in self.babies:
            print(i.balance)
