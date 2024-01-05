import random

def random_card(cards):
  random_card = random.choice(cards)
  random_card.chosen = True
  return random_card



