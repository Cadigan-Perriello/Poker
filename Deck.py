'''
Created on Jan 18, 2023

@author: cadiganperriello
'''
from Card import Card
import random 
from Hand import Hand

"""
The Deck class models a deck of 52 playing cards. The Deck class has one attribute, a last that will hold all 52 cards. The only major
algorithms in the class is the for look that creates the deck of cards by looking through the amount of suits and then a nested
for loop of all of the possible values in order to create all values in each suit with no repeats and then adds then to the deck list.
This allows a deck to be created by calling the class. The shuffle method loops through 500 times, (does not have to be 500, just a
large number) and picks a random number from 0 to 52 and then adds that number card to the end of deck and deletes it from its stop,
randomizing the deck. I met the  "for x in thisList" loop requirement in the constructor with "for x in suits" loop. I met the 
"for i in range()" requirement also in the constructor with "for i in range(2, 15):" loop. I also used list comprehension in the print
deck method with "[print(x.get_name()) for x in Deck.deck]" to print the common names for all the cards. I have also used the  list
methods .append(), and .pop(). 


"""

class Deck:
   # deck = []
    suits = ("hearts", "diamonds", "clubs", "spades")
    def __init__(self):  
        self.deck = []
        for x in Deck.suits:
            for i in range(2, 15):
                card = Card(i, x)
                self.deck.append(card)
                
    def get_deck(self):
        return self.deck
    
    def print_deck(self):
        [print(x.get_name()) for x in self.deck]
            
    def shuffle(self):
        for i in range(500):
            x = int(random.uniform(0, 52))
            self.deck.append(self.deck.pop(x))
    
    def deal_card(self):
        return self.deck.pop(0)





















