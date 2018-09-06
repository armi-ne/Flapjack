import random

cards = ["ca", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck", "da", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk", "ha", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk", "sa", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk"]

clubs_deck = cards[:int(len(cards)/4)]
diamonds_deck = cards[int(len(cards)/4):int(len(cards)/4*2)]
heart_deck = cards[int(len(cards)/4*2):int(len(cards)/4*3)]
spades_deck = cards[int(len(cards)/4*3):int(len(cards)/4*4)]

deck = [clubs_deck, diamonds_deck, heart_deck, spades_deck]

def get_hand(current, deck):
    random_deck = random.choice(deck)
    deck_colour = ""
    if random_deck[0][0] == "c" or random_deck[0][0] == "s":
        deck_colour = "b"
    else:
        deck_colour = "r"
    if current == "bot":
        if len(bot_deck) == 0:
            bot_deck.append(random_deck)
        if len(bot_deck) == 1:
            colour_to_avoid = ""
            if bot_deck[0][0][0] == "c" or bot_deck[0][0][0] == "s":
                colour_to_avoid = "b"
            else:
                colour_to_avoid = "r"
            if random_deck not in bot_deck and deck_colour != colour_to_avoid:
                bot_deck.append(random_deck)

bot_deck = []
user_deck = []

def deal_hand():
    condition = True
    while condition:
        if len(bot_deck) <= 1:
            get_hand("bot", deck)
        else:
            condition = False
    for i in deck:
        if i not in bot_deck:
            user_deck.append(i)

def add_decks(bot, user):
    bot_decks = bot[0] + bot[1]
    user_decks = user[0] + user[1]
    return bot_decks, user_decks

def run_everything(bot_deck, user_deck):
    bot_deck.clear()
    user_deck.clear()
    deal_hand()
    bot_deck_new, user_deck_new = add_decks(bot_deck, user_deck)
    return bot_deck_new, user_deck_new