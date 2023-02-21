from random import shuffle

"""
# class card
    suits,rank,value 
"""

# global varibales 

suits = ("Daimonds","Clubs","Spades","Hearts")
ranks = ("Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Jack" , "Queen" , "King" , "Ace")
values = {
    "Two" : 2 , "Three" : 3 , "Four" : 4 , "Five" : 5 , "Six" : 6 , "Seven" : 7 , "Eight" : 8 , "Nine" : 9 , "Ten" : 10 , "Jack" : 11 , "Queen" : 12 , "King" : 13 , "Ace" :14 
    }


# card class to create a suit,rank, and value for each card
class Card:

    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank 
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# two_of_hearts = Card("Hearts" , "Two")

# print(two_of_hearts)
# print(two_of_hearts.value)


# three_of_spades = Card("Spades", "Three")
# print(three_of_spades)
# print(three_of_spades.value)

# print(three_of_spades.value > two_of_hearts.value)

# create a Card class to initialize the deck for all 52 cards

class Deck:
    

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def suffle_dec(self):
        shuffle(self.all_cards)
        # print(Deck.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()
# new_deck.suffle_dec()

# myCard = new_deck.deal_one()
# print(myCard)
# print(len(new_deck.all_cards))
# print(new_deck.all_cards)

# for d in new_deck.all_cards:
    # print(d)


class Player: 

    def __init__(self, name ):
        self.name = name
        self.all_cards = [] 

    # we remove to card from the top of the deck
    def remove_one(self):
        # if len(self.all_cards) > 1:
        return self.all_cards.pop(0)
            # first_card = self.all_cards[0]
            # self.all_cards = self.all_cards[1::]
            # return first_card
        # return "cards deck is empty"

    # we add the card/cards to the list from the bottom
    def add_cards(self, new_cards):
        # to check if the player is having more than one card 
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            # to add the single card to the list 
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards'
    

# player_1 = Player("mayur")

# print(player_1)
# print(player_1.remove_one())

# player_1.add_cards(myCard)
# player_1.add_cards([myCard,myCard,myCard, "test"])
# print(player_1)
# print(player_1.remove_one())
# for p in player_1.all_cards:
#     print(" --- ", p)

player1 = Player("One")
player2 = Player("Two")

new_game = Deck()
new_game.suffle_dec()


for card in range(26):
    player1.add_cards(new_game.deal_one())
    player2.add_cards(new_game.deal_one())

print(len(player1.all_cards))
print(len(player2.all_cards))

game_on = True
round_num = 0 

while game_on:
    
    round_num += 1
    print(f'round {round_num}')

    if len(player1.all_cards) == 0:
        print("player one is out of cards, player Two wins")
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print("player Two is out of cards, player One wins")
        game_on = False
        break

    # starting a new round 

    player1_cards = []
    player1_cards.append(player1.remove_one())

    player2_cards = []
    player2_cards.append(player2.remove_one())

    print(" pl all cards --- -- - - " , len(player1.all_cards))
    print(" p2 all cards --- -- - - " , len(player2.all_cards))
    war_on = True
    # while war on 
    while war_on:

        if player1_cards[-1].value > player2_cards[-1].value:
            print(" --- -- - - p1 len" , len(player1_cards))

            player1.add_cards(player1_cards) 
            player1.add_cards(player2_cards)
            war_on = False

        elif player1_cards[-1].value < player2_cards[-1].value:
            print(" --- -- - - p2 len " , len(player2_cards))
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            war_on = False

        else: 
            print('WaaaRRR !!')
            if len(player1.all_cards) < 5:
                print("Player One in out of cards ")
                print("player 2 Wins")
                game_on = False
                break
            elif len(player2.all_cards) < 5:
                print('player Two is out of cards')  
                print("player 1 Wins")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())


