import random
from math import ceil

wallet = 1000

isPlayOnGoing = 1
while isPlayOnGoing:
    print ("Amount in your wallet: {0} $".format(wallet))
    bet_number = -1
    bet_amount = -1
    while (bet_number < 0 or bet_number > 49):
        try:
            bet_number = raw_input ("type the number you wanna bet on: ")
            bet_number= int (bet_number)
        except:
            bet_number = -1
            print ("not a number")
        if (bet_number <0 or bet_number > 50):
            print ("number must between 0 & 49")
            bet_number = -1

    while bet_amount < 0 or bet_amount > wallet:
        try:
            bet_amount = input ("Amount you wanna bet on: ")
            bet_amount = int (bet_amount)
        except:
            bet_amount = -1
            print ("not a number")
        if (bet_amount < 0  or bet_amount > wallet):
            print("you don't have that amount")
            bet_amount = -1


    result = random.randrange(49)
    print ("   the ball is on the number : {0}".format(result))

    # compute bet reward
    if bet_number == result:
        print ("      GOOD: same number ! you win 3*bet") 
        wallet += bet_amount * 4
    elif (bet_number % 2) == (result %2 ):
        print ("      Good: same color ! you win 0.5 * bet")
        wallet += ceil(bet_amount * 1.5)
    else:
        print ("      Sorry, you lost your bet")
        wallet -= bet_amount

    if (wallet <= 0):
       print ("you don't have money anymore")
       isPlayOnGoing = 0
    else:
        keepPlaying = raw_input("continue playing y/n : ")
        if keepPlaying is 'n' or keepPlaying is 'N':
            isPlayOnGoing = 0
            print("Thank your for playing with us, bye.")