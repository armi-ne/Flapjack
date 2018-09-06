import deck_simple
import intro
import random
import os
clear = lambda: os.system('cls')

#Running introduction sequence
intro.welcome_sequence()

#Game # counter
game_counter = 1

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
    if counter < 25 and counter >= 16:
        return 25 - counter
    else:
        return 25

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
    if value < 25 and value >= 16:
        return 25 - value
    else:
        return 25

def new_game():
    bot_score = 0
    user_score = 0
    bot_score = bot_play()
    print("User's Turn")
    user_score = user_play()
    print("")
    print("Bot score: {0}".format(bot_score))
    print("User score: {0}".format(user_score))
    return bot_score, user_score

game_1 = []
game_2 = []
game_3 = []
game_4 = []
game_5 = []

if game_counter == 1:
    bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
    bot_score, user_score = new_game()
    game_1.append(bot_score)
    game_1.append(user_score)
    game_counter += 1
    print("Game 1 finished!")
if game_counter == 2:
    bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
    bot_score, user_score = new_game()
    game_2.append(bot_score)
    game_2.append(user_score)
    game_counter += 1
if game_counter == 3:
    bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
    bot_score, user_score = new_game()
    game_3.append(bot_score)
    game_3.append(user_score)
    game_counter += 1
if game_counter == 4:
    bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
    bot_score, user_score = new_game()
    game_4.append(bot_score)
    game_4.append(user_score)
    game_counter += 1
if game_counter == 5:
    bot_deck_new, user_deck_new = deck_simple.run_everything(deck_simple.bot_deck, deck_simple.user_deck)
    bot_score, user_score = new_game()
    game_5.append(bot_score)
    game_5.append(user_score)
    final_list = [game_1, game_2, game_3, game_4, game_5]
    print(final_list)
    bot_final = 0
    user_final = 0
    for i in final_list:
        bot_final += i[0]
    for i in final_list:
        user_final += i[1]
    if user_final < bot_final:
        print("Congratulations! Out of 5 games, you managed to win with a score of {0}.".format(user_final))
        print("Scores for game 1 (bot, user):" + str(game_1))
        print("Scores for game 2 (bot, user):" + str(game_2))
        print("Scores for game 3 (bot, user):" + str(game_3))
        print("Scores for game 4 (bot, user):" + str(game_4))
        print("Scores for game 5 (bot, user):" + str(game_5))
        print("Final scores = Bot: {0}, User: {1}.".format(bot_final, user_final))
    elif bot_final > user_final:
        print("Sorry, but the bot won this time with a score of {0}.".format(user_final))
        print("Scores for game 1 (bot, user):" + str(game_1))
        print("Scores for game 2 (bot, user):" + str(game_2))
        print("Scores for game 3 (bot, user):" + str(game_3))
        print("Scores for game 4 (bot, user):" + str(game_4))
        print("Scores for game 5 (bot, user):" + str(game_5))
        print("Final scores = Bot: {0}, User: {1}.".format(bot_final, user_final))
