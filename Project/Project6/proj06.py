###############################################################################
#  CSE 231 Project #6
#
#  Algorithm
#    import csv module
#    import from operator module itemgetter 
#    declare constants with given value
#
#    define function open_file(). This function prompts the user to input a 
#    file name to open and keeps prompting until a valid name is entered.  
#    Return the file pointer.
#    
#    define function read_file(). This function creates list of tuples. Each 
#    tuple stands for a character following format: (name, element, weapon, 
#    rarity, region) The type of each element in the tuple: (string, string, 
#    string, int, string)  If there is no value for the region, use None.
#    
#    define function get_characters_by_criterion(). This function takes 
#    in a list of character tuples and retrieves the characters that match a 
#    certain criteria.  If there is a problem with a value or criteria 
#    parameter, character is not added to the return list.
#
#    define function get_characters_by_criteria(). This function takes as 
#    parameter the list of tuples returned by the read_file function, an 
#    element, a weapon, and a rarity and returns a list of tuples filtered 
#    using those 3 criteria.
#
#    define function get_region_list(). This function takes a master list of 
#    character tuples and retrieves all available regions into a list without 
#    any duplicates. If the region is None, it is not included in the list.
#
#    define function sort_characters(). This function takes a list of character
#    tuples and creates a new list where character tuples have been sorted. The
#    order of sorting is by decreasing order of rarity and alphabetically by 
#    name.
#
#    define function display_characters(). This function takes a list of 
#    character tuples and displays characters along with their information 
#    using the formats given (HEADER and ROWS). If a region has the value None,
#    display 'N/A'. If list_of_tuples is empty, print an error message.
#
#    define function get_option(). This function displays a menu of options and
#    prompts for input. This function does not take parameters.
#
#    define main() function
#        call open_file() and assign it to filepointer, fp
#        call read_file() to read the specified file and store list_of_tuples
#        returned in a variable
#        while loop
#            call get_option() to display MENU, prompt for user input (option)
#            and store the returned value in a variable called opt
#            if opt equals 1
#                call get_region_list() taking in list_of_tuples, store the 
#                resulting list of regions in variable region_list, print this
#                list using join() and string ', ' to ensure proper format
#            
#            elseif opt equals 2
#                prompt user to input a criteria number from the criteria menu
#                if criteria option inputted is between 1 and 4 (inclusive), 
#                    prompt user to input a value for the corresponding 
#                    criterion  
#                    if criteria option inputted corresponds to RARITY
#                        try to convert the value inputted to int, if unable to
#                        convert then display error message and reprompt for
#                        value input
#                else
#                    print error message, display criteria menu and reprompt 
#                    for criteria option
#                call get_characters_by_criterion() with list_of_tuples, 
#                criteria input, and value as parameter. Store the resulting 
#                list of characters in a variable called return_list
#                sort return_list by calling sort_characters() and storing the
#                resulting final list as list_sorted
#                call display_characters to display the character tuples in the 
#                required format with list_sorted as parameter.
#
#              elseif opt equals 3
#                  ask user to input element, weapon, and rarity
#                  try to convert rarity to int, if not possible then print an
#                  error message and reprompt a value for rarity and convert to
#                  an int
#                  call get_characters_by_criteria() with list_of_tuples, 
#                  element, weapon, rarity as parameters. Store the resulting 
#                  list of characters in a variable called return_list
#                  sort return_list by calling sort_characters() and storing 
#                  resulting final list as list_sorted
#                  call display_characters to display the character tuples in 
#                  required format with list_sorted as parameter.
#              elseif opt equals 4
#                  break
#    close the file
#  call main() function
#  end of program                  
#
###############################################################################

import csv           #importing the csv module 7
from operator import itemgetter   #import itemgetter from standard operator 
                                  #module

NAME = 0        #these constants refer to indices of the corresponding criteria
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}" #header string formatting
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"   #row string formatting



def open_file():
    '''
    This function prompts the user to input a file name to open and keeps
    prompting until a valid name is entered.  Return the file pointer. 
    Parameter: none
    Returns: file pointer
    Displays: prompt or error messages accordingly
    '''
    
    file_name = input("Enter file name: ")
    while True:
        try:  #trying to open the file with inputted name in read mode
            fp = open(file_name, 'r') 
            break
        
        except FileNotFoundError: 
            #if invalide filename inputted, exception is raised
            print("\nError opening file. Please try again.") 
            file_name = input("Enter file name: ")
            continue
    return fp   #returning file pointer 
    
    

