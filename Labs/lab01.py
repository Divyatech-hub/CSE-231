#Laboratory Exercise #1
# Team 2: Divyalakshmi, Arnav, Jathin, Aino
# Purpose:  compute the two roots of a quadratic equation.
#
# Import the math module to access function "math.sqrt()"
import math


# **** Do not change the statement below ****

A = float( input( "\nEnter the coefficient A: \n" ) ) 

B = float( input( "\nEnter the coefficient B: \n" ) ) 

C = float( input( "\nEnter the coefficient C: \n" ) ) 

print( "\nThe coefficients of the equation:\n" ) 
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )


# **** Replace the following with the calculations of the roots ****

root1 = (-B + math.sqrt((B**2)- 4*A*C))/(2*A)
root2 = (-B - math.sqrt((B**2)- 4*A*C))/(2*A)


print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", round(root1,3) )  # round the result to three decimal places before printing
print( "  Root #2 = ", round(root2,3) )
