from data import *
from functions import *
import random
import pickle

def save_score(score):
   with open('score', 'wb') as f_player:
      players = pickle.Pickler(f_player)
      players.dump(score)
def load_score ():
   with open('score', 'rb') as f_player:
      players = pickle.Unpickler(f_player)
      score_loaded = players.load()
      return score_loaded

player_list = load_score()
print (player_list)

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