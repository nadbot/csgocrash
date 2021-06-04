from goldenBabies import GoldenBabies
from population import Population
import pandas as pd

goal = 100

test = Population(2)
df = pd.read_csv('DATASET_ALL_17_2.csv')
values = df.to_numpy()
values = values[0:1000]
print("Values from " + str(0) + " to " + str(1000))
for baby in range(len(test.babies)):
    test.babies[baby].correct_values = values
f = open("god_bots.csv", "r")
bots = []
for i in range(2):
    accuracy = f.readline()
    balance = f.readline()
    fitness = f.readline()
    won = f.readline()
    lost = f.readline()
    directions = f.readline()
    directions = directions[1:-2]
    li = list(directions.split(","))
    for el in range(len(li)):
        li[el] = li[el].strip()
        li[el] = int(li[el])
    print(li)
    print(li[0])
    bot = {}
    bot['accuracy'] = accuracy
    bot['balance'] = balance
    bot['fitness'] = fitness
    bot['won'] = won
    bot['lost'] = lost
    bot['directions'] = li
    bots.append(bot)

for i in range(len(bots)):
    test.babies[i].brain.directions = bots[i]['directions']
for j in range(10000, 20000):
    if test.allDotsDead():
        values = df.to_numpy()
        values = values[j:j+1000]
        print("Values from " + str(j) + " to " + str(j+1000))
        test.calculateFitness()
        test.naturalSelection()
        test.mutateDemBabies()
        # previous_dead = j
        print(test.gen)
        for baby in range(len(test.babies)):
            test.babies[baby].correct_values = values
    else:
        # if any of the dots are still alive then update and then show them
        test.update()
# test.show_results()
max_balance = -100
best_baby = 0
for i in range(len(test.babies)):
    if test.babies[i].balance > max_balance:
        max_balance = test.babies[i].balance
        best_baby = i
print(test.babies[best_baby].balance)
print(test.babies[best_baby].fitness)
print((test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
print(test.babies[best_baby].won_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
print(test.babies[best_baby].lost_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
# print(test.babies[0].brain.directions)
print(test.gen)
