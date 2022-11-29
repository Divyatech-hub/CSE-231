###############################################################################
#  CSE 231 Project #4

#  Algorithm
#    import math module
#    declare EPSILON as a constant with given value
#
#    define factorial() function such that when inputted a string N if int(N)  
#    is non-negative integer, then loop, calculate and return N!, else return 
#    None value
#
#    define e() function that calculates and returns value of constant e using  
#    formula and EPSILON-based approximations rounded to 10 places
#
#    define pi() function that calculates and returns value of constant pi   
#    using formula and EPSILON-based approximations rounded to 10 places
#
#    define sinh() function that takes in x as input in radians, tries to 
#    convert to float(x) and calculates hyperbolic sine using formula and 
#    EPSILON-based approximations rounded to 10 places
#
#    define main() function
#         print MENU for user
#         main while loop 
#         ask user for option as input ('F' or 'E' or 'P' or 'S' or 'M' or 'X') 
#         if option equals 'F'
#             print message 'Factorial'
#             input a non-negative integer N in form of string
#             call factorial(N) function and store returned value to variable
#             calc_ed
#             if calc_ed is not None
#                 calculate factorial of N using math module function 
#                 factorial(x) and store in math_fact, and print it
#                 find absolute value of difference of math_fact and calc_ed, 
#                 and print it
#             else if calc_ed is None
#                 print invalid N error message
#
#         elif option equals 'E'
#             print message 'e'
#             call e() function and store returned value to variable calc_ed
#             find e using math module constant math.e, round to 10 places, 
#             store in math_e, and print 
#             find absolute value of difference of math_e and calc_ed, print it
#             
#         elif option equals 'P'
#             print message 'pi'
#             call pi() function and store returned value to variable calc_ed
#             find pi using math module constant math.pi, round to 10 places, 
#             store in math_pi, and print 
#             find absolute value of difference of math_pi and calc_ed, print 
#
#         elif option equals 'S'
#             print message 'sinh'
#             input x in form of radians as a string
#             call sinh(x) function and store returned value to variable
#             calc_ed
#             if calc_ed is not None
#                 calculate sinh(x) using math module function math.sinh(x), 
#                 round to 10 places, store in math_sinh, and print it
#                 find absolute value of difference of math_sinh and calc_ed, 
#                 and print it
#             else if calc_ed is None
#                 print invalid x error message
#
#         elif option equals 'M'
#             print MENU 
#
#         elif option equals 'X
#             print thank you message
#             end program
#
#         else
#            invalid option inputted error message
#            print MENU
#
#    call main() function 
###############################################################################

import math
EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(N): 
    ''' Function to calculate the factorial when a string containing digit is
    inputted.
    input value: string
    returns: int or None ''' 
    if N.isdigit():      #checking if N string has only digits in it
        N_int = int(N)
    
        if N_int > 0:    #if int(N) is positive integer 
            factorial_N = 1   #counter var keeping track of factorial product
            for i in range(1, N_int+1):
                factorial_N = factorial_N * i
            return factorial_N
            
        elif N_int == 0:   #we defined 0! equals 1
            factorial_N = 1
            return factorial_N
        
        elif N_int <= 0:  #if int(N) is negative integer
            return None   #factorial doesn't exist for negative integers 
        
    else:           #check to see if N string has other characters than digits 
        return None
        
    
    
 
def e(): 
    ''' This function takes no arguments and returns an approximate value 
    of e. 
    input value: no arguments
    returns: float rounded to 10 places''' 
    EPSILON = 0.0000001   #constant to avoid an infinite addition series
    e = 0                 #initializing constant e we want to calculate 
    i = 0                 #counter var for while loop
    while True:
        next_term = 1/ math.factorial(i) #formula to find next term of series
        
        if math.fabs(next_term) > EPSILON: 
            #check to see if to add next term to e sum or not
            e += next_term
            i += 1
            
        elif math.fabs(next_term) < EPSILON:
            #if less than, then ignore that and subsequent terms
            break
    
    return round(e, 10)  #return rounded value of e to 10 decimal places 


        

