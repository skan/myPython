from data import *
from functions import *

sk_listToGuess = ["*"]*8
wordToguess = "fonction"

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