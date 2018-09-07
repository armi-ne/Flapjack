def probability_calc(cards_in_deck, value_of_hand):
    no_of_cards_in_deck = len(cards_in_deck)
    blacks = []
    reds = []
    val_of_blacks = 0
    val_of_reds = 0
    for i in cards_in_deck:
        if i[0] == "c" or i[0] == "s":
            blacks.append(i)
        else:
            reds.append(i)
    for i in blacks:
        if i[1] == "a":
            val_of_blacks += 5
        elif i[1] == "k":
            val_of_blacks += 10
        elif i[1] == "q":
            val_of_blacks += 10
        elif i[1] == "j":
            val_of_blacks += 10
        elif len(i) > 2:
            val_of_blacks += 10
        elif i[1].isnumeric():
            val_of_blacks += int(i[1])
    for i in reds:
        if i[1] == "a":
            val_of_reds += 5
        elif i[1] == "k":
            val_of_reds += 10
        elif i[1] == "q":
            val_of_reds += 10
        elif i[1] == "j":
            val_of_reds += 10
        elif len(i) > 2:
            val_of_reds += 10
        elif i[1].isnumeric():
            val_of_reds += int(i[1])
    total_val = val_of_blacks + val_of_reds
    prob_of_red = val_of_reds / total_val
    prob_of_black = val_of_blacks / total_val
    if no_of_cards_in_deck == 26:
        return "Yes"
    elif no_of_cards_in_deck > 0:
        print("Val of Hand")
        print(value_of_hand)
        print("No of Cards in Deck")
        print(no_of_cards_in_deck)
        if value_of_hand >= 16:
            return "No"
        elif (val_of_blacks - val_of_blacks) == 0:
            return "Yes"
        elif (val_of_blacks - val_of_reds) > 0:
            return "Yes"
        elif (val_of_blacks - val_of_reds) < -0.15:
            return "No"
