###############################################################################
#  CSE 231 Project #2

#  Algorithm
#    display the game banner
#    main while loop
#         ask user if they want to continue
#         if input is A
#              prompt user for customer code
#              if customer code is not BD or D or W, give error message but if  
#              correct code, then proceed
#              prompt user for num of days, odometer start and odometer 
#              end readings
#              note down the base and mileage charge for each case and 
#              sub-case
#              perform the required miles calculations accordingly, get  
#              amount due for that scenario
#              output a customer summary with all transaction details, miles, 
#              and amount
#         elif input is B
#              print(Thank you message)
#              end program
###############################################################################


import math  #importing the math module

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"   #welcome message

print(BANNER)

while True:                #the main while loop that iterates till user says
    prompt = input("\nWould you like to continue (A/B)? \n")
    
    if prompt == "A":      #A means yes here 
        x = input("\nCustomer code (BD, D, W): \n")
        
        while not (x == 'BD' or x == 'D' or x == 'W'):#customer code check
            print("\n\t*** Invalid customer code. Try again. ***")
            x = input("\nCustomer code (BD, D, W): \n")
            
        num_of_days = int(input("\nNumber of days: \n"))
        odomet_start = int(input("Odometer reading at the start: \n"))
        odomet_end = int(input("Odometer reading at the end:   \n"))
        
        
        
        
        if x == 'BD':       #Type 1: Budget rentals.
            BASE_CHARGE_DAILY = 40.00
            MILEAGE_CHARGE = 0.25
            
            if odomet_end > odomet_start:  
                #Comparing odometer start and end values to determine the 
                #method of calculation of number of miles
                num_of_miles = (odomet_end - odomet_start)/10    
            elif odomet_end < odomet_start:
                num_of_miles = ((1000000 - odomet_start) + odomet_end)/10
            
            amount_due = (BASE_CHARGE_DAILY * num_of_days) + \
                (MILEAGE_CHARGE * num_of_miles)
            
            
            
            
        elif x == 'D':       #Type 2: Daily rentals 
            BASE_CHARGE_DAILY = 60.00
            MILEAGE_CHARGE = 0.25
            
            if odomet_end > odomet_start: 
                #Comparing odometer start and end values to determine the 
                #method of calculation of number of miles
                num_of_miles = (odomet_end - odomet_start)/10
            elif odomet_end < odomet_start:
                num_of_miles = ((1000000 - odomet_start) + odomet_end)/10
                
                
            avg_num_of_miles = num_of_miles/num_of_days
            
            
            if avg_num_of_miles <= 100:
                amount_due = (BASE_CHARGE_DAILY * num_of_days)
                
            elif avg_num_of_miles > 100:
                amount_due = (BASE_CHARGE_DAILY * num_of_days) + \
                    (MILEAGE_CHARGE * (num_of_miles - (num_of_days*100)))
                
                
                
                
        elif x == 'W':     #Type 3: Weekly Rentals
            BASE_CHARGE_WEEKLY = 190.00
            MILEAGE_CHARGE = 0.25
            
            if odomet_end > odomet_start:
                #Comparing odometer start and end values to determine the 
                #method of calculation of number of miles
                num_of_miles = (odomet_end - odomet_start)/10 
            elif odomet_end < odomet_start:
                num_of_miles = ((1000000 - odomet_start) + odomet_end)/10
                
                
            weeks = math.ceil (num_of_days/7)  #ceil() rounds the no of 
                                               #weeks to next higher integer
                                               
            avg_miles_weekly = num_of_miles / weeks #calculating the average 
                                                    #number of miles per week
                                               
            
            if avg_miles_weekly <= 900:        
                #we have different formulae for different ranges of avg miles 
                #to calculate amount
                amount_due = BASE_CHARGE_WEEKLY * weeks
                
            elif avg_miles_weekly > 900 and avg_miles_weekly <= 1500:   
                amount_due = (BASE_CHARGE_WEEKLY * weeks) + (100.00 * weeks)
                
            elif avg_miles_weekly > 1500:
                amount_due = (BASE_CHARGE_WEEKLY + 200.00) * weeks + \
                    ((avg_miles_weekly - 1500) * MILEAGE_CHARGE * weeks)
            
            
        print("\nCustomer summary:")   #Printing the customary summary details 
        print("\tclassification code:", x)
        print("\trental period (days):", num_of_days)
        print("\todometer reading at start:", odomet_start)
        print("\todometer reading at end:  ", odomet_end)
        print("\tnumber of miles driven: ", num_of_miles)
        print("\tamount due: $", amount_due)
            
        
    elif prompt == "B":    #B means no here 
        print("Thank you for your loyalty.")
        break             #the loop ends and program stops