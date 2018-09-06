#Introduction and checking to see if user would like to see the rules
def welcome_sequence():
    print("Welcome to Flapjack!")
    condition = True
    while condition == True:
        rules = input("If you would like to read the rules now, please enter y. If not, please enter n: ")
        if rules.upper() == "Y":
            print("Rules: ")
            print("1) The cards must first be split into their four respective suits and 2 decks will be created with one colour each per deck. One deck for each player.")
            print("2) Decks must then be shuffled and placed face down.")
            print("3) The dealer will then start their turn first, picking a card from their deck one by one until they decide to hold or are bust.")
            print("4) The goal is to get 25, any value above 25 is an automatic bust.")
            print("5) If the value of the hand is between 16-24, the score will be calculated by: 25 - value. After games are finished, player with score closest to 0 wins.") 
            print("6) Black cards have a positive value whereas Red cards have a negative value.")
            print("7) A total number of 5 games will be played, after which the winner will be decided upon.")
            print("8) Cards from 2 - 10 are face value, Jacks, Queens and Kings are worth 10 and the Ace is worth either 1 or 11 (decided by the user)")
            condition = False
        elif rules.upper() == "N":
            print("Moving on.")
            condition = False
        else:
            print("There was an error with your input, please try again")
