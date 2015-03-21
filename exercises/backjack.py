# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        string = 'Hand contains'
        for card in self.cards:
            string += ' ' + card.get_suit() + card.get_rank()
        return string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        has_a = False
        for card in self.cards:
            if card.get_rank() == 'A':
                has_a = True
            value += VALUES[card.get_rank()]
        if has_a and (value + 10 <= 21):
            value += 10
        return value
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas,[pos[0] + (i * CARD_SIZE[0]), pos[1]])
            i += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        string = 'Deck: '
        for card in self.cards:
            string += ' ' + card.get_suit() + card.get_rank()
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, game_hand1, game_hand2, score
    if in_play:
        score -= 1
        outcome = 'You Loose! Click on deal again!'
        in_play = False
    else:    
        game_deck = Deck()
        game_deck.shuffle()
        
        game_hand1 = Hand()
        game_hand2 = Hand()
        
        game_hand1.add_card(game_deck.deal_card())
        game_hand1.add_card(game_deck.deal_card())
        
        game_hand2.add_card(game_deck.deal_card())
        game_hand2.add_card(game_deck.deal_card())
        
        in_play = True
        outcome = 'Hit or Stand?'

def hit():
    global game_hand1, game_deck, outcome, score, in_play
    if in_play and game_hand1.get_value() <= 21:
        game_hand1.add_card(game_deck.deal_card())
        if game_hand1.get_value() > 21:
            outcome = "You have busted"
            in_play = False
            score-= 1
        else:
            outcome = "Hit or Stand?"
       
def stand():
    global in_play, game_hand1, game_hand2, game_deck, outcome, score
    if in_play:
        while game_hand2.get_value() < 17:
            game_hand2.add_card(game_deck.deal_card())
        if game_hand2.get_value() > 21:
            outcome = "Dealer busted!"
            in_play = False
            score += 1
        else:
            if game_hand2.get_value() >= game_hand1.get_value():
                outcome = "Dealer Wins!"
                in_play = False
                score -= 1
            else:
                outcome = "You Win!"
                in_play = False
                score += 1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome, [230, 150], 20, 'White')
    canvas.draw_text("score: " + str(score), [430, 100], 20, 'White')
    canvas.draw_text("BlackJack", [200, 80], 40, 'White')
    game_hand1.draw(canvas,[100,400])
    game_hand2.draw(canvas,[100,200])
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [100 + CARD_CENTER[0],200 + CARD_CENTER[1]],CARD_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric