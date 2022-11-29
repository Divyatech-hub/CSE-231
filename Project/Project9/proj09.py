###############################################################################
#  CSE 231 Project #9
#
#  ALGORITHM
#
#  import csv module 
#  import itemgetter from operator module
#  declare constants with given value
#
#  define open_file() that prompts user for both files to open and keeps 
#  looping for the first file until open. It returns file pointers for both 
#  files or displays error messages accordingly.
#
#  define read_file(securities_fp) that takes the securities file pointer with
#  names of companies and their codes to create a set of all company names
#  along with a master dictionary where key is the company code and value
#  is a list with [company name, the sector of the company, the subsector of 
#  the company, the address, the date added, an empty list]
#
#  define add_prices (master_dictionary, prices_file_pointer) that changes
#  master dictionary by adding to the empty list for the particular company in 
#  each prices file line. The resulting master_dictionary looks like this 
#  D = {code: [name, sector, subsector, address, date, [[date, open info, 
#  close info, low info, high info],…]]}. It returns the changed master dict,
#  prices file pointer
#
#  define get_max_price_of_company (master_dictionary, company_symbol) that 
#  takes the master dictionary and company symbol, and it gets max high price, 
#  the date of the max price. It returns the tuple (max_price, date) or
# (None, None) if no max exists or company_symbol not in master dict.
#
#  define find_max_company_price (master_dictionary) that takes master dict and
#  finds the company with highest high price ignoring companies that do not 
#  have anything in their price list. It returns company with maximum value & 
#  max price as tuple. 
#
#  define get_avg_price_of_company (master_dictionary, company_symbol) that 
#  finds the average high price rounded to 2 decimal places for the company. 
#  If company does not exist or no price data for company, it returns 0.0.  
#
#  define display_list (lst) that takes list of strings, displays it in 3
#  columns (each being 35 characters wide). It adds a new line character “\n”
#  when done printing all elements of list. The special case is when there are
#  less than 3 companies in last line, then there is no "\n" added. 
#
#  define main() function
#    display the welcome banner using WELCOME constant
#    call open_file(), assign the returned file pointer to variables prices_fp,
#    and securities_fp
#    call read_file(securities_fp) and assign returned values to variables 
#    company_names_set, master_dict 
#    call add_prices(master_dict, prices_fp) and re-assign returned values to 
#    master_dict, prices_fp to update values 
#    main while loop
#    display MENU of options
#    prompt user to input an option, check if option is valid
#       if opt equals 1
#          display heading "Companies in the New York Stock Market from 2010 
#          to 2016" in the mentioned format
#          convert company_names_set returned by read_file() into list, sort it
#          call display_list(comp_names_list) with the comp_names_list as the
#          parameter 
#
#       elif opt equals 2
#          display heading "\ncompanies' symbols:" in the mentioned format
#          store the company_symbols retrieved from master_dict.keys() function
#          in a list called comp_code_list, then sort it 
#          call display_list(comp_code_list) with the comp_code_list as the
#          parameter 
#
#       elif opt equals 3
#          prompt user to input a company_symbol, check if company_symbol is 
#          valid. If not, then display error message & keep repromting 
#          continuosly until valid company_symbol entered.

#          if symbol is valid, then call 
#          get_max_price_of_company(master_dict, company_symbol) and assign the
#          returned value to max_high_price_tup  
#          if value of max_high_price_tup is (None, None)
#             display a message saying "\nThere were no prices."
#          
#          else
#             print the max high price and the date for that stock retrived 
#             from the max_high_price_tup
#
#       elif opt equals 4
#          call find_max_company_price(master_dict) and store its returned 
#          values in variables comp_code, highest_price, the print it. 
#
#       elif opt equals 5 
#          prompt user to input a company_symbol, check if company_symbol is 
#          valid. If not, then display error message & keep repromting 
#          continuosly until valid company_symbol entered.
#          
#          if symbol is valid, then call 
#          get_avg_price_of_company(master_dict, company_symbol) and assign the
#          returned value to avg_price
#          if value of avg_price is 0.0
#             display a message saying "\nThere were no prices."
#          
#          else
#             print the avg_price for that stock rounded to 2 decimal places
#
#       elif opt equals 6
#          break
#    else if opt entered is invalid
#       diplay error message "\nInvalid option. Please try again."
#       continue
#  call main() function
#  end of program
#
###############################################################################
        
import csv  
from operator import itemgetter
MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    


