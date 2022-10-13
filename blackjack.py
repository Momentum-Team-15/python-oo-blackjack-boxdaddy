import random

#outline classes

SUITS = ['♥️', '♣️', '♦️','♠️']
RANK_VALUES = {
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': 11,
    # TODO handle when A is 1
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9, 
    10: 10,
}

class Game:
    def __init__(self):
        self.deck = Deck('Bicycle')
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        #deal 2 cards to dealer and player
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.player)

        print("The dealer's cards are: ")
        for card in self.dealer.hand:
            print(card)
        print(f'This hand is worth {self.calculate_hand(self.dealer)}')

        print("The player's cards are: ")
        for card in self.player.hand:
            print(card)
        print(f'This hand is worth {self.calculate_hand(self.player)}')

        print(f'There are now {len(self.deck.cards)} in the deck')

    def deal_card(self, participant):
        #take a card rom the deck and put in in someone's hand 
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        return total_points

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# example of building one card
# queen_of_hearts = Card('♥️', 'Q', 10)
# print(f'{queen_of_hearts} is worth {queen_of_hearts.value}')
# build a whole deck

class Deck:
    def __init__(self, brand):
        self.cards = []
        self.brand = brand
        self.used = False
        for suit in SUITS:
            for rank_value in RANK_VALUES.items():
                new_card = Card(suit, rank_value[0], rank_value(1))
                self.cards.append(new_card)

        def __str__(self):
            return f'{self.brand} deck of {len(self.suit)} cards'

        def shuffle(self):
            random.shuffle(self.cards)

class Player:
    def __init__(self):
        self.hand = []

class Dealer:
    def __init__(self):
        self.hand = []

# starts game, calls __init__ method
# check if dealer has 21

def play_game():
    # TODO make player go first
    if new_game.calculate_hand(new_game.dealer) == 21:
        # dealer has blackjack
        print('Dealer has blackjack!')
        if new_game.calculate_hand(newgame.player) == 21:
            # player also has blackjack
            print('Push')
            return
        else: 
            print(f'Player loses with {new_game.calculate_hand(new_game.player)}')
            # dealer does not have blackjack but player does 
            print('Player wins with blackjack!')
            return

    # nobody has blackjack, dealer's turn

    while new_game.calculate_hand(newgame.dealer) < 17:
        new_game.deal_card(new_game.dealer)
        print('Dealer hits')
        if new_game.calculate_hand(new_game.dealer) > 21:
            print(f'Dealer busted with {new_game.calculate_hand(newgame.dealer)}!')
            break

        elif new_game.calculate_hand(newgame.dealer) == 21:
            print('Dealer wins with 21!')
            break
        
    # we reach here only if the dealer has at least 17 but less than 21
    else:
        print(f"Dealer's hand is: ")
        [print(card) for card in new_game.dealer.hand]
        # this list comprehension is shorthand for
        # for card in new_game.dealer.hand:
            # print(card)
        print(f"Player's hand is: ")
        [print(card) for card in new_game.player.hand]
        # player now chooses whether to hit or stay        
        choice = ''
        while choice != 's':
            choice = input("Would you like to (h)it or (s)tay ").lower()
            if choice == 'h':
                new_game.deal_card(new_game.player)
                print(f"Player's hand is: ")
                [print(card) for card in new_game.player.hand]
                if new_game.calculate_hand(new_game.player) == 21:
                    print("Player wins with 21!")
                    break
                elif new_game.calculate_hand(new_game.player) > 21:
                    print("Player busts!")
                    break

            elif choice == 's':
                print("Player stays")
                print(f"Player's hand is: ")
                [print(card) for card in new_game.player.hand]
            else:
                print("Please choose 'h' or 's'")
        else: 
            print(f"Dealer's hand is: ")
            [print(card) for card in new_game.dealer.hand]
            print(f"Player's hand is: ")
            [print(card) for card in new_game.player.hand]
            # determine if player has more points than dealer
            dealer_points = new_game.calculate_hand(new_game.dealer)
            player_points = new_game.calculate_hand(new_game.player)
            if dealer_points > player_points:
                print(f'Dealer wins with {dealer_points}. Player has {player_points}')
            elif player_points > dealer_points:
                print(f'Player wins with {player_points}. Dealer has {dealer_points}')
            else:
                print(f"It's a draw. Both have {dealer_points}")
        
new_game = Game()
play_game()



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
