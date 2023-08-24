'''
Created on Jan 18, 2023

@author: cadiganperriello


I have the .index() and .clear() list method in this class. 


'''
from Hand import Hand
from Card import Card
from Deck import Deck
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def make_row(img1, img2, img3, img4, img5):
    row = Image.new('RGB', (img1.width * 6, img1.height))
    row.paste(img1, (0, 0))
    row.paste(img2, (img1.width, 0))
    row.paste(img3, (img1.width + img2.width, 0))
    row.paste(img4, (img1.width + img2.width + img3.width, 0))
    row.paste(img5, (img1.width + img2.width + img3.width + img4.width, 0))
    return row
    
   
def make_column(row1, row2, row3, row4): 
    column = Image.new('RGB', (row1.width, row1.height * 4 ))
    column.paste(row1, (0, 0))
    column.paste(row2, (0, row1.height))
    column.paste(row3, (0, row1.height + row2.height))
    column.paste(row4, (0, row1.height + row2.height + row3.height))
    return column
    
    
    

    

# text(x, y), "text content", font, fill=(r,g,b))

if __name__ == '__main__':
    poker_game = (Hand(), Hand(), Hand(), Hand())
    deck1 = Deck()
    deck1.shuffle()
    for i in range(20):
        poker_game[i%4].add_card(deck1.deal_card())
        
   
        
    row1 = make_row(Image.open("cards/" + poker_game[0].get_hand()[0].image_file_name()),
                    Image.open("cards/" + poker_game[0].get_hand()[1].image_file_name()),
                    Image.open("cards/" + poker_game[0].get_hand()[2].image_file_name()),
                    Image.open("cards/" + poker_game[0].get_hand()[3].image_file_name()),
                    Image.open("cards/" + poker_game[0].get_hand()[4].image_file_name()))
    
    row2 = make_row(Image.open("cards/" + poker_game[1].get_hand()[0].image_file_name()),
                    Image.open("cards/" + poker_game[1].get_hand()[1].image_file_name()),
                    Image.open("cards/" + poker_game[1].get_hand()[2].image_file_name()),
                    Image.open("cards/" + poker_game[1].get_hand()[3].image_file_name()),
                    Image.open("cards/" + poker_game[1].get_hand()[4].image_file_name()))
    
    row3 = make_row(Image.open("cards/" + poker_game[2].get_hand()[0].image_file_name()),
                    Image.open("cards/" + poker_game[2].get_hand()[1].image_file_name()),
                    Image.open("cards/" + poker_game[2].get_hand()[2].image_file_name()),
                    Image.open("cards/" + poker_game[2].get_hand()[3].image_file_name()),
                    Image.open("cards/" + poker_game[2].get_hand()[4].image_file_name()))
        
    row4 = make_row(Image.open("cards/" + poker_game[3].get_hand()[0].image_file_name()),
                    Image.open("cards/" + poker_game[3].get_hand()[1].image_file_name()),
                    Image.open("cards/" + poker_game[3].get_hand()[2].image_file_name()),
                    Image.open("cards/" + poker_game[3].get_hand()[3].image_file_name()),
                    Image.open("cards/" + poker_game[3].get_hand()[4].image_file_name()))
    

    

    winner = []
    for x in range(len(poker_game)):
        is_undefeated = True
        for i in range(len(poker_game)):
            if x != i:
                if poker_game[x].compare(poker_game[i]) == -1:
                    is_undefeated = False
        winner.append(is_undefeated)

    
    
    
    
    column = make_column(row1, row2, row3, row4)
    
    I1 = ImageDraw.Draw(column)
    myFont = ImageFont.truetype('Times New Roman', 15)
    winnerFont = ImageFont.truetype('Times New Roman', 25)
    
    
    I1.text(((column.width-80), 70), poker_game[0].get_hand_type(), font = myFont, fill = (255, 255, 255))
    I1.text(((column.width-80), 215), poker_game[1].get_hand_type(), font = myFont, fill = (255, 255, 255))
    I1.text(((column.width-80), 360), poker_game[2].get_hand_type(), font = myFont, fill = (255, 255, 255))
    I1.text(((column.width-80), 505), poker_game[3].get_hand_type(), font = myFont, fill = (255, 255, 255))
    
    
    winner_position = [70 + 10, 215 +10, 360 + 10, 505 + 10]
    winner_index = winner.index(True)
    for x in winner:
        if x is True:
            I1.text(((column.width - 85), winner_position[winner_index]), "Winner!", font = winnerFont, fill = (255, 255, 255))
            
    
    column.show()
    
    
    # print("My Hand:")
    # poker_game[0].print_hand()
    # print(poker_game[0].get_hand_type())
    # print("\n")
    # print("Other Hand:")
    # poker_game[1].print_hand()
    # print(poker_game[1].get_hand_type())
    # print("\n")
    # print(poker_game[0].compare(poker_game[1]))


    for x in range(len(poker_game)):
        poker_game[x].print_hand()
        print("\n")
    
    print(winner)
    winner.clear()
    































