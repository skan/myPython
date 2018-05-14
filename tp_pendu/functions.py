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
