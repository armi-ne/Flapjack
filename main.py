import deck_simple
import intro
import random
import os
clear = lambda: os.system('cls')

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
    while (counter <= 25) and not (counter >= 20) and (len(bot_deck_new) >0):
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
        counter += value
        bot_deck_new.remove(card)
    if counter > 25:
        return 25
    else:
        return 25 - counter

#User's turn to play
def user_play():
    user_cont = True
    value = 0
    while (user_cont == True) and (value <= 25) and (len(user_deck_new) > 0):
        print("The current value of your deck is: {0}".format(value))
        card = random.choice(user_deck_new)
        colour = ""
        colour_present = ""
        suit = ""
        face = ""
        if card[0] == "c" or card[0] == "s":
            colour = "b"
            colour_present = "Black"
        else:
            colour = "r"
            colour_present = "Red"
        if card[0] == "c":
            suit = "Clubs"
        elif card[0] == "d":
            suit = "Diamonds"
        elif card[0] == "h":
            suit = "Hearts"
        elif card[0] == "s":
            suit = "Spades"
        if len(card) >= 3:
            face = "10"
        elif card[1:] == "k":
            face = "King"
        elif card[1:] == "j":
            face = "Jack"
        elif card[1:] == "q":
            face = "Queen"
        elif card[1:] == "a":
            face = "Ace"
        else:
            face = str(card[1:])
        print("You have been dealt the {0} of {1}, which is a {2} card".format(face, suit, colour_present))
        if colour == "b":
            if len(card) == 3:
                value += 10
            if card[1].isnumeric():
                if int(card[1]) >= 2 and int(card[1]) < 10:
                    value += int(card[1])
            elif card[1] == "a":
                ask = input("You've been dealt a black Ace, would you like to use it as a 1 or an 11?: ")
                if ask == "1":
                    value += 1
                elif ask == "11":
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
                ask = input("You've been dealt a red Ace, would you like to use it as a 1 or an 11? ")
                if ask == "1":
                    value -= 1
                elif ask == "11":
                    value -= 11
            else:
                value -= 10
        print("The new value of your hand is {0} and there are {1} cards left in your deck.".format(value, len(user_deck_new)))
        if value > 25:
            print("Sorry, but you just got bust.")
            break
        elif value == 25:
            print("Congratulations! You managed to get 25.")
            break
        carry_on_or_hold = input("Would you like to carry on (Y) or fold (N)? Y/N: ")
        if carry_on_or_hold.upper() == "Y":
            user_cont = True
        else:
            user_cont = False
        user_deck_new.remove(card)
        clear()
    if value > 25:
        return 25
    else:
        return 25 - value

bot_score = bot_play()
print("User's Turn")
user_score = user_play()
print("")
print("Bot score: {0}".format(bot_score))
print("User score: {0}".format(user_score))
