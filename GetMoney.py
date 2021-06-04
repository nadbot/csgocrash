from goldenBabies import GoldenBabies
from population import Population
import pandas as pd

goal = 100
while True:
    test = Population(100)
    df = pd.read_csv('DATASET_ALL_17_2.csv')
    values = df.to_numpy()
    values = values[0:1000]
    print("Values from " + str(0) + " to " + str(1000))
    for baby in range(len(test.babies)):
        test.babies[baby].correct_values = values
    # for i in range(100):
    # previous_dead = 0
    for j in range(1000000):
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


    test.show_results()
    max_balance = -100
    best_baby = 0
    for i in range(len(test.babies)):
        if test.babies[i].balance > max_balance:
            max_balance = test.babies[i].balance
            best_baby = i
    print(test.babies[best_baby].balance)
    print((test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
    print(test.babies[best_baby].won_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
    print(test.babies[best_baby].lost_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))
    # print(test.babies[0].brain.directions)
    print(test.gen)
    if test.babies[best_baby].won_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets) > 0.92:
        f = open("best_values.csv", "a")
        f.write("\n")
        f.write(str((test.babies[best_baby].won_bets/(test.babies[best_baby].won_bets+test.babies[best_baby].lost_bets))) + "\n")
        f.write(str(test.babies[best_baby].balance)+"\n")
        f.write(str(test.babies[best_baby].fitness)+"\n")
        f.write(str(test.babies[best_baby].won_bets)+"\n")
        f.write(str(test.babies[best_baby].lost_bets)+"\n")
        f.write(str(test.babies[best_baby].brain.directions)+"\n")
        f.close()
