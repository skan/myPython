from data import *
from functions import *
import random
import pickle

def save_score(score):
   with open('score', 'wb') as f_player:
      pickle_players = pickle.Pickler(f_player)
      pickle_players.dump(score)
def load_score ():
   with open('score', 'rb') as f_player:
      players = pickle.Unpickler(f_player)
      score_loaded = players.load()
      return score_loaded

dic_playerList = load_score()
actual_player=str(raw_input ("welcome, your name pls: "))
if actual_player in dic_playerList.keys():
   actual_score = dic_playerList.get(actual_player)
   print ("welcome {0} , your actual score is {1}".format(actual_player,actual_score))
else:
   dic_playerList[actual_player] = 0
   newPlayer = 1
   print ("New playser: welcome {0} , your actual score is {1}".format(actual_player,dic_playerList[actual_player]))

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

save_score(dic_playerList)