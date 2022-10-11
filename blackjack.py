import random
# planning phase
# create empty dealer cards list
dealer_cards = []
# create empty player cards list
player_cards = []

# deal 2 cards to dealer / show only dealer's 2nd card
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# deal 2 cards to player / show both cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# show sum of dealer's cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# show sum of player's cards / get player input
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?"))
    # player chooses hit / calculate new sum
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("New total " + str(sum(player_cards)) + " from ", player_cards)
    # player chooses stay / reveal dealer's cards
    else:
        print("Dealer has " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("New total " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break
if sum(player_cards) > 21:
    print("Busted, dealer wins.")
elif sum(player_cards) == 21:
    print("Yaaay blackjack.")


# compare te sums of the cards between D v P
# if P card sum > 21 = BUST
# if P card sum < 21 = option hit or stay
# if P option stay compare sum of D v P
# if P sum < 21 && D sum then P wins
# if P sum < D sum then P loses
