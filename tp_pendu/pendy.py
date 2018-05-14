from data import *
from functions import *
import random
import pickle


dic_playerList = load_score()
actual_player=str(raw_input ("welcome, your name pls: "))

#check if playser exist and setup score
if actual_player in dic_playerList.keys():
   actual_score = dic_playerList.get(actual_player)
   print ("welcome {0} , your actual score is {1}".format(actual_player,actual_score))
else:
   dic_playerList[actual_player] = 0
   newPlayer = 1
   print ("New playser: welcome {0} , your actual score is {1}".format(actual_player,dic_playerList[actual_player]))

wordToguess = random.choice(words_list) # get a random word from list 
sk_listToGuess = ["*"]*8 #init the * display

step = 0
game_score = MAX_TRIALS
while step < MAX_TRIALS:
   print ("".join(sk_listToGuess))
   #trial = raw_input ("give a letter: ")
   trial = getLetter()
   result = [pos for pos, char in enumerate(wordToguess) if char == str(trial)]
   if len(result) == 0:
      print ("letter not found")
   else:
      for position in result:
         sk_listToGuess [position] = trial
      if (sk_listToGuess.count("*")==0):
         print ("You win: and you gain {0} points".format(step))
         dic_playerList[actual_player]+=step
         save_score(dic_playerList)
         break
   step += 1
   game_score -= 1
if (step == MAX_TRIALS):
   print("You Lose: the word to guess: {0}".format(wordToguess))
