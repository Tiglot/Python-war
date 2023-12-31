import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.suit + " of " + self.rank


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_one(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


Player_1 = Player("Pedro")
Player_2 = Player("João")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    Player_1.add_one(new_deck.deal_one())
    Player_2.add_one(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print("Round " + str(round_num))
    if round_num >= 5000:
        print("Muitos rounds, vão dormir")
        game_on = False
        break

    elif len(Player_1.all_cards) == 0:
        print(Player_1.name + " lost")
        game_on = False
        break

    elif len(Player_2.all_cards) == 0:
        print(Player_2.name + " lost")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(Player_1.remove_one())

    player_two_cards = []
    player_two_cards.append(Player_2.remove_one())
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            Player_1.add_one(player_one_cards)
            Player_1.add_one(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            Player_2.add_one(player_one_cards)
            Player_2.add_one(player_two_cards)
            at_war = False
        else:
            print("WAR")
            if len(Player_1.all_cards) < 5:
                print(Player_1.name + " lost, can't declare war")
                game_on = False
                break
            elif len(Player_2.all_cards) < 5:
                print(Player_2.name + " lost, can't declare war")
                game_on = False
                break
            else:
                for i in range(5):
                    player_one_cards.append(Player_1.remove_one())
                    player_two_cards.append(Player_2.remove_one())
