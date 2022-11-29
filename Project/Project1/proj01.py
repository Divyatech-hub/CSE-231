###################################################################
#  CSE 231 Project #1

#  Algorithm
#    prompt user for number of rods as string
#    convert rods to float
#    display inputted rods number
#    convert rods to meters, round to 3 places, and print
#    convert rods to feet, round to 3 places, and print
#    convert rods to miles, round to 3 places, and print
#    convert rods to furlongs, round to 3 places, and print
#    convert rods to minutes to walk, round to 3 places, and print
#
###################################################################

#Constant for the program
METERS_PER_ROD = 5.0292
RODS_PER_FEET = 0.06060606
RODS_PER_MILE = 319.999
RODS_PER_FURLONG = 40


rods_str = input("Input rods: \n")        #user inputs rods as string
rods_flt = float(rods_str)                #convert rods as a float number
print("You input", rods_flt,"rods.\n")


print("Conversions")


meters = rods_flt * METERS_PER_ROD        #calculating meters from rods
print("Meters:", round(meters, 3))


feet = rods_flt / RODS_PER_FEET          #calculating feet from rods
print("Feet:", round(feet, 3))


miles = rods_flt / RODS_PER_MILE         #calculating miles from rods
print("Miles:", round(miles, 3))


furlongs = rods_flt / RODS_PER_FURLONG   #calculating furlongs from rods 
print("Furlongs:", round(furlongs, 3))


minutes_to_walk = rods_flt/ (3.1 * RODS_PER_MILE / 60)  #calculate minutes
print("Minutes to walk", rods_flt, "rods:", round(minutes_to_walk, 3))