def read_file(fp):
    '''
    This function creates list of tuples. Each tuple stands for a character 
    following format: (name, element, weapon, rarity, region) The type of each
    element in the tuple: (string, string, string, int, string)  If there is no
    value for the region, use None.
    Parameter: file pointer.
    Returns: list of tuples 
    Displays: nothing.
    '''
    
    reader = csv.reader(fp)   #reading the csv file 
    charac_list = []    
    next(reader, None)    #this line skips the header of csv file
    for charac in reader:  
        if charac != []:   #skipping the empty line present in csv file
            char_name = charac[0]   
            char_rarity = int(charac[1])  #convert rarity to int 
            char_elem = charac[2]
            char_weapon = charac[3]
            if charac[4] == '':  #if region is missing, assign it None value
                char_region = None
            elif charac[4] != '':   
                char_region = charac[4]
                
            #storing each character's info as a tuple
            charac_info = (char_name, char_elem, char_weapon, char_rarity,\
                           char_region)
            #making a list of tuples with all characters 
            charac_list.append(charac_info)

    return charac_list



def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''
    This function takes in a list of character tuples and retrieves the 
    characters that match a certain criteria.  If there is a problem with a 
    value or criteria parameter, character is not added to the return list.
    Parameter: list of tuples, int, int/string
    Returns: list of tuples 
    Displays: nothing
    '''
    
    global NAME
    global ELEMENT
    global WEAPON
    global RARITY
    global REGION
    return_list = []

    if list_of_tuples == []: #if the list of tuples is empty, return empty list
        return return_list
    
    else:
        for charac in list_of_tuples:
            if criteria == ELEMENT: #if element is selected as criteria
                if charac[ELEMENT] == None: 
                    #if its value is None, skip that character
                    continue
                elif  charac[ELEMENT] != None:
                    #if its value is not None, check if value inputted matches
                    #the character's value for element crtierion
                    if value.upper() == charac[ELEMENT].upper():
                        return_list.append(charac)
                        
                        
            elif criteria == WEAPON: #if weapon is selected as criteria
                if charac[WEAPON] == None: 
                #if its value is None, skip that character
                    continue
                elif charac[WEAPON] != None:
                    #if its value is not None, check if value inputted matches
                    #the character's value for weapon crtierion
                    if value.upper() == charac[WEAPON].upper():
                        return_list.append(charac)
                
                
            elif criteria == RARITY: #if rarity is selected as criteria
                if type(value) == int: #check if value's type is int
                    if value == charac[RARITY]:
                        #check if value inputted matches the character's value 
                        #for rarity crtierion
                        return_list.append(charac)
                else:
                    #if value's type not int, skip that character
                    continue
                
            elif criteria == REGION:  #if region is selected as criteria
                if charac[REGION] == None:
                    #if its value is None, skip that character
                    continue
                elif charac[REGION] != None:
                    #if its value is not None, check if value inputted matches
                    #the character's value for weapon crtierion
                    if value.upper() == charac[REGION].upper():
                        return_list.append(charac)
                        
        return return_list                       

    
            
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''
    This function takes as parameter the list of tuples returned by the 
    read_file function, an element, a weapon, and a rarity and 
    returns a list of tuples filtered using those 3 criteria.
    Parameter: list of tuples, string, string, int
    Returns: list of tuples 
    Display: nothing.
    '''
    
    global NAME
    global ELEMENT
    global WEAPON
    global RARITY
    global REGION
    
    #call the get_characters_by_criterion() to filter by 3 criteria one after
    #the other - element, weapon, and rarity. Returned list of one is the 
    #parameter for the next function call
    list_returned = get_characters_by_criterion(master_list, ELEMENT, element)
    list_returned = get_characters_by_criterion(list_returned, WEAPON, weapon)
    list_returned = get_characters_by_criterion(list_returned, RARITY, rarity)
    
    return list_returned

    

def get_region_list  (master_list):
    '''
    This function takes a master list of character tuples and retrieves all 
    available regions into a list without any duplicates. If the region is 
    None, it is not included in the list.
    Parameters: list of tuples
    Returns: sorted list of strings 
    Display:  nothing.
    '''
    
    region_list = []
    for charac in master_list: 
        #checking for duplicate region names. If not present then add to 
        #the region_list
        if charac[4] not in region_list and charac[4] != None: 
            region_list.append(charac[4])
    region_list.sort()
    return region_list
        
    
    
