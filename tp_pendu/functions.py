import pickle
import os
from data import *

def save_score(score):
   with open('score', 'wb') as f_player:
      pickle_players = pickle.Pickler(f_player)
      pickle_players.dump(score)

def load_score ():
   if os.path.exists(score_fileName):
      f_player = open('score', 'rb')
      playersUnpcickler = pickle.Unpickler(f_player)
      score_loaded = playersUnpcickler.load()
   else:
      score_loaded = {}
   return score_loaded

def getLetter():
   trial = raw_input ("give a letter: ")
   trial = trial.lower()
   if len(trial) > 1 or not trial.isalpha():
      print ("you didn't type a correct letter")
      return getLetter()
   else:
      return trial
