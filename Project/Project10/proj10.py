###############################################################################
#  CSE 231 Project #10
#
#  ALGORITHM
#  import Card and Deck classes from cards.py 
#  declare constants with given value
#  define initialize() function that starts the Klondike game by 
#  initializing all the variables/data strcutures. Tableu is a list of 7 
#  nested lists, foundation is a list of 4 lists, waste is a list, and stock 
#  is an instance of the class Deck. The function also turns all the cards in 
#  the tableu except the last card in each column face down. Stock is shuffled.
# 
#  define display(tableau, stock, foundation, waste) that is used to display 
#  the game setup/board everytime.
#  
#  define stock_to_waste( stock, waste ) that is designed to move/deal a card 
#  from the stock deck to the waste (talon) pile. But before moving card, the 
#  function checks if stock is empty or not. If transfer was successfully done 
#  it returns True, else False.
#
#  define waste_to_tableau( waste, tableau, t_num ) that is designed to 
#  move/deal a card from the waste (talon) pile to the correct one of the 7 
#  columns in the tableu. If transfer was successfully done it returns True, 
#  else False. Here, t_num is the index of column (nested list) in the tableu
#  the card has to be moved to. If tableu is empty then card has to be only a 
#  King.
#
#  define waste_to_foundation( waste, foundation, f_num ) that is designed to 
#  move/deal a card from the waste (talon) pile to the correct one of the 4 
#  piles in the foundation (one is present for each suite). If transfer was 
#  successfully done it returns True, else False. Here, f_num is the index of 
#  pile (nested list) in the foundation the card has to be moved to. If 
#  foundation is empty then card has to be only an Ace.
# 
#  define tableau_to_foundation( tableau, foundation, t_num, f_num ) that is 
#  designed to move/deal a card from the tableau to the correct one of the 4 
#  piles in the foundation (one is present for each suite). If transfer was
#  successfully done it returns True, else False. Here, f_num is the index of 
#  pile (nested list) in the foundation the card has to be moved to and t_num 
#  is the column number in tableau that the card is currently in. If 
#  foundation is empty then card has to be only an Ace.
#
#  define tableau_to_tableau( tableau, t_num1, t_num2 ) that is designed to 
#  move/deal a card from one column in the tableau to another column in the 
#  tableau. If transfer was successfully done it returns True, else False. 
#  Here, t_num1 is the source column number in tableau and t_num2 is the 
#  destination column number. If tableu is empty then card has to be only King.
# 
#  define check_win (stock, waste, foundation, tableau) that checks if the 
#  game's status is a winning situation. That is if all cards are in their 
#  respective foundation piles & stock, waste and tableau are empty.
#
#  define parse_option(in_str) that prompts the user for an option and checks
#  that the input has the form requested in the menu, printing an error 
#  message, if not.
#
#  define main() function
#     call the initialize() function and assign the returned values to four
#     variables tableau, stock, waste, foundation
#     display the MENU of options
#     main while loop
#     call the display(tableau, stock, foundation, waste) function 
#     prompt user to input an option
#     call parse_option(in_str) and assign its returned value to variable
#     parse_result
#     if parse_result equals None, then skip this iteration and go to loop 
#     header (continue statement)
#       
#     else if parse_result[0] equals 'TT'
#        call tableau_to_tableau(tableau, t_num1, t_num2) with the parameters
#        as parse_result[1]-1 & parse_result[2]-1 and assign the return value
#        to variable tt_result
#        if tt_result is True skip this iteration and go to loop header 
#        (continue statement)
#        else, print error message "\nInvalid move!\n"
#        
#     else if parse_result[0] equals 'TF'
#        call tableau_to_foundation(tableau, foundation, t_num, f_num) with the
#        parameters as parse_result[1]-1 & parse_result[2]-1 and assign the
#        return value to variable tf_result
#        if tt_result is True
#           if check_win(stock, waste, foundation, tableau) equals True
#              print the message 'You won!', then call display function again
#              and terminate the loop (break statement)
#           else 
#              skip this iteration and go to loop header (continue statement)
#        else
#           print error message "\nInvalid move!\n"
# 
#     else if parse_result[0] equals 'WF'
#        call waste_to_foundation(waste, foundation, f_num) with the 
#        parameter as parse_result[1]-1 and assign the returned value to 
#        variable wf_result
#        if wf_result is True
#           if check_win(stock, waste, foundation, tableau) equals True
#              print the message 'You won!', then call display function again
#              and terminate the loop (break statement)
#           else 
#              skip this iteration and go to loop header (continue statement)
#        else
#           print error message "\nInvalid move!\n"
#
#     else if parse_result[0] equals 'WT'
#        call waste_to_tableau(waste, tableau, t_num) with the parameter as 
#        parse_result[1]-1 and assign the returned value to variable wt_result 
#        if wt_result is True
#           skip this iteration and go to loop header (continue statement)
#        else
#           print error message "\nInvalid move!\n"
#
#     else if parse_result[0] equals 'SW'
#        call stock_to_waste(stock, waste) and assign the returned value to 
#        variable sw_result 
#        if sw_result is True
#           skip this iteration and go to loop header (continue statement)
#        else
#           print error message "\nInvalid move!\n"
#
#     else if parse_result[0] equals ['R']
#        shuffle the cards in stock using .shuffle()
#        reinitialize() the 4 data structures: tableau, stock, foundation, 
#        waste  by calling the initialize() function
#        display the MENU of options
#        skip this iteration and go to loop header (continue statement)
#
#     else if parse_result[0] equals ['H']
#        display the MENU of options
#
#     else if parse_result[0] equals ['Q']
#        terminate the loop (break statement)
#
#  call main() function
#  end of program
#
###############################################################################

