from data import *
from functions import *
import random

sk_listToGuess = ["*"]*8
wordToguess = random.choice(words_list)

step = 0
while step < MAX_TRIALS:
   print ("".join(sk_listToGuess))
   trial = raw_input ("give a letter: ")
   result = [pos for pos, char in enumerate(wordToguess) if char == str(trial)]
   if len(result) == 0:
      print ("letter not found")
   else:
      for position in result:
         sk_listToGuess [position] = trial
   step += 1
print("the word to guess: {0}".format(wordToguess))