def open_file():
    '''This function is going to ask the user for both files to open. You will 
    keep looping for the first one until a file is open. Afterwards, you have 
    to do the same for the second file. 
    
    Parameters: None
    Returns : Two file pointers. (file pointer of prices, and the file pointer 
    of securities) in that order
    Displays: nothing. '''
    while True:
        f1_name = input("\nEnter the price's filename: ") 
        
        try:                          #trying to open file in read mode
            fp1 = open(f1_name, 'r')
        except FileNotFoundError:    #if file not found, reprompt user for name
            print("\nFile not found. Please try again.")
            continue
        
        f2_name = input("\nEnter the security's filename: ")
        
        try:                         #trying to open file in read mode
            fp2 = open(f2_name, 'r')
        except FileNotFoundError:    #if file not found, reprompt user for name
            print("\nFile not found. Please try again.")
            continue
        break
    return fp1, fp2
    



def read_file(securities_fp):
    '''This function takes the security’s file pointer that has the names of 
    the companies and their codes to create a set of all the company’s names.
    It also creates a master dictionary where key is the company code and value
    is a list with [company name, the sector of the company, the subsector of 
    the company, the address, the date added, an empty list].
    
    Parameters: A file pointer
    Returns: set, dictionary
    Displays: nothing. '''
    
    company_names_set = set()
    master_dict = {}
    
    sec_reader = csv.reader(securities_fp)  #reading the securities.csv file
    next(sec_reader, None)                  #skipping the file header
    for line in sec_reader:
        if line == []:      #skipping the empty line present in csv file
            continue
        else:
            company_names_set.add(line[1]) #adding company names to set
            master_dict[line[0]] = [line[1], line[3], line[4], line[5],\
                                    line[6], []]  #adding company info to dict
            
    return company_names_set, master_dict
            
            
    
        
def add_prices (master_dictionary, prices_file_pointer):
    '''This function changes the master dictionary while reading the prices 
    file. When prices file is being read, it adds to the empty list for the 
    particular company in each prices file line. The resulting 
    master_dictionary should look like this D = {code: [name, sector, 
    subsector, address, date, [[date, open info, close info, low info, 
    high info],…]]} 
    
    Parameters: dictionary, file pointer 
    Returns : None
    Displays nothing   
    '''
    prices_reader = csv.reader(prices_file_pointer) 
    next(prices_reader, None)              #skip the file header 
    for line in prices_reader:
        if line == []:
            continue
        elif line[1] in master_dictionary:#mapping thru dict with company codes
            prices_info_list = []
            date = line[0]
            open_info = float(line[2]) #converting prices to float
            close_info = float(line[3])
            low_info = float(line[4])
            high_info = float(line[5])
            prices_info_list = [date, open_info, close_info, low_info,\
                                high_info]#making list of prices for each compy
            master_dictionary[line[1]][5].append(prices_info_list)
            #updating dictionary's value for that compny with prices list
            
    return master_dictionary, prices_file_pointer
            
    
    
def get_max_price_of_company (master_dictionary, company_symbol):
    '''This function takes the master dictionary and a company symbol, and it 
    gets the max high price and the date of the max price. It returns the tuple
    (max_price, date) or a tuple (None, None) if no max exists.
    Parameters: dictionary, string
    Returns : (float, string)
    Displays nothing''' 
    list_of_tuples = []   #declaring a list
    if company_symbol in master_dictionary:
        if master_dictionary[company_symbol][5] == []: #if prices_list is empty
            return None, None
        else:
            for prices_list in master_dictionary[company_symbol][5]:
                #If prices_list (or more than one) exist/exists then append the
                #high stock price and its date as a tuple in list_of_tuples
                list_of_tuples.append((prices_list[4], prices_list[0]))
                
            max_tuple = max(list_of_tuples) #find the maximum high price 
            return max_tuple 
            
    else: #if company_symbol is invalid, return (None, None)
        return None, None 
    
    
    

