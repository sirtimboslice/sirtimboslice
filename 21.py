import random
from colorama import Fore, Style


suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten', \
         'Jack','Queen','King','Ace')
values = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7, \
          'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self):
        self.total = int(input('How much money would you like add to your starting bank? '))
        self.bet = 0

    def win_bet(self):
        self.total += (self.bet)*1.2

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to bet? '))
            return chips.bet
        except ValueError:
            print('Please input a number.')
        else:
            if chips.bet > chips.total:
                print('You do not have enough money to make that bet.')
                print('Your bank is at: ' + Fore.LIGHTGREEN_EX + chips.total + Style.RESET_ALL)
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing
    playing = True
    while playing == True:
        x = input('\nWould you like to Hit or Stand? Enter H or S: ').upper()
        if x == 'H':
            hit(deck,hand)
        elif x == 'S':
            print('Stand. Dealer turn.')
            playing = False
        else:
            print('Enter H or S')
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print(Fore.RED,"\nPlayer busts!",Style.RESET_ALL)
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print(Fore.LIGHTGREEN_EX,"\nPlayer wins!",Style.RESET_ALL)
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print(Fore.LIGHTGREEN_EX,"\nDealer busts!",Style.RESET_ALL)
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(Fore.RED,"\nDealer wins!",Style.RESET_ALL)
    chips.lose_bet()


def push():
    print(Fore.YELLOW,"Dealer and Player tie! It's a push.",Style.RESET_ALL)


def clear_screen():
    print('\n'*100)


# Start of game logic
def play_game():
    print('Welcome to Blackjack!\nI am your dealer, Monty.')
    print('Wins pay 1.2x\n')
    begin = input('Are you ready to begin? Y or N ').upper()
    if begin == 'Y':
        print('\nLet me remind you of the card values:\n'
              '1 through 10 are face value\n'
              'Jack, Queen, King are 10\n'
              'Ace is either 1 or 11, depending on which is higher without going over 21\n')
        print(Fore.LIGHTBLUE_EX + 'Good luck!' + Style.RESET_ALL)
        player_chips = Chips()
        game_on = True
        pass
    else:
        game_on = False
        print(Fore.LIGHTRED_EX + 'Goodbye!' + Style.RESET_ALL)
        exit(99)


    while game_on == True:
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        take_bet(player_chips)
        print('Your bank: ' + Fore.LIGHTGREEN_EX, player_chips.total, Style.RESET_ALL)
        print('Your bet: ',Fore.RED, player_chips.bet,Style.RESET_ALL)

        show_some(player_hand,dealer_hand)

        playing = True
        while playing == True:
            x = input('\nWould you like to Hit or Stand? Enter H or S: ').upper()
            if x == 'H':
                hit(deck,player_hand)
            elif x == 'S':
                print("Stay. Dealer's turn.")
                playing = False
            else:
                print('Enter H or S.')
            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push()

        print('Your bank: ' + Fore.LIGHTGREEN_EX, player_chips.total, Style.RESET_ALL)

        new_game = input('\nWould you like to keep playing? Y or N ').upper()
        if new_game == 'Y':
            playing = True
            continue
        else:
            print('\nGoodbye')
            playing = False
            break

if __name__ == '__main__':
    play_game()