from cards import Card, Deck #Importing the Card, Deck classes from cards.py


MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
    
    
def initialize():
    '''This function is the function that starts the Klondike game by 
    initializing all the variables/data strcutures. Tableu is a list of 7 
    nested lists, foundation is a list of 4 lists, waste is a list, and stock 
    is an instance of the class Deck. 
    The function also turns all the cards in the tableu except the last card in
    each column face down. The stock is shuffled.
    
    Parameters: None
    Returns: list of lists, instance of Class Deck, list of lists, list.
    Displays: Nothing
    '''
    tableu = [[], [], [], [], [], [], []] 
    foundation = [[], [], [], []] #these have to be initially empty
    waste = []
    stock = Deck()        #stock is an instance of Deck class
    
    for i in range(7):     
        #these statements are to deal the cards in an orderly manner into the
        #7 columns of the tableau, all cards being flipped to face down.
        for j in range(i, 7):
            card = stock.deal()
            tableu[j].append(card)
            card.flip_card()
        
    for col in tableu:
        #these statements are to flip only the last card in every column of the
        #tableau down.
        card = col[-1]
        card.flip_card()
        
    waste.append(stock.deal()) #adding the topmost card of stock to the waste
    stock.shuffle()            #shuffling the cards in the stock deck
    
    return tableu, stock, foundation, waste
    
    
    

def display(tableau, stock, foundation, waste):
    """ This function is used to display the game setup/board everytime. """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card),\
                                        str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    
    

