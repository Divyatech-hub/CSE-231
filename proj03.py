###############################################################################
#  CSE 231 Project #3
#
#  Algorithm
#    display the triangle banner
#    declare a num_of_triangle variable 
#    ask user if they want to process a triangle (Y/N)
#    main while loop
#         if user input is 'Y' or 'y'
#              ask user to input the sides of the triangle as a,b,c
#              if sum of any two sides is greater than the third side
#                   then print message 'Valid Triangle'
#                   display the sides of the triangle
#                   increment num_of_triangle variable by 1
#                   calculate the values of interior angles of triangle A, B, C 
#                   using law of cosines formula in radians and degrees 
#                   output angles in radians after rounding to 1 decimal place
#                   output angles in degrees after rounding to 1 decimal place
#                   add all side lengths to find perimeter and display after 
#                   rounding to 1 decimal place
#                   find the semi perimeter of triangle
#                   calculate area of triangle using herons formula and output
#                   after rounding to 1 decimal place
#                   based on conditions, output type(s) of triangle - scalene,
#                   isosceles, equilateral, obtuse, oblique, right 
#                   prompt user if want to process another triangle
#                         if 'Y' or 'y', then repeat the above steps
#                         else if anything else, output the number of valid 
#                         triangle till now
#                         end program
#
#              if sum of any two sides is equal to the third side
#                         then print message 'Degenerate Triangle'
#                         prompt user if want to process another triangle
#                         if 'Y' or 'y', then repeat the above steps
#                         else if anything else, output the number of valid 
#                         triangle till now
#                         end program
#              if sum of any two sides is lesser than the third side
#                         then print message 'Not a Triangle'
#                         prompt user if want to process another triangle
#                         if 'Y' or 'y', then repeat the above steps
#                         else if anything else, output the number of valid 
#                         triangle till now
#                         end program
#         else if anything else is inputed, output number of valid triangles
#         till now
#         end program
#        
###############################################################################

import math                   #importing math module 
DEG_MULTIPLIER = 180/math.pi  #Constant to convert angles in radians to degrees

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()

num_of_valid_tri = 0    #counter variable to track no. of valid triangles
user_inp= input("Do you wish to process a triangle (Y or N)?  ")

while True:     #main while loop
    if user_inp == 'Y' or user_inp == 'y':  
        c = int(input('\nEnter length of side AB: ')) #sides of the triangle
        a = int(input('\nEnter length of side BC: '))
        b = int(input('\nEnter length of side CA: '))
        
        if (a + b) > c and (b + c) > a and (c + a) > b: 
            #Inequality property to check if triangle is valid triangle or not
            print("\n\n  Valid Triangle")
            print("\n  Triangle sides:")
            print("    Length of side AB:", float(c))
            print("    Length of side BC:", float(a))
            print("    Length of side CA:", float(b))
            
            num_of_valid_tri += 1    #increment variable by 1
            
            #finding the value of interior angles in radians by law of cosines
            angleA_rad = math.acos((b**2 + c**2 - a**2)/ (2*b*c))
            angleB_rad = math.acos((a**2 + c**2 - b**2)/ (2*a*c))
            angleC_rad = math.acos((a**2 + b**2 - c**2)/ (2*a*b))
            
            #converting interior angles to degrees
            angleA_deg = angleA_rad * DEG_MULTIPLIER
            angleB_deg = angleB_rad * DEG_MULTIPLIER
            angleC_deg = angleC_rad * DEG_MULTIPLIER
            
            print("\n  Degree measure of interior angles:")
            print("    Angle A:", round(angleA_deg, 1))
            print("    Angle B:", round(angleB_deg, 1))
            print("    Angle C:", round(angleC_deg, 1))
            
            print("\n  Radian measure of interior angles:")
            print("    Angle A:", round(angleA_rad, 1))
            print("    Angle B:", round(angleB_rad, 1))
            print("    Angle C:", round(angleC_rad, 1))
            
            #sum of all sides to get perimeter of triangle
            perimeter = float(a + b + c)
            print("\n  Perimeter and Area of triangle:")
            print("    Perimeter of triangle:", round(perimeter, 1))
            
            #perimeter divided by 2 gives us semi perimeter for using 
            #the Heron's formula
            s_perimeter = perimeter/2
            
            #apply heron's formula to find area of triangle
            area = math.sqrt(s_perimeter*(s_perimeter-a)*(s_perimeter-b)*\
                             (s_perimeter-c))
            print("    Area of triangle:", round(area, 1))
            
            
            #Determining the type(s) for the triangle
            print("\n  Types of triangle:")
            if a != b and b != c and c != a:
                print("    Scalene Triangle")
                
            if (a == b) or (b == c) or (a == c):
                print("    Isosceles Triangle")
                
            if a == b == c:
                print("    Equilateral Triangle")
                
            if not (angleA_deg == 90.0 or angleB_deg == 90.0 or angleC_deg == \
                    90.0):
                print("    Oblique Triangle")
                
            if (angleA_deg == 90.0 or angleB_deg == 90.0 or angleC_deg == \
                90.0):
                print("    Right Triangle")
                
            if (angleA_deg > 90.0 or angleB_deg > 90.0 or angleC_deg > 90.0):
                print("    Obtuse Triangle")
                
                
            user_inp = input("\nDo you wish to process another triangle?" + \
                             " (Y or N) ")
            if user_inp == 'Y' or user_inp == 'y':
                continue
            elif user_inp != 'Y' or user_inp != 'y':
                print("\nNumber of valid triangles:", num_of_valid_tri)
                break  #the loop ends here
        
                            
            
        elif (a + b) == c or (b + c) == a or (c + a) == b:
            #Condition to check if it's a degenerate triangle or not
            print("\n\n  Degenerate Triangle")
            user_inp = input("\nDo you wish to process another triangle?"+\
                             " (Y or N) ")
            if user_inp == 'Y' or user_inp == 'y':
                continue
            elif user_inp != 'Y' or user_inp != 'y':
                print("\nNumber of valid triangles:", num_of_valid_tri)
                break   # loops ends here
            
            
            
        elif (a + b) < c or (b + c) < a or (c + a) < b:
            #Condition to check if it's not a triangle
            print("\n\n  Not a Triangle")
            user_inp = input("\nDo you wish to process another triangle?"+\
                             " (Y or N) ")
            if user_inp == 'Y' or user_inp == 'y':
                continue
            elif user_inp != 'Y' or user_inp != 'y':
                print("\nNumber of valid triangles:", num_of_valid_tri)
                break   #the loop ends here
                
                
            
    elif user_inp != 'Y' or user_inp != 'y':  #if anything else is inputed
        #display the no. of valid triangles till that point
        print("\nNumber of valid triangles:", num_of_valid_tri)
        break #loop ends here
            
            
        
