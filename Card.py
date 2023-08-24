'''
Created on Jan 18, 2023

@author: cadiganperriello
'''

"""
The Card class models a single card in a deck. The card class has an attribute of card_names which is a tuple that holds the
common names for all of the card values, such as Queen instead of 12. All cards have the attribute value and suit.
This class has a constructor with value and suit parameters and two getters for those. It them has a method to return 
the name for the card value and uses the class attribute tuple to do this. The last method returns an image file name 
of the value and suit as a file name to be used later to access pictures. 

"""



class Card:
    card_names = ("Duece", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def get_name(self):
        return Card.card_names[self.value - 2] + " of " + self.suit
    
    def image_file_name(self):
        if self.value <= 10:
            return f"{self.value}_of_{self.suit}.png"
        elif self.value > 10:
            return f"{Card.card_names[self.value - 2].lower()}_of_{self.suit}.png"
    
    