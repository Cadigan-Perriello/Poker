'''
Created on Jan 18, 2023

@author: cadiganperriello
'''
import Card

"""
The Hand class models a hand of 5 random cards from the deck. The Hand class has one attribute, a list that will receive 
cards as they are dealt, modeling a hand of cards. Using method decomposition, I divided the rank algorithm into different
 methods for all of the possible types of hand (ex. one-pair, two-pair), also utilizing my methods that determine if a 
hand is a straight or a flush. Each method returns a boolean as to whether a hand is that type and then in my rank method 
i use if and elif statements to return the rank (0-9) of the hand. The other major algorithm is the compare algorithm. I 
used method decomposition to divide the code into three methods: compare; this method simply returns a winner if one hand 
has a higher hand that the other, compare_high_card; this method uses a for loop running through each card in the hands 
and returns which card has a higher card value with 1, -1, and 0 integers, and finally same_rank; this method is used to 
determine the winner if two hands have the same hand. It uses an if statement for every rank and goes through each rank to
determine the winner. Two Royal flushes is a true tie, but other than that each if statements uses either the high card 
method to determine the winner or loops through the find the value of the pairs in order to determine which hand holds a 
higher pair/s and therefore wins. It also utilizes the sorting of the hand by knowing that pairs and three of a kind will 
be next to each other. I have also used the list methods .sort(), .reverse(), .append(), and .insert(). 

"""



