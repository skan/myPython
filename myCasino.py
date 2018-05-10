import random

wallet = 1000
print ("amount in your wallet", wallet, "$")

isPlayOnGoing = 1
while isPlayOnGoing:
    bet_number = input ("type the number you wanna bet on: ")
    bet_number= int (bet_number)
    bet_amount = input ("type the amount you wanna bet on: ")
    bet_amount= int (bet_amount)
    wallet -= bet_amount

    result = random.randrange(49)

    print ("   the ball is on the number : ", result,)

    # compute bet reward
    reward = 0
    if bet_number == result:
        print ("      GOOD: same number ! you win 3*bet") 
        reward = bet_amount * 4
    elif (bet_number % 2) == (result %2 ):
        print ("      Good: same color ! you win 0.5 * bet")
        reward = bet_amount * 1.5
    else:
        print ("      Sorry, you lost your bet")

    wallet += reward
    print ("Amount in your wallet", wallet, "$")
    keepPlaying = raw_input("continue playing y/n")
    if keepPlaying == "n" or keepPlaying == "N":
       isPlayOnGoing = 0
       print("Thank your for playing with us, bye.")