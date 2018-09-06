import deck_simple
import intro

#Running introduction sequence
intro.welcome_sequence()
#Splitting a deck of cards into 4 suits, then assigning 1 suit of each colour, for up to 2 suits, for a deck
bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)

print(bot_deck_new)
print(user_deck_new)