class Hand:
    def __init__(self):
        self.my_cards = []
    def get_hand(self):
        return self.my_cards
    def print_hand(self):
        [print(x.get_name()) for x in self.my_cards]
    def add_card(self, new_card):
        self.my_cards.insert(len(self.my_cards)+1, new_card)
        self.my_cards.sort(key = get_key)
        self.my_cards.reverse()
        
    def is_straight(self):
        for i in range(len(self.my_cards) - 1 ):
            if not self.my_cards[i].get_value() - self.my_cards[i+1].get_value() == 1:
                return False 
        return True
    def is_flush(self):
        for i in range(len(self.my_cards) - 1 ):
            if not self.my_cards[i].get_suit() == self.my_cards[i+1].get_suit():
                return False
        return True

    
    def is_royal_flush(self):
        if self.is_flush() and self.is_straight() and self.my_cards.get_value[0] == 14:
            return True
        else:
            return False
        
    def is_straight_flush(self):
        if self.is_straight() and self.is_flush:
            return True  
        else:
            return False
        
    def is_4_of_a_kind(self):
        if self.my_cards[0].get_value() == self.my_cards[3].get_value():
            return True
        elif self.my_cards[1].get_value() == self.my_cards[4].get_value():
            return True
        else:
            return False
    
    def is_full_house(self):
        if self.my_cards[0].get_value() == self.my_cards[1].get_value() and self.my_cards[2].get_value() == self.my_cards[4].get_value():
            return True
        elif self.my_cards[0].get_value() == self.my_cards[2].get_value() and self.my_cards[3].get_value() == self.my_cards[4].get_value():
            return True
        else:
            return False
    def is_three_of_a_kind(self):
        if self.my_cards[0].get_value() == self.my_cards[2].get_value():
            return True
        elif self.my_cards[2].get_value() == self.my_cards[4].get_value():
            return True
        else:
            return False
    
    def is_two_pair(self):
        if self.my_cards[0].get_value() == self.my_cards[1].get_value() and self.my_cards[2].get_value() == self.my_cards[3].get_value():
            return True
        elif self.my_cards[0].get_value() == self.my_cards[1].get_value() and self.my_cards[3].get_value() == self.my_cards[4].get_value():
            return True
        elif self.my_cards[1].get_value() == self.my_cards[2].get_value() and self.my_cards[3].get_value() == self.my_cards[4].get_value():
            return True
        else:
            return False
    
    def is_one_pair(self):
        if self.my_cards[0].get_value() == self.my_cards[1].get_value():
            return True
        elif self.my_cards[1].get_value() == self.my_cards[2].get_value():
            return True
        elif self.my_cards[2].get_value() == self.my_cards[3].get_value():
            return True
        elif self.my_cards[3].get_value() == self.my_cards[4].get_value():
            return True
        else:
            return False
    
    def rank(self):
        if self.is_royal_flush():
            return 9
        elif self.is_straight_flush():
            return 8 
        elif self.is_4_of_a_kind():
            return 7
        elif self.is_full_house():
            return 6
        elif self.is_flush():
            return 5
        elif self.is_straight():
            return 4
        elif self.is_three_of_a_kind():
            return 3
        elif self.is_two_pair():
            return 2
        elif self.is_one_pair():
            return 1
        else:
            return 0 
    
    def get_hand_type(self):
        if self.rank() == 9:
            return "Royal Flush"
        if self.rank() == 8:
            return "Straight Flush"
        if self.rank() == 7:
            return "Four of a Kind"
        if self.rank() == 6:
            return "Full House"
        if self.rank() == 5:
            return "Flush"
        if self.rank() == 4:
            return "Straight"
        if self.rank() == 3:
            return "Three of a Kind"
        if self.rank() == 2:
            return "Two Pair"
        if self.rank() == 1:
            return "One Pair"
        if self.rank() == 0:
            return "High Card"
    def compare(self, other_hand):
        if other_hand.rank() > self.rank():
            return -1
        elif self.rank() > other_hand.rank():
            return 1
        elif self.rank() == other_hand.rank():
            return self.same_rank(other_hand)
        
    def compare_high_card(self, other_hand):
        for i in range(len(self.my_cards)):
            if self.my_cards[i].get_value() > other_hand.get_hand()[i].get_value():
                return 1 
            elif self.my_cards[i].get_value() < other_hand.get_hand()[i].get_value():
                return -1
        else:
            return 0
        
        
    def same_rank(self, other_hand):
        high_card = 0
        if other_hand.rank() == 9:
            return 0
        if other_hand.rank() == 8:
            return self.compare_high_card(other_hand)
        if other_hand.rank() == 7:
            if other_hand.get_hand()[2].get_value() >   self.my_cards[2].get_value():
                return -1
            else:
                return 1
        if other_hand.rank() == 6:
            if other_hand.get_hand()[2].get_value() >  self.my_cards[2].get_value():
                return -1
            else:
                return 1 
        if other_hand.rank() == 5:
            return self.compare_high_card(other_hand)
        if other_hand.rank() == 4:
            return self.compare_high_card(other_hand)
        if other_hand.rank() == 3:
            if other_hand.get_hand()[2].get_value() >  self.my_cards[2].get_value():
                return -1
            else:
                return 1 
        if other_hand.rank() == 2:

            if self.my_cards[1].get_value() > other_hand.get_hand()[1].get_value():
                return 1
            elif self.my_cards[1].get_value() < other_hand.get_hand()[1].get_value():
                return -1
            elif self.my_cards[3].get_value() > other_hand.get_hand()[3].get_value():
                    return 1
            elif self.my_cards[3].get_value() < other_hand.get_hand()[3].get_value():
                    return -1
            else:
                return self.compare_high_card(other_hand)
        if other_hand.rank() == 1:
            if self.my_cards[0].get_value() == self.my_cards[1].get_value(): 
               my_pair = self.my_cards[0].get_value()
            elif self.my_cards[1].get_value() == self.my_cards[2].get_value(): 
               my_pair = self.my_cards[1].get_value()
            elif self.my_cards[2].get_value() == self.my_cards[3].get_value(): 
               my_pair = self.my_cards[2].get_value()
            elif self.my_cards[3].get_value() == self.my_cards[4].get_value(): 
               my_pair = self.my_cards[3].get_value()
               
            if other_hand.get_hand()[0].get_value() == other_hand.get_hand()[1].get_value():
                other_hand_pair = other_hand.get_hand()[0].get_value()
            elif other_hand.get_hand()[1].get_value() == other_hand.get_hand()[2].get_value():
                other_hand_pair = other_hand.get_hand()[1].get_value()
            elif other_hand.get_hand()[2].get_value() == other_hand.get_hand()[3].get_value():
                other_hand_pair = other_hand.get_hand()[2].get_value()
            elif other_hand.get_hand()[3].get_value() == other_hand.get_hand()[4].get_value():
                other_hand_pair = other_hand.get_hand()[3].get_value()
                
            if other_hand_pair > my_pair:
                return -1
            elif my_pair > other_hand_pair:
                return 1
            else:
                return self.compare_high_card(other_hand)
        if other_hand.rank() == 0:
            return self.compare_high_card(other_hand)
           


def get_key(obj):
    return obj.value
























