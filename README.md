# Poker
## Hand Class:

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

## Deck Class:

The Deck class models a deck of 52 playing cards. The Deck class has one attribute, a last that will hold all 52 cards. The only major algorithms in the class is the for look that creates the deck of cards by looking through the amount of suits and then a nested for loop of all of the possible values in order to create all values in each suit with no repeats and then adds then to the deck list. This allows a deck to be created by calling the class. The shuffle method loops through 500 times, (does not have to be 500, just a large number) and picks a random number from 0 to 52 and then adds that number card to the end of deck and deletes it from its stop, randomizing the deck. I met the  "for x in thisList" loop requirement in the constructor with "for x in suits" loop. I met the "for i in range()" requirement also in the constructor with "for i in range(2, 15):" loop. I also used list comprehension in the print deck method with "[print(x.get_name()) for x in Deck.deck]" to print the common names for all the cards. I have also used the  list methods .append(), and .pop(). 

## Card Class:
The Card class models a single card in a deck. The card class has an attribute of card_names which is a tuple that holds the
common names for all of the card values, such as Queen instead of 12. All cards have the attribute value and suit.
This class has a constructor with value and suit parameters and two getters for those. It them has a method to return 
the name for the card value and uses the class attribute tuple to do this. The last method returns an image file name 
of the value and suit as a file name to be used later to access pictures.


