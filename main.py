import deck_simple
import intro
import random

#Running introduction sequence
intro.welcome_sequence()
#Splitting a deck of cards into 4 suits, then assigning 1 suit of each colour, for up to 2 suits, for a deck
bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
#Shuffling both decks
random.shuffle(bot_deck_new)
random.shuffle(user_deck_new)

#Bots turn to play
def bot_play():
    counter = 0
    while (counter <= 25) and not (counter >= 20):
        card = random.choice(bot_deck_new)
        colour = ""
        value = 0
        if card[0] == "c" or card[0] == "s":
            colour = "b"
        else:
            colour = "r"
        if colour == "b":
            if len(card) == 3:
                value += 10
            if card[1].isnumeric():
                if int(card[1]) >= 2 and int(card[1]) < 10:
                    value += int(card[1])
            elif card[1] == "a":
                value += 11
            else:
                value += 10
        elif colour == "r":
            if len(card) == 3:
                value -= 10
            if card[1].isnumeric():
                if int(card[1]) >= 2 and int(card[1]) < 10:
                    value -= int(card[1])
            elif card[1] == "a":
                value -= 11
            else:
                value -= 10
        print("counter before {0}".format(counter))
        print(card)
        print(colour)
        print(value)
        counter += value
        print("counter after {0}".format(counter))
        print("____")
    return counter

bot_score = bot_play()
print(bot_score)

#User's turn to play