def find_max_company_price (master_dictionary):
    '''This function takes the master dictionary and finds the company with the
    highest high price. It ignores companies that do not have anything in their
    price list.  This function returns the company with the maximum value and 
    the price of it, in that order. 
    
    Parameters: dictionary
    Returns : (string, float)
    Displays nothing '''
    
    company_tup_list = list()
    for company_symb in master_dictionary: 
        #if company_symbol is valid, call the get_max_price_of_company to get
        #max high price and its date as tuple for a compny
        max_tup_per_compny = get_max_price_of_company(master_dictionary,\
                                                      company_symb)
    
        if max_tup_per_compny != (None, None):
            #if the get_max_price_of_company returned a value that is not 
            #None, None .i.e. the max_high_price and its date were returned,
            #then create a new tuple with the max_high_price value and compny 
            #code, append it to list. 
            new_max_tup_per_compny = (company_symb,) + max_tup_per_compny[0:1]
            company_tup_list.append((new_max_tup_per_compny))
            
    max_of_all_tuples = max(company_tup_list, key = itemgetter(1)) 
    return max_of_all_tuples
        
    

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''This function uses the master dictionary and company symbol to find the
    average high price for the company with the average rounded to two decimal
    places. If the company does not exist or there is no price data for the 
    company, it returns 0.0.  
    Parameters: dictionary, string 
    Returns : float
    Displays nothing '''
    prices_sum = 0
    if company_symbol in master_dictionary:  #if company_symbol is valid
        company_info = master_dictionary[company_symbol]
        if company_info[5] == []: #if price_list has no values, return 0.0
            return 0.0
        else:
            for prices_list in company_info[5]: 
                #if price_List has values, add the high price of stock to sum 
                prices_sum += prices_list[4]
            prices_average = prices_sum/len(company_info[5]) #find average 
            return round(prices_average,2)  #round average to 2 decimal places 
        
    else:   # if company_symbol is invalid,return 0.0
        return 0.0
    
            
def display_list (lst):  # "{:^35s}"
    '''This function does not return anything, but it takes a list of strings 
    and displays that list in three columns, each column is 35 characters wide.
    It adds a new line character “\n” when done printing all elements of list. 
    The special case is when there are less than 3 companies in the last line
    of the display, then there is no "\n" added. 
    Parameters: list of strings
    Returns : None
    Display: prints list in three columns going from left to right, 
    # top down. '''
    columns = 0  #variable carrying the number of columns 
    list_len = len(lst) #length of the list inputted 
    for index in range(list_len):        
        if columns != 0 and columns % 3 == 0:  
            #if column num is divisible by 3 and not equal to 0 i.e. 3,6,9,...
            #then go to nextline
            print() 
        print("{:^35s}".format(lst[index]), end = '')
        columns = columns + 1 #Increment column number after every iteration
        
    if list_len % 3 == 0:  
        #checking if there are 3 items in last line, if so print "\n"
        print("\n")
    elif list_len % 3 != 0:
        print()
        
        

def main():
    print(WELCOME)  #print welcome banner
    prices_fp, securities_fp = open_file()  #opening both csv files 
    company_names_set, master_dict = read_file(securities_fp)
    master_dict, prices_fp = add_prices(master_dict, prices_fp)
    while True:  #main while loop 
        print(MENU)  #print the MENU of options 
        opt = input("\nOption: ")   #ask user to input an option
        if opt in "123456":  #checking if option is valid 
            if opt == '1':
                print("\n{:^105s}".format\
                ("Companies in the New York Stock Market from 2010 to 2016"))
                comp_names_list = list(company_names_set) #convert set to list
                comp_names_list.sort()
                display_list(comp_names_list) 
                print()
            
            
            
            elif opt == '2':
                print("\ncompanies' symbols:")
                comp_code_list = list(master_dict.keys())#retrieve keys of dict
                comp_code_list.sort()
                display_list(comp_code_list)
                print()
                
                
            elif opt == '3':
                #ask user to input a compny symbol
                company_symbol = input\
                    ("\nEnter company symbol for max price: ")
                flag = True
                while flag:
                    #check if compny symbol is  valid
                    if company_symbol not in master_dict:
                        #if invalid, print error message and reprompt, until
                        #valid symbol provided
                        print\
                        ("\nError: not a company symbol. Please try again."\
                             )
                        company_symbol = input\
                            ("\nEnter company symbol for max price: ")
                        continue
                    else:
                        flag = False
            
                max_high_price_tup = get_max_price_of_company\
                    (master_dict, company_symbol)
                if max_high_price_tup == (None, None):
                    #if (None, None) returned, that means there were no prices
                    #for that particular company.
                     print("\nThere were no prices.")
                else:
                    print(\
                "\nThe maximum stock price was ${:.2f} on the date {:s}/\n".
                format(max_high_price_tup[0], max_high_price_tup[1]))
                        
                    
                    
                    
            elif opt == '4':
                #call the find_max_company_price(master_dict) to get company
                #symbol and highest price of company with max price. 
                 comp_code, highest_price = find_max_company_price(master_dict)
                 print\
("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".\
 format(comp_code, highest_price))
            
            
           
            elif opt == '5':
                #ask user to input a compny symbol
                company_symbol = input\
                    ("\nEnter company symbol for average price: ")
                
                while True:
                    #check if compny symbol is  valid
                    if company_symbol not in master_dict:
                        #if invalid, print error message and reprompt, until
                        #valid symbol provided
                        print\
                        ("\nError: not a company symbol. Please try again.")
                        company_symbol = input\
                            ("\nEnter company symbol for average price: ")
                        continue
                    break

                avg_price = get_avg_price_of_company\
                    (master_dict, company_symbol)
                if avg_price == 0.0:
                    #if 0.0 returned, that means there were no prices
                    #for that particular company.
                    print("\nThere were no prices.")
                else:
                    print("\nThe average stock price was ${:.2f}.\n".\
                          format(avg_price))
                        
                
                
                
            elif opt == '6':
                break
                
        else:
            #if user entered an invalid option i.e. not in '123456' then print 
            #error message and reprompt. 
            print("\nInvalid option. Please try again.")
            continue
        

    
if __name__ == "__main__": 
    main() 


