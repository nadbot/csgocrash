import pandas as pd
import numpy as np
from Brain import Brain


class GoldenBabies:
    balance = 0
    is_best = False
    dead = False
    reachedGoal = False
    fitness = 0
    threshold = 1.1
    bet = 0.5
    won_bets = 0
    lost_bets = 0
    brain = Brain(1000)
    correct_values = []

    def __init__(self):
        self.balance = 0
        self.brain = Brain(1000)
        self.reachedGoal = False

    def move(self):
        if len(self.brain.directions) > self.brain.step:
            # if there are still directions left then set the acceleration as the next PVector in the direcitons array
            do_bet = self.brain.directions[self.brain.step]
            if self.correct_values[self.brain.step] > self.threshold and do_bet:
                # print("won bet", self.balance)
                self.won_bets += 1
                self.balance -= self.bet
                self.balance += self.threshold * self.bet
            elif self.correct_values[self.brain.step] <= self.threshold and do_bet:
                # print("lost bet")
                self.lost_bets += 1
                self.balance -= self.bet
            self.brain.step += 1
        else:
            # if at the end of the directions array then the dot is dead
            self.dead = True

    def update(self):
        if self.balance > 100:  # if reached goal
            self.reachedGoal = True
        elif self.balance <= -10:
            self.dead = True
        if not self.dead and not self.reachedGoal:
            self.move()

    def calculateFitness(self):
        if self.reachedGoal:
            # if the dot reached the goal then the fitness is based on the amount of steps it took to get there
            fitness = 1.0/16.0 + 10000.0/float(self.brain.step * self.brain.step)
        else:
            # if the dot didn't reach the goal then the fitness is based on how close it is to the goal
            distanceToGoal = (100 - self.balance)
            fitness = 1.0/(distanceToGoal * distanceToGoal)
        print(fitness)
        self.fitness = fitness

    def gimmeBaby(self):
        baby = GoldenBabies()
        baby.brain = self.brain.clone()  # babies have the same brain as their parents
        return baby