def stock_to_waste( stock, waste ):
    '''This function is designed to move/deal a card from the stock deck to the
    waste (talon) pile. But before moving the card, the function checks if 
    stock is empty or not. If transfer was successfully done it returns True, 
    else False.
    Parameters: stock, waste
    Returns: True or False
    Displays: Nothing 
    '''
    stock_size = stock.__len__()  #number of cards in the stock currently
    if stock_size == 0:
        #if stock is empty, then we can't add to the waste, so return False
        return False
    else:
        #If stock is not empty, then deal 1 card from stock, add it to waste,
        #return True
        card = stock.deal()
        waste.append(card)
        return True
    
    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''This function is designed to move/deal a card from the waste (talon) 
    pile to the correct one of the 7 columns in the tableu. If transfer was 
    successfully done it returns True, else False. Here, t_num is the 
    index of column (nested list) in the tableu the card has to be moved to.
    For the card to move into tableu, it should be of opposite colour and 
    one rank lower than topmost card in that tableu column. If tableu is empty
    then card has to be only a King.
    
    Parameters: waste, foundation, t_num
    Returns: True or False
    Displays: Nothing'''
    
    transfer_card = waste[-1]  #this is the card to be transferred.
    rank2 = transfer_card.rank()  #rank of the transfer card
    suit2 = transfer_card.suit()  #suit of the transfer card 
    
    if len(tableau[t_num]) == 0:        
        #destination column of tableau is empty, then only a king (card with
        #rank 13) is possible to be added 
        if transfer_card.rank() == 13:
            #if the card is a king, then pop it and move to particular
            #column in tableau, return True.
            transfer_card = waste.pop()
            tableau[t_num].append(transfer_card)
            return True
        
        else:
            #If not a king, then return False
            return False
    else:
        #destination column of tableau is not empty
        topmost_card = tableau[t_num][-1] #this is the topmost card of column
        rank1 = topmost_card.rank()  #rank of the topmost card
        suit1 = topmost_card.suit()  #suit of the topmost card
        
        if suit1 in (1,4) and suit2 in (2,3):
            # checking if the transfer and topmost cards are of opposite suits
            if rank2 == (rank1-1):
                #check if rank of transfer card is one greater than rank of 
                #topmost card, then pop it, add it to tableau column, return
                #True
                transfer_card = waste.pop()
                tableau[t_num].append(transfer_card)
                return True
        
            else:
                #if there is a mismatch of rank, return False
                return False
            
        elif suit1 in (2,3) and suit2 in (1,4):
            # checking if the transfer and topmost cards are of opposite suits
            if rank2 == (rank1-1):
                #check if rank of transfer card is one greater than rank of 
                #topmost card, then pop it, add it to tableau column, return
                #True
                transfer_card = waste.pop()
                tableau[t_num].append(transfer_card)
                return True
            
            else:
                #if there is a mismatch of rank, return False
                return False
        else:
            #if card suits are not opposite (same suit), return False
            return False
    
    


def waste_to_foundation( waste, foundation, f_num ):
    '''This function is designed to move/deal a card from the waste (talon) 
    pile to the correct one of the 4 piles in the foundation 
    (one is present for each suite).If transfer was successfully done it 
    returns True, else False. Here, f_num is the index of pile (nested list)
    in the foundation the card has to be moved to. For the card to move into 
    foundation, it should be of same suit and one rank higher than topmost 
    card in foundation pile. If foundation is empty then card has to be only
    an Ace.
    
    Parameters: waste, foundation, f_num
    Returns: True or False
    Displays: Nothing '''
    transfer_card = waste[-1]  #this is the card to be transferred.
    if len(foundation[f_num]) == 0:
        #destination pile of foundation is empty, then only an ace (card with
        #rank 1) is possible to be added
        if transfer_card.rank() == 1:
            #if the card is an ace, then pop it and move to particular
            #pile in foundation, return True.
            transfer_card = waste.pop()
            foundation[f_num].append(transfer_card)
            return True
        
        else:
            #if not an ace, return False
            return False
        
    else:
        #destination pile of foundation is not empty, check if transfer card is
        #of same suit and one rank higher than topmost card in foundation pile
        if (transfer_card.rank() == foundation[f_num][-1].rank() + 1)\
        and (transfer_card.suit() == foundation[f_num][-1].suit()):
            #if condition satisfied, then pop card from waste, add to 
            #foundation pile, return True
            transfer_card = waste.pop()
            foundation[f_num].append(transfer_card)
            return True
        
        else:
            #if above conditions not satisfied, return False
            return False
    
    
    

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''This function is designed to move/deal a card from the tableau to the 
    correct one of the 4 piles in the foundation (one is present for each 
    suite). If transfer was successfully done it returns True, else False. 
    Here, f_num is the index of pile (nested list) in the foundation the card 
    has to be moved to and t_num is the column number in tableau that the 
    card is currently in. For the card to move into foundation, it should be 
    of same suit and one rank higher than topmost card in foundation pile. If 
    foundation is empty then card has to be only an Ace.
    
    Parameters: tableau, foundation, t_num, f_num
    Returns: True or False
    Displays: Nothing '''
    
    transfer_card = tableau[t_num][-1] #this is the card to be transferred.
    
    if len(foundation[f_num]) == 0:
        #destination pile of foundation is empty, then only an ace (card with
        #rank 1) is possible to be added
        
        if transfer_card.rank() == 1:
            #if the card is an ace, then pop it and move to particular
            #pile in foundation, return True.
            transfer_card = tableau[t_num].pop()
            foundation[f_num].append(transfer_card)
            
            if tableau[t_num]:
                #if source column in tableau is not empty after transferring 
                #card then next card in column is turned face up if not 
                #already so, return True
                next_card = tableau[t_num][-1]
                if next_card.is_face_up():
                    return True
                else:
                    next_card.flip_card()
                    return True
                
            else:
                #if source column in tableau is empty after transferring 
                #card then just return True
                return True
            
        else:
            #if the card is not an ace, return False
            return False
        
    else:
        #destination pile of foundation is not empty, check if transfer card is
        #of same suit and one rank higher than topmost card in foundation pile
        if (transfer_card.rank() == foundation[f_num][-1].rank() + 1)\
        and (transfer_card.suit() == foundation[f_num][-1].suit()):
            #if condition satisfied, then pop card from tableau column, add to 
            #foundation pile, return True
            transfer_card = tableau[t_num].pop()
            foundation[f_num].append(transfer_card)
            
            if tableau[t_num]:
                #if source column in tableau is not empty after transferring 
                #card then next card in column is turned face up if not 
                #already so, return True
                next_card = tableau[t_num][-1]
                if next_card.is_face_up():
                    return True
                else:
                    next_card.flip_card()
                    return True
                
            else:
                #if source column in tableau is empty after transferring 
                #card then just return True
                return True
            
        else:
            #if the card is not an ace, return False
            return False