def sort_characters (list_of_tuples):
    '''
    This function takes a list of character tuples and creates a new list 
    where character tuples have been sorted. The order of sorting is by 
    decreasing order of rarity and alphabetically by name. 
    Parameters: list of tuples 
    Return : sorted list of tuples
    Display: nothing
    '''
    
    global RARITY
    new_lot = sorted(list_of_tuples)  #sorting alphabetically by name 
    #sorting reverse order of rarity
    new_lot = sorted(new_lot, key=itemgetter(RARITY), reverse = True)
    
    return new_lot
    


def display_characters (list_of_tuples):
    '''
    This function takes a list of character tuples and displays characters 
    along with their information using the formats given (HEADER and ROWS). 
    If a region has the value None, display 'N/A'. If list_of_tuples is empty, 
    print an error message.
    Parameters: list of tuples
    Return: nothing
    Display: character attributes
    '''
    
    global HEADER_FORMAT
    global ROW_FORMAT
    if list_of_tuples == []: #if the list of tuples is empty, return empty list
        print("\nNothing to print.")
        
    elif list_of_tuples != []:
        print(HEADER_FORMAT.format('Character', 'Element', 'Weapon', 'Rarity',\
                                   'Region'))
        for charac in list_of_tuples:
            if charac[4] == None:
                print(ROW_FORMAT.format(charac[0], charac[1], charac[2],\
                                        charac[3], 'N/A'))
            elif charac[4] != None:
                print(ROW_FORMAT.format(charac[0], charac[1], charac[2],\
                                        charac[3], charac[4]))
    
    
    

def get_option():
    '''
    This function displays a menu of options and prompts for input. This 
    function does not take parameters.
    Parameters: nothing
    Return: int 
    Display: menu and error message
    '''
  
    global MENU
    global INVALID_INPUT
    
    opt = int(input(MENU)) #displaying the MENU and prompting for user option 
    if opt >= 1 and opt <= 4: 
        return opt
    else:
        print(INVALID_INPUT) #invalid input, then display error message
    
    
  
def main():
    '''
    Inside this function we have the whole program code wherein functions 
    are called and inputs and outputs are present.
    No arguments passed
    No values returned but they are printed according to condition satisfaction
    '''
    fp = open_file()  #opening file. fp is file pointer
    list_of_tuples = read_file(fp)
    while True:  #Main while loop 
        opt = get_option() #calling function to get an option as input
        
        if opt == 1:  #if first option on menu selected
            region_list = get_region_list(list_of_tuples) 
            print("\nRegions:")
            print(', '.join(region_list))#joining regionlist elements with ', '
            
            
        elif opt == 2:  #if second option on menu selected
            crit_opt = int(input(CRITERIA_INPUT)) #prompt for criteria input
            if crit_opt >= 1 and crit_opt <= 4: 
                #if criteria option is valid input, prompt for corresponding
                #value input
                val_input = input(VALUE_INPUT) 
                if crit_opt == RARITY:
                    #if the criteria is rarity, try to convert value to int. If
                    #not possible, then print error message, repromt for value
                    try:
                        val_input =  int(val_input)
                    except ValueError:
                        print(INVALID_INPUT)
                        val_input = input(VALUE_INPUT)
            
            else:
                #If criteria option is an invalid input, print error message, 
                #reprompt for criteria option
                print(INVALID_INPUT)
                crit_opt = int(input(CRITERIA_INPUT))
                
            return_list = get_characters_by_criterion(list_of_tuples,\
                                                      crit_opt, val_input)
            list_sorted = sort_characters(return_list)
            display_characters(list_sorted)
        
        
        
        elif opt == 3:
           element_inp = input(ELEMENT_INPUT)
           weapon_inp = input(WEAPON_INPUT)
           rarity_inp = input(RARITY_INPUT)
           try:
               #trying to convert the rarity input to int
               rarity_inp =  int(rarity_inp)
               
           except:
               #if exception raised, print error message, reprompt for rarity
               #input and convert to int
               print(INVALID_INPUT)
               rarity_inp = int(input(RARITY_INPUT))
        
           return_list = get_characters_by_criteria(list_of_tuples,\
                                                    element_inp, weapon_inp,\
                                                        rarity_inp)
           list_sorted = sort_characters(return_list)
           display_characters(list_sorted)
           
           
           
        elif opt == 4:
            #loop is terminated
            break
    fp.close()   #closing the csv file

# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()    #calling main function 
    