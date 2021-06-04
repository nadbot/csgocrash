import pandas as pd
import numpy as np
df = pd.read_csv('DATASET_ALL_17_2.csv')
values = df.to_numpy()
latest = 0





def get_new_value():
    global latest
    latest+=1
    return values[latest]


def bet(value):
    global balance
    global bets_done
    global bets_won
    global bets_lost
    bets_done+=1
    balance -= bet_amount
    # print("Balance before:" +str(balance))
    # print("Betting: " + str(value))
    won = False
    if value > threshold:
        balance += 1.1*bet_amount
        bets_won +=1
        won = True
    else:
        bets_lost += 1
        won = False
    return won
    # print("New balance: "+ str(balance))

def wait_turns():
    while get_new_value() > threshold:
        print("waiting")


threshold = 1.01
bet_amount = 0.5
balance = 100000

bets_done = 0
bets_won = 0
bets_lost = 0

# do_bet = False
# count = 0

# for i in range(1, len(values)):
#     # if values[i-1]< threshold:
#     bet(values[i])
#
# print(bets_done)
# print(bets_won)
# print(bets_lost)
# print(balance)

# Gewinn

#
do_bet = False
while(latest <len(values)-1):
    # previous_values =
    new_value = get_new_value()
    if new_value < threshold:
        do_bet = True

#         if bet(get_new_value()): #won bet
#             bet(get_new_value())
#             bet(get_new_value())
#             bet(get_new_value())
#
#             continue


        # test = values[latest - 20:latest+1]
        # if len(np.where(test < threshold)) >= 2:
        #     print(test)
        #     wait_turns()
        #     bet(get_new_value())



# for i in range(1, len(values)):
#     # if values[i-1]< threshold:
#     bet(values[i])
    #if values[i-4]<threshold and values[i-3]<threshold and values[i-2]<threshold and values[i-1]<threshold:
    #test = values[i-30:i-10]
    #if len(np.where(test < threshold)) >= 2:
    #    bet(values, i)

    # test = values[i-10:i-2]

    # if len(np.where(test < threshold)) >=1:
    #     if values[i-1] < threshold:
    #         do_bet = True
    #         count = 0
    # if do_bet:
    #     count+=1
    #     if count == 1:
    #         do_bet = False
    #     bet(values, i)

# print(bets_done)
# print(bets_won)
# print(bets_lost)
# print(bets_lost/bets_done)

