sk_listToGuess = ["*"]*8
print sk_listToGuess
sk_stringToDisplay= "".join(sk_listToGuess)
print sk_stringToDisplay

wordToguess = "fonction"
step = 0
while step < 10:
   trial = raw_input ("give a letter: ")
   print ("your propositin is the letter {0}".format(trial))
   #postion = wordToguess.find(str(trial))
   result = [pos for pos, char in enumerate(wordToguess) if char == str(trial)]
   if len(result) == 0:
      print ("letter not found")
   else:
      for position in result:
         sk_listToGuess [position] = trial
   sk_stringToDisplay= "".join(sk_listToGuess)
   print sk_stringToDisplay
   step += 1