def pi():
    ''' This function takes no arguments and returns an approximate value 
    of constant pi. 
    input value: no arguments
    returns: float rounded to 10 places''' 
    EPSILON = 0.0000001     #constant to avoid an infinite addition series
    pi_sum = 0              #initializing constant pi we want to calculate
    i = 0                   #counter var for while loop
    while True:
        next_term = ((-1)**(i)) / (2*i + 1)#formula to find next term of series
        
        if math.fabs(next_term) > EPSILON:
            #check to see if to add next term to pi sum or not
            pi_sum += next_term
            i += 1
            
        elif math.fabs(next_term) < EPSILON:
            #if less than, then ignore that and subsequent terms
            break
        
    final_pi = pi_sum * 4 #multiply previous pi sum by 4 according to formula
    return round(final_pi, 10) #return rounded value of pi to 10 decimal places 




def sinh(x): 
    ''' This function accepts as input a numeric value X (measured in radians)
    as a string and returns the approximate value of the hyperbolic sine 
    of X. 
    input value: string
    returns: float rounded to 10 places or None''' 
    try:       #trying to convert x from string to float
        x_flt = float(x)
        EPSILON = 0.0000001  #constant to avoid an infinite addition series
        sinh_sum = 0         #initializing constant sinh we want to calculate
        i = 0                #counter var for while loop
        while True:
            #formula to find next term of series
            next_term = (x_flt**(2*i + 1)) / math.factorial(2*i + 1)
            
            if math.fabs(next_term) > EPSILON:
                #check to see if to add next term to sinh sum or not
                sinh_sum += next_term
                i += 1
                
            elif math.fabs(next_term) < EPSILON:
                #if less than, then ignore that and subsequent terms
                break
        return round(sinh_sum, 10)#return rounded value of sinh to 10 places
        

    except ValueError:  #if encounter ValueError exception, return None
        return None
        
    

def main(): 
    '''Inside this function we have the whole program code wherein functions 
    are called and inputs and outputs are present.
    No arguments passed
    No values returned but they are printed according to condition satisfaction
    '''
    print(MENU) 
    while True:  #main while loop for program
        opt = input("\nChoose an option: ") #ask user for option input
        
        if opt.upper() == 'F':
            print("\nFactorial")
            N = input("Input non-negative integer N: ")
            calc_ed = factorial(N)   #calling defined factorial() function 
            
            if calc_ed != None:  #if function doesn't return None
                #comparing factorial value calculated by defined function and
                #factorial function in math module
                math_fact = math.factorial(int(N))
                diff = math.fabs(math_fact - calc_ed) #absolute value of diff.
                print("\nCalculated:", calc_ed)
                print("Math:", math_fact)
                print("Diff:", int(diff))
            else:
                print("\nInvalid N.")
                
              

        elif opt.upper() == 'E':
            print("\ne")
            calc_ed = e()   #calling defined e() function
            #comparing e value calculated by defined function and e constant
            #in math module
            math_e = round(math.e, 10)
            diff = calc_ed - math_e
            diff = math.fabs(diff)
            
            print("Calculated:", calc_ed)
            print("Math:", math_e)
            print("Diff: {:.10f}".format(diff))
                        
            
            
        elif opt.upper() == 'P':
            print("\npi")
            calc_ed = pi()   #calling defined pi() function
            #comparing pi value calculated by defined function and pi constant 
            #in math module
            math_pi = round(math.pi, 10)
            diff = calc_ed - math_pi
            diff = math.fabs(diff)
            
            print("Calculated:", calc_ed)
            print("Math:", math_pi)
            print("Diff: {:.10f}".format(diff))
            

            
        elif opt.upper() == 'S':
            print("\nsinh")
            x = input("X in radians: ")
            calc_ed = sinh(x)   #calling defined sinh() function
            
            if calc_ed != None:  #if function doesn't return None
                    #comparing sinh value calculated by defined function and
                    #sinh function in math module
                math_sinh = round(math.sinh(float(x)), 10)
                diff = math.fabs(math_sinh - calc_ed)  #absolute value of diff.
                print("\nCalculated:", calc_ed)
                print("Math:", math_sinh)
                print("Diff: {:.10f}".format(diff))  
            else:
                print("\nInvalid X.")
            


        elif opt.upper() == 'M':
            #option to reprint menu
            print(MENU)  
            
        elif opt.upper() == 'X':
            #option to quit loop
            print("\nThank you for playing.")  
            break
        
        else:
            #if any other option inputted, invalid message and menu printed
            print("\nInvalid option:", opt.upper())
            print(MENU)



# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()