def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''This function is designed to move/deal a card from one column in the 
    tableau to another column in the tableau. If transfer was successfully done
    it returns True, else False. Here, t_num1 is the source column number in 
    tableau and t_num2 is the destination column number. For the card to move 
    into destination column in tableau, it should be of opposite colour and 
    one rank lower than topmost card in that tableu column. If tableu is empty
    then card has to be only a King.
    
    Parameters: tableau, t_num1, t_num2
    Returns: True or False
    Displays: Nothing '''
    
    transfer_card = tableau[t_num1][-1]  #this is the card to be transferred
    rank2 = transfer_card.rank()         #rank of the transfer card
    suit2 = transfer_card.suit()         #suit of the transfer card
    
    if len(tableau[t_num2]) == 0:        
        #destination column of tableau is empty, then only a king (card with
        #rank 13) is possible to be added 
        if rank2 == 13:
            #if the card is a king, then pop it and move to particular
            #column in tableau, return True. 
            transfer_card = tableau[t_num1].pop()
            tableau[t_num2].append(transfer_card)
            
            if tableau[t_num1]:
                #if source column in tableau is not empty after transferring 
                #card then next card in column is turned face up if not 
                #already so, return True
                next_card = tableau[t_num1][-1]
                if next_card.is_face_up():
                    return True
                else:
                    next_card.flip_card()
                    return True
            else:
                #if source column in tableau is empty after transferring 
                #card then just return True
                return True
            
        else:
            #if the card is not a king, return False
            return False
    else:
        topmost_card = tableau[t_num2][-1]  #this is the topmost card of column
        rank1 = topmost_card.rank()         #rank of the topmost card
        suit1 = topmost_card.suit()         #suit of the topmost card
        
        if suit1 in (1,4) and suit2 in (2,3): 
            # checking if the transfer and topmost cards are of opposite suits
            if rank2 == (rank1-1):
                #check if rank of transfer card is one greater than rank of 
                #topmost card, then pop it, add it to tableau column, return
                #True
                transfer_card = tableau[t_num1].pop()
                tableau[t_num2].append(transfer_card)
                
                if tableau[t_num1]:
                    next_card = tableau[t_num1][-1]
                    if next_card.is_face_up():
                        return True
                    else:
                        next_card.flip_card()
                        return True
                else:
                    return True
            else:
                #If there is a mismatch of rank, return False
                return False
            
        elif suit1 in (2,3) and suit2 in (1,4):
            # checking if the transfer and topmost cards are of opposite suits
            if rank2 == (rank1-1):
                #check if rank of transfer card is one greater than rank of 
                #topmost card, then pop it, add it to tableau column, return
                #True
                transfer_card = tableau[t_num1].pop()
                tableau[t_num2].append(transfer_card)
                if tableau[t_num1]:
                    next_card = tableau[t_num1][-1]
                    if next_card.is_face_up():
                        return True
                    else:
                        next_card.flip_card()
                        return True
                else:
                    return True
            else:
                #If there is a mismatch of rank, return False
                return False
        else:
            #if they are of same suit, return False
            return False
    
    
    
    
def check_win (stock, waste, foundation, tableau):
    '''This function checks if the game's status is a winning situation. That 
    is if all cards are in their respective foundation piles, stock, waste and
    tableau are empty.
    Parameters: stock, waste, foundation, tableau
    Returns: True or False
    Displays: Nothing
    '''
    stock_good = False  #boolean value to check is stock is in winning status 
    foundation_good = False #bool value to check is foundn is in winning status 
    waste_good = False  #boolean value to check is waste is in winning status 
    tableau_good = False  #bool value to check is tableau is in winning status 
    tableau_count = 0   #counter to keep track of number of filled columns 
    foundation_count = 0 #counter to keep track of number of filled piles
    
    if len(waste) == 0: 
        #if waste is empty, waste is in winning status
        waste_good = True
    
    if stock.is_empty():
        #if stock is empty, stock is in winning status
        stock_good = True
    
    for column in tableau:
        #checking if every column in tableau is empty. If so, increment counter
        #variable by 1 
        if len(column) == 0:
            tableau_count += 1
            
    if tableau_count == 7:
        #If all the seven columns of tableau are empty, tableau is in winning
        #status
        tableau_good = True
    
    for pile in foundation:
        #checking if every pile in foundation has 13 cards. If so, increment 
        #counter variable by 1 
        if len(pile) == 13:
            foundation_count += 1
        
    if foundation_count == 4:
        #If all the 4 piles of foundation are filled, foundation is in winning
        #status
        foundation_good = True
    
    if stock_good and foundation_good and waste_good and tableau_good:
        #if all data structures are in winning status, return True
        return True
    else:
        #Otheriwse return False
        return False
        
    
    
    
        
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    '''This function has no parameter but it controls flow and execution of
    the Klondike game by displaying outputs, error messages as required.
    '''
    tableau, stock, foundation, waste = initialize() #initializing all vars
    print(MENU)  #displaying the MENU of options
    while True:  
        #main while loop for running program
        display(tableau, stock, foundation, waste) #to display the board
        opt = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        parse_result = parse_option(opt) #check if option is valid
        
        if parse_result == None:
            #if the result of parse_option function is None, that means it is
            #an invalid input for option, skip the iteration and go to loop
            #header
            continue
       
        elif parse_result[0] == 'TT':
            #if the selected move is tableau to tableau, then call the function
            #and store its returned value. If returned value is True, then 
            #skip to next iteration (continue statement) else print error 
            #message
            tt_result = tableau_to_tableau(tableau, parse_result[1]-1,\
                                           parse_result[2]-1)
            if tt_result:
                continue
            else:
                print("\nInvalid move!\n")
        
        elif parse_result[0] == 'TF':
            #if the selected move is tableau to foundation, then call function
            #and store its returned value. If returned value is True, then 
            #check if check_win() function returns True. If so print 'You won!'
            #display board, terminate loop. Otherwise skip to next iteration 
            #(continue statement)
            tf_result = tableau_to_foundation(tableau, foundation,\
            parse_result[1]-1, parse_result[2]-1)

            if tf_result: #check if return value is True
                if check_win(stock, waste, foundation, tableau):
                    print('You won!')
                    display(tableau, stock, foundation, waste)
                    break
                else:
                    continue
            else: #if return value is False, print error message
                print("\nInvalid move!\n")
        
        elif parse_result[0] == 'WF':
            #if the selected move is waste to foundation, then call function
            #and store its returned value. If returned value is True, then 
            #check if check_win() function returns True. If so print 'You won!'
            #display board, terminate loop. Otherwise skip to next iteration 
            #(continue statement)
            wf_result = waste_to_foundation(waste, foundation,\
                                            parse_result[1]-1)
            if wf_result: #check if return value is True
                if check_win(stock, waste, foundation, tableau):
                    print('You won!')
                    display(tableau, stock, foundation, waste)
                    break
                else:
                    continue
            else:  #if return value is False, print error message
                print("\nInvalid move!\n")
                
        elif parse_result[0] == 'WT':
            #if the selected move is waste to tableau, then call the function
            #and store its returned value. If returned value is True, then 
            #skip to next iteration (continue statement) else print error 
            #message
            wt_result = waste_to_tableau(waste, tableau, parse_result[1]-1)
            if wt_result: #check if return value is True
                continue
            else:
                print("\nInvalid move!\n")
                
        elif parse_result[0] == 'SW':
            sw_result = stock_to_waste(stock, waste)
            if sw_result:
                continue
            else:  #if return value is False, print error message
                print("\nInvalid move!\n")
                
        elif parse_result == ['R']:
            #if user wants to restart game, shuffle stock deck, re-initialize
            #all the data structures, print MENU, skip to next iteration
            stock.shuffle()
            tableau, stock, foundation, waste = initialize()
            print(MENU)
            continue
        
        elif parse_result == ['H']:
            #if users wants to see MENU, print it.
            print(MENU)
            
        elif parse_result == ['Q']:
            #if user wants to quit, terminate the loop.
            break
        
        

if __name__ == '__main__':
     main()
