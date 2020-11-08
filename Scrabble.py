# Code developped by Linda Pérez in 11-November-2020

# List of acceptable tiles to play
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# Dictionary of the relationship of letters with points
letters_to_points = {key:value for key,value in zip(letters, points)}
# Adds space as a tile
letters_to_points[""] = 0
# List of players
players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
# Dictionary of player's words'
player_to_words = { player:{} for player in players} 
# Dictionary of player's score
player_to_points = { player:0 for player in players}

def get_words(player):
  played_words = ""
  for word in player_to_words[player]:
    played_words += word.title() + " "
  return played_words

# Gets player with higher score
def get_score():
  winner_score = 0
  for player, score in player_to_points.items():
    print("{} played: {}and got {} points.".format(player, get_words(player), score))
    if winner_score < score:
      winner_score = score
      winner = player
  print("\nThe winner is {}.".format(winner))

# Get words score
def score_word(lst):
  point_total = 0
  for word in lst:
    for letter in word:
      point_total +=letters_to_points.get(letter.upper(),0)
  return point_total

# Adds points to player
def update_point_totals(player, word):
  player_to_points[player] += score_word(word)
  return 0

# Adds played word to player
def play_word(player, word):
  try:
    player_to_words[player] += word
  except TypeError:
    player_to_words[player] = word
  update_point_totals(player, word)
  return 0


# Play simulation
play_word("player1", ["BLUE","TENNIS","EXIT"])
play_word("wordNerd", ["EARTH","EYES","MACHINE"])
play_word("Lexi Con", ["ERASER","BELLY","HUSKY"])
play_word("Prof Reader", ["ZAP","COMA","PERIOD"])
get_score()

