# Program Blackjack
# Description: 
#   Blackjack Game
# Author: Jacob Doney
# Date: 17 July 2021
# Revised: 
#   24 July 2021

# import library modules here
import random
import tkinter as tk
import tkinter.font
from tkinter import ttk

# Card Class Joins a suit value with a face value.  
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    # End __init__ Function

    def __repr__(self):
        return "".join((self.value, self.suit))

    # End __repr__ Function

# End Class Card

class Application(tk.Frame):

    def __init__(self,master):
        super(Application,self).__init__(master)
        
        # Declare Variales
        self.count = int()
        self.win_count = int()
        self.canvas_left = int()
        self.canvas_right = int()
        self.text_position = int()
        self.stand_clicked = bool()
        
        # Initialize variables
        self.count = 0
        self.win_count = 0
        self.lose_count = 0
        self.canvas_left = 180
        self.canvas_right = 310
        self.text_position = 245
        self.stand_clicked = False

        # Declaring Constants
        self.MY_FONT = tkinter.font.Font(family='Helvetica', size=25, weight='bold')
        self.LBL_FONT = tkinter.font.Font(family='Helvetica', size=15)

        self.play()
        self.create_window()
        self.create_buttons()

    # Function hand_value()
    # Description:
    #   Creates the deck and the initial hand
    # Calls:
    #   none
    # Parameters:
    #   self
    # Returns:
    #   none
    
    def play(self):

        # Declare Local Variable types (NOT parameters)
        self.cards = list()
        self.hand = list()
        self.dealers_hand = list()
        self.deck_suit = list()
        self.deck_value = list()
        

        # Passes the suit symbols and the the face values to Card class where they are joined together and then added to a list called cards. 
        self.cards = [Card(self.deck_suit, self.deck_value) for self.deck_suit in ["♦", "♥", "♠", "♣"] for self.deck_value in [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        # shuffles the deck list
        random.shuffle(self.cards)

        # initializes list for users hand and the dealers hand
        self.hand = []
        self.dealers_hand = []

        # appends(adds) two  cards to the hand list and the dealers_hand
        for count in range(2):
            self.hand.append(deal(self.cards))
            self.dealers_hand.append(deal(self.cards))

        # End For

    #} End Function play()

    # Function create_window()
    # Description:
    #   Creates the main gui canvass and window
    # Calls:
    #   none
    # Parameters:
    #   self
    # Returns:
    #   none

    def create_window(self):
        
        # Declare Local Variable types (NOT parameters)

        self.top_canvas_right = int()
        self.top_canvas_left = int()
        self.top_text_position = int()
        self.dealers_count = int()

        # Initializing values
        self.top_canvas_right = 310
        self.top_canvas_left = 180
        self.top_text_position = 245
        self.top_text_y_position = 165
        self.top_canvas_top = 80
        self.top_canvas_bottom = 250
        self.dealers_count = 0
        self.bottom_canvas_bottom = 500
        self.bottom_canvas_top = 330
        self.bottom_text_y_position = 415

         # creates the main canvas in the GUI. The greenback ground. This also determines the window size. 
        self.canvas_main = tk.Canvas(self, width=1080, height=600, bg='green')
        # When using tkinter you must pack all objects for it to show up (Text and drawings do not need to be pack) 
        self.canvas_main.pack()

        # Card style and position.
        dealer_card_one = self.canvas_main.create_rectangle(30, 80, 160, 250, fill='white', width=3)
        dealer_card_two = self.canvas_main.create_rectangle(310, 80, 180, 250, fill='white', width=3)
        hand_card_one = self.canvas_main.create_rectangle(30, 330, 160, 500, fill='white', width=3)
        hand_card_two = self.canvas_main.create_rectangle(310, 330, 180, 500, fill='white', width=3)

        # Text position and style
        dealer_tittle = self.canvas_main.create_text( 160, 50,text='Dealer\'s Hand', fill='white', font=self.MY_FONT)
        your_hand_tittle = self.canvas_main.create_text( 160, 300, text='Your Hand', fill='white', font=self.MY_FONT)
        dealer_card_one_text = self.canvas_main.create_text(90, 165, text=self.dealers_hand[1], fill=color_selector(self.dealers_hand[1]), font=self.MY_FONT)
        dealer_card_two_text = self.canvas_main.create_text(245, 165, text='Hidden', fill='black', font=self.MY_FONT)
        hand_card_one_text = self.canvas_main.create_text(90, 415, text=self.hand[0], fill=color_selector(self.hand[0]), font=self.MY_FONT)
        hand_card_two_text = self.canvas_main.create_text(245, 415, text=self.hand[1], fill=color_selector(self.hand[1]), font=self.MY_FONT)

        # Gets cards value
        self.card_value = hand_value(self.hand)

        # Labels that tell the user their hand value and if the win, lose, or tie. 
        self.lbl = tk.Label(self, text =f'Hand Value {self.card_value}', font=self.LBL_FONT)
        self.lbl.pack(side='bottom')
        self.win_lbl = tk.Label(self, font=self.LBL_FONT)
        self.win_lbl.pack(side='bottom')
        self.win_lbl.config(text =f'Rounds Won: {self.win_count}\nRounds Lost: {self.lose_count}')
        self.chat = tk.Label(self, text='BLACKJACK', font=self.MY_FONT)
        self.chat.pack(side='bottom')

        # Natural 21. If user gets 21 on initial deal. Want to pass this to def as it is repeted later on but can't get it to work with the gui
        # Gets card value
        self.card_value = hand_value(self.hand)

        if self.card_value == 21:
            # Gets Dealers value
            self.dealers_value = hand_value(self.dealers_hand)
            
            dealer_card_two = self.canvas_main.create_rectangle(310, self.top_canvas_top, 180, self.top_canvas_bottom, fill='white', width=3)
            dealer_card_two_text = self.canvas_main.create_text(245, self.top_text_y_position, text=self.dealers_hand[0], fill=color_selector(self.dealers_hand[0]), font=self.MY_FONT)
            self.lbl.config(text=f'Hand Value {self.card_value}! : Dealer\'s Value {self.dealers_value}')

            while self.dealers_value < 17:
                self.top_canvas_right += 150
                self.top_canvas_left += 150
                self.top_text_position += 150
                self.dealers_count += 1
                self.dealers_hand.append(deal(self.cards))
                self.dealers_value = hand_value(self.dealers_hand)
                self.lbl.config(text=f'Hand Value {self.card_value}! : Dealer\'s Value {self.dealers_value}', font=self.LBL_FONT)
                self.canvas_main.create_rectangle(self.top_canvas_right, self.top_canvas_top, self.top_canvas_left, self.top_canvas_bottom, fill='white', width=3)
                self.canvas_main.create_text(self.top_text_position, self.top_text_y_position, text=self.dealers_hand[1 + self.dealers_count], fill=color_selector(self.dealers_hand[1 + self.dealers_count]), font=self.MY_FONT)
            # End While

            # Displays who won
            if self.card_value != self.dealers_value and self.card_value == 21:
                self.chat.config(text='NATURAL 21! YOU WIN!')
                self.win_count += 1
            else:
                self.chat.config(text='TIE')
            # End if
        
        else:
            pass

        
    #} End Function create_window

    # Function create_buttons()
    # Description:
    #   Creates button widgets
    # Calls:
    #   none
    # Parameters:
    #   self
    # Returns:
    #   none

    def create_buttons(self):

        # Style
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font=self.LBL_FONT, background='black', foreground='white')
        self.style.map('TButton', background=[('active', '#ff0000')])
        
        # Hit Button
        self.hit_button = ttk.Button(self, text='Hit', command=self.hit_click)
        self.hit_button.pack(side='left', padx=(250,0), anchor='center')

        # Stand Button
        self.stand_button = ttk.Button(self, text='Stand', command=self.click_stand)
        self.stand_button.pack(side='left', anchor='center')

        # New deal Button
        self.deal_button = ttk.Button(self, text='Deal Again', command=self.click_new_deal)
        self.deal_button.pack( side='left', anchor='center')


        # Quit Button
        self.quit_button = ttk.Button(self, text='Quit', command=root.destroy)
        self.quit_button.pack( side='left', anchor='center')

    #} End create_buttons function

    def hit_click(self):
        
        #local variables
        self.top_canvas_right = int()
        self.top_canvas_left = int()
        self.top_text_position = int()
        self.dealers_count = int()
        self.card_value = int()
        self.dealers_value = int()

        #Initializing variables
        self.top_canvas_right = 310
        self.top_canvas_left = 180
        self.top_text_position = 245
        self.dealers_count = 0
        
        if self.stand_clicked == False:
            self.card_value = hand_value(self.hand)

            # user has not busted
            if self.card_value < 21:
                self.count += 1
                self.canvas_right += 150
                self.canvas_left += 150
                self.text_position += 150
                self.hand.append(deal(self.cards))
                self.card_value = hand_value(self.hand)
                self.lbl.config(text=f'Hand Value {self.card_value}')
                # Shows your new card
                self.canvas_main.create_rectangle(self.canvas_right, self.bottom_canvas_top, self.canvas_left, self.bottom_canvas_bottom, fill='white', width=3)
                self.canvas_main.create_text(self.text_position, self.bottom_text_y_position, text=self.hand[1 + self.count], fill=color_selector(self.hand[1 + self.count]), font=self.MY_FONT)
                self.card_value = hand_value(self.hand)

                # user has busted
                if self.card_value >= 21:
                    # Shows dealers hidden card
                    self.canvas_main.create_rectangle(310, 80, 180, 250, fill='white', width=3)
                    self.canvas_main.create_text(245, 165, text=self.dealers_hand[0], fill=color_selector(self.dealers_hand[0]), font=self.MY_FONT)
                    self.dealers_value = hand_value(self.dealers_hand)
                    self.lbl.config(text=f'Hand Value {self.card_value} : Dealer\'s Value {self.dealers_value}')
                    while self.dealers_value < 17 and self.card_value < 22:
                        self.top_canvas_right += 150
                        self.top_canvas_left += 150
                        self.top_text_position += 150
                        self.dealers_count += 1
                        self.dealers_hand.append(deal(self.cards))
                        self.dealers_value = hand_value(self.dealers_hand)
                        # Displays new dealer card
                        self.canvas_main.create_rectangle(self.top_canvas_right, self.top_canvas_top, self.top_canvas_left, self.top_canvas_bottom, fill='white', width=3)
                        self.canvas_main.create_text(self.top_text_position, self.top_text_y_position, text=self.dealers_hand[1 + self.dealers_count], fill=color_selector(self.dealers_hand[1 + self.dealers_count]), font=self.MY_FONT)
                        self.lbl.config(text=f'Hand Value {self.card_value} : Dealer\'s Value {self.dealers_value}')

                    # End While
                    
                    # Displays who won
                    if self.dealers_value > self.card_value and self.card_value < 22 and self.dealers_value < 22:
                        self.chat.config(text='YOU LOSE!')
                        self.lose_count += 1
                    elif self.card_value == 21 and self.card_value != self.dealers_value:
                        self.chat.config(text='YOU GOT BLACKJACK! YOU WIN!')
                        self.win_count += 1
                    elif self.card_value > self.dealers_value and self.card_value < 22 and self.dealers_value < 22:
                        self.chat.config(text='YOU WIN!')
                        self.win_count += 1
                    elif self.card_value > 21:
                        self.chat.config(text='BUSTED! YOU LOSE!')
                        self.lose_count += 1
                    elif self.dealers_value > 21:
                        self.chat.config(text='DEALER BUSTED! YOU WIN!')
                        self.win_count += 1
                    else:
                        self.chat.config(text='TIE')
                    # End if

                else:
                    pass

                # End if

            # User busted
            else:
                pass

            #End if 
        else:
            pass
        # End if
        
    #} Function hit_click()

    # Function click_stand()
    # Description:
    #   Shows dealers hand and ends game play. 
    # Calls:
    #   none
    # Parameters:
    #   self
    # Returns:
    #   none

    def click_stand(self):
        #local variables
        self.top_canvas_right = int()
        self.top_canvas_left = int()
        self.top_text_position = int()
        self.dealers_count = int()
        self.card_value = int()
        self.dealers_value = int()

        # intialize variables
        self.top_canvas_right = 310
        self.top_canvas_left = 180
        self.top_text_position = 245
        self.dealers_count = 0

        # Shows dealers hidden card
        self.canvas_main.create_rectangle(310, self.top_canvas_top, 180, self.top_canvas_bottom, fill='white', width=3)
        self.canvas_main.create_text(245, self.top_text_y_position, text=self.dealers_hand[0], fill=color_selector(self.dealers_hand[0]), font=self.MY_FONT)
        self.card_value = hand_value(self.hand)
        self.dealers_value = hand_value(self.dealers_hand)
        self.lbl.config(text=f'Hand Value {self.card_value} : Dealer\'s Value {self.dealers_value}')

        if self.stand_clicked == False:
            # Dealer keeps hitting if under 17 and user has not busted
            while self.dealers_value < 17 and self.card_value < 22:
                self.top_canvas_right += 150
                self.top_canvas_left += 150
                self.top_text_position += 150
                self.dealers_count += 1
                self.dealers_hand.append(deal(self.cards))
                self.dealers_value = hand_value(self.dealers_hand)
                self.lbl.config(text=f'Hand Value {self.card_value} : Dealer\'s Value {self.dealers_value}')
                # Deals a new card for dealer
                self.canvas_main.create_rectangle(self.top_canvas_right, self.top_canvas_top, self.top_canvas_left, self.top_canvas_bottom, fill='white', width=3)
                self.canvas_main.create_text(self.top_text_position, self.top_text_y_position, text=self.dealers_hand[1 + self.dealers_count], fill=color_selector(self.dealers_hand[1 + self.dealers_count]), font=self.MY_FONT)

            # End While

            # Displays winner
            if self.dealers_value > self.card_value and self.card_value <= 21 and self.dealers_value <= 21:
                self.chat.config(text='YOU LOSE!')
                self.lose_count += 1
            elif self.card_value == 21 and self.card_value != self.dealers_value:
                self.chat.config(text='BLACKJACK! YOU WIN!')
                self.win_count += 1
            elif self.card_value > self.dealers_value and self.card_value <= 21 and self.dealers_value <= 21:
                self.chat.config(text='YOU WIN!')
                self.win_count += 1
            elif self.card_value > 21:
                self.chat.config(text='BUSTED! YOU LOSE!')
                self.lose_count += 1
            elif self.dealers_value > 21:
                self.chat.config(text='DEALER BUSTED! YOU WIN!')
                self.win_count += 1
            else:
                self.chat.config(text='TIE')

            # End if 
            
        #End if

        # sets stand click to true
        self.stand_clicked = True
        
    #} Function click_stand()

    # Function new deal()
    # Description:
    #   Resets game when new deal button is clicked
    # Calls:
    #   none
    # Parameters:
    #   self
    # Returns:
    #   none
    
    def click_new_deal(self):

        # Destroying card and labels
        self.canvas_main.destroy()
        self.hit_button.destroy()
        self.stand_button.destroy()
        self.deal_button.destroy()
        self.lbl.destroy()
        self.win_lbl.destroy()
        self.chat.destroy()
        self.quit_button.destroy()

        # Resets variabless
        self.count = 0
        self.canvas_left = 180
        self.canvas_right = 310
        self.text_position = 245
        self.stand_clicked = False

        #Reruns play()
        self.play()
        self.create_window()
        self.create_buttons()
        
    #} Function click_new_deal


# End Class Application



# Function deal()
# Description:
#   adds cards from cards list to either hand or dealer_hands
# Calls:
#   none
# Parameters:
#   deck
# Returns:
#   deck.pop(0)

def deal(deck):
    if len(deck) > 1:
        # Return values
        return deck.pop(0)
    
#} function deal()

# Function hand_value()
# Description:
#   determins cards value
# Calls:
#   none
# Parameters:
#   cards_in_hand
# Returns:
#   value

def hand_value(cards_in_hand):
    # local variables
    has_ace = bool()
    cards = int()
    value = int()

    # Initialize variables
    value = 0
    has_ace = False

    # Loops all cards in list
    for cards in cards_in_hand:
        # card is a numeric adds numeric value to value
        if cards.value.isnumeric():
            value += int(cards.value)
            
        else:
            # Ace set to 11
            if cards.value == "A":
                    has_ace = True
                    value += 11
            # Face cards set to 10
            else:
                value += 10

    # Sets ace to 1 if value is over 21
    if ( has_ace == True ) and ( value > 21 ):
        value -=10

    # Return values  
    return value
                    
    
#} function hand_value()

# Function color_selector()
# Description:
#   sets a color to the card. 
# Calls:
#   none
# Parameters:
#   cards
# Returns:
#   color

def color_selector(cards):
    #local variables
    color = str()

    if cards.suit == "♦" or cards.suit == "♥":
        color = 'red'
    else:
        color = 'black'

    # Return values
    return color
    
#} function color_selector()


if __name__ == '__main__':

# Creates the main window
    root = tk.Tk()
    root.title('Black Jack')
    app = Application(root).pack()
    root.mainloop()
