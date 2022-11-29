###############################################################################
#  CSE 231 Project #5
#
#  Algorithm
#    import math module
#    declare constants with given value
#    define function open_file for trying to open required csv file in read  
#    mode. If file not found print error message and reprompt for file name.
#    
#    define function make_float() that tries to convert string to float and 
#    return it, if not returns -1. 
#    
#    define function get_density() that takes in planet mass and planet radius
#    and calculates density using density of sphere formula, returns it.
#
#    define function temp_in_range() that takes in certain parameters - axis,
#    star_radius, star_temp, albedo, low_bound, upp_bound and check if the 
#    planet is habitable or not by returning True or False accordingly. 
#
#    define get_distance_range() function that prompts user for max distance. 
#    If that distance is lesser than 0 or cannot be converted to float, 
#    print error message and reprompt.
#
#    define main() function
#        print welcome message
#        call open_file() to open respective file in read mode
#        get the max distance as float value by dividing returned value of 
#        get_distance_range() by constant PARSEC_LY
#        initialize the required variables for the program
#        read through first line of file using readline() (skipping headers)
#        main for loop parsing through each line of file
#            retrieve distance of planet from file data using string slicing
#            call make_float() function to convert distance
#            if distance_conv is not -1 i.e. conversion to float was 
#            successful
#                if distance_conv > 0 also distance_conv < max_distance 
#                calculated
#                    extract planet_name, axis, star_temp, star_radius, 
#                    num_of_stars, num_of_planets, plan_radius, plan_mass from
#                    the file. Convert num_of_planets and num_of_stars to int,
#                    all variables except planet_name to float by calling 
#                    make_float() function. 
#                    if num_of_stars in current iteration > max_stars
#                        then max_stars = num_of_stars
#                    if num_of_planets in current iteration > max_planets
#                        then max_planets = num_of_planets 
#                    if current planet's mass is positive
#                        increment total planet mass by current planet's mass
#                        increment counter by 1 
#                    call get_density() function to calculate planet density
#                    for the current planet 
#                    call temp_in_range function to check if planet is 
#                    habitable, if returns True
#                        increment habitable planets variable by 1
#                        if plan_mass between 0 and 10 or plan_radius between 
#                        0 and 1.5 or plan_density > 2000 (checking if rocky or
#                        gaseous planet)
#                            if closest rocky planet's distance > distance_conv
#                                increment rocky planet counter by 1
#                                set closestrocky planet dist = distance_conv 
#                                closest_rocky_name = planet_name  
#                        else
#                            if closest gaseous planet distance > distance_conv
#                                increment gaseous planet counter by 1
#                                set closestgaseous planet dist = distance_conv 
#                                closest_gaseous_name = planet_name  
#                else
#                    continue
#        close the file_pointer
#        print the number of stars in system with most stars
#        print the number of planets in system with most planets 
#        print the average mass of all planets in the file in terms of Earth 
#        masses
#        print the number planets in habitable zone
#
#        if rocky planet counter > 0
#            print the name and distance of closest rocky planet
#        else
#            print message saying no rocky planets 
#        if gaseous planet counter > 0
#            print the name and distance of closest gaseous planet
#        else
#            print message saying no gaseous planets 
#
#    call main() function
#    end of the program
#              
###############################################################################

import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

def open_file(): 
    ''' Function to open a csv file containing the required data. 
    Parameters: None 
    Returns: file_pointer
    Displays: prompt and error message accordingly'''
    
    file_name = input("Input data to open: ")
    while True:
        try:
            file_name += '.csv' #adding .csv to name of file inputted
            file_pointer = open(file_name, 'r') #opening file in read mode
            break
        
        except FileNotFoundError: 
            #if invalide filename inputted, exception is raised
            print("\nError: file not found.  Please try again.") 
            file_name = input("Enter a file name: ")
            continue
    return file_pointer
    


def make_float(s):  
    ''' Function to covert string to float, if possible. If not return -1.
    Parameters: string s
    Returns: float or -1
    Displays: Nothing'''
    try: 
        s_flt = float(s)  
        return s_flt      #return float value of s
        
    except ValueError:
        return -1  #if float conversion not successful, return -1
           
    
    
def get_density(mass, radius): 
    ''' Function that takes mass and radius of a spherical object in terms of 
    Earth units and returns the density. The parameters mass and radius must
    be converted to metric using the provided constants. Returns -1 if 
    parameters are negative or radius is zero.
    Parameters: float, float
    Returns: float or -1
    Display: nothing '''
    
    global EARTH_MASS
    global EARTH_RADIUS
    
    if mass < 0 or radius < 0 or radius == 0: 
        #checking if inputted values are valid for density calculation
        return -1  
    
    else:
        metric_mass = mass * EARTH_MASS  #conversion to metric units 
        metric_radius = radius * EARTH_RADIUS  #conversion to metric units 
        
        volume =(4*PI*(metric_radius)**3) / 3 
        density = metric_mass / volume 
        
        return density    #function returns density calculated for the planet


def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound): 
    '''This function returns True if we estimate that the planet’s temperature
    is within a range that might support life as we know it; False otherwise.
    Make sure to convert to metric units before applying this formula.
    Parameters: float, float, float, float, float 
    Returns: bool 
    Displays: nothing '''
    
    global SOLAR_RADIUS
    global AU
    
    if axis<0 or star_temp<0 or star_radius<0 or albedo<0 or low_bound<0 or\
        upp_bound<0:
        #if any of the parameters are negative, return False
        return False
    
    else:
        met_star_rad = star_radius * SOLAR_RADIUS #conversion to metric units 
        met_axis = axis * AU   #conversion to metric units 
        
        planet_temp = star_temp*(met_star_rad/(2*met_axis))**(0.5)\
            *(1-albedo)**(0.25)  #formula to calculate planet's temperature
    
        if planet_temp >= low_bound and planet_temp <= upp_bound:
            return True    #if planet's temp within bounds, return True
    
        else:
            return False
        
    

def get_dist_range(): 
    ''' Function asking user for farthest distance from Earth to filter the 
    data. Prompt for a distance.  If the distance is less than zero or cannot
    be converted to a float, print an error message and re-prompt.
    Parameter: nothing
    Returns: float 
    Displays: prompt and possibly an error message 
    '''
    
    while True: 
        max_dis = input("\nEnter maximum distance from Earth (light years): ")
        try:    
            #trying to convert max_dis to float
            max_dis_flt = float(max_dis)
            if max_dis_flt > 0:   #a valid distance is positive. 
                return max_dis_flt
                
            elif max_dis_flt < 0: #invalid distance inputted show error message
                print("\nError: Distance needs to be greater than 0.")
                continue   #reprompt the input message for user
        
        except ValueError:
            #if unable to convert to float, show error message
            print("\nError: Distance needs to be a float." )
            continue #reprompt the input message for user
                
 

def main():            
    '''Inside this function we have the whole program code wherein functions 
    are called and inputs and outputs are present.
    No arguments passed
    No values returned but they are printed according to condition satisfaction
    '''
    
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''') 
    file_pointer = open_file()  #calling function to read specified file
    max_dist_flt = get_dist_range() / PARSEC_LY  #
    
    low_bound = 200
    upp_bound = 350
    albedo = 0.5
    
    file_pointer.readline()  #reading the first line of the file (skips header)
    
    max_planets = -1 
    max_stars = - 1
    tot_plan_mass = 0  #total accumulated mass of all planets in the file
    closest_rocky = 100000000  #the distance of closest rocky planet
    closest_gaseous = 100000000 #the distance of closest gaseous planet
    counter = 0    #a variable keeping track of number of planets 
    habitable_planets = 0  #variable for number of habitable planets 
                           #that have the right temp within the habitable range
    rocky_count = 0  #variable counting number of rocky planets
    gaseous_count = 0 #variable counting number of gaseous planets 
    
    for line in file_pointer: #parsing through each line of file 
        distance = line[114:] #extracting planet distance using atring slicing
        distance_conv = make_float(distance) #float conversion 
        if distance_conv != -1:  
            #if float conversion was successful for distance
            if distance_conv >= 0 and distance_conv <= max_dist_flt:
                planet_name = line[:25]
                axis = make_float(line[66:77])
                star_temp = make_float(line[97:105])
                star_radius = make_float(line[106: 113])
                num_of_stars = int(line[50:57])
                num_of_planets = int(line[58:65])
                plan_radius = make_float(line[78:85])
                plan_mass = make_float(line[86:96])
                
                #using high level maximum algorithm for finding max_stars
                if num_of_stars > max_stars: 
                    max_stars = num_of_stars
                    
                #using high level maximum algorithm for finding max_planets
                if num_of_planets > max_planets:
                    max_planets = num_of_planets
                    
                if plan_mass > 0:  #if planet mass is positive.ie. valid mass
                    tot_plan_mass += plan_mass#increment total planet mass by 1 
                    counter += 1  #increment number of planets by 1
                    
                plan_density = get_density(plan_mass, plan_radius)
                
                if temp_in_range(axis, star_temp, star_radius, albedo,\
                                 low_bound, upp_bound) == True:
                    #if the planet temp is within low and upper bounds, then it
                    #is a habitable planet. 
                    habitable_planets += 1
                    if (plan_mass > 0 and \
                        plan_mass < 10) or (plan_radius > 0 and plan_radius\
                                            < 1.5) or (plan_density > 2000):
                        #if above conditions are satisfied, planet is rocky
                        if closest_rocky > distance_conv:
                            #comparing value of closest_rocky with 
                            #distance_conv to identify closest rocky planet
                            rocky_count += 1
                            closest_rocky = distance_conv
                            closest_rocky_name = planet_name
                            
                    else:
                        #otherwise, planet is gaseous
                        if closest_gaseous > distance_conv:
                            #comparing value of closest_gaseous with 
                            #distance_conv to identify closest gaseous planet 
                            gaseous_count += 1
                            closest_gaseous = distance_conv
                            closest_gaseous_name = planet_name
                
            else:
                #if float conversion wasn't successful for distance, skip that
                #line of the file 
                continue
    file_pointer.close()  #closing file object
    
    print("\nNumber of stars in systems with the most stars: {:d}.".format\
          (max_stars))
    print("Number of planets in systems with the most planets: {:d}.".format\
          (max_planets))
    print("Average mass of the planets: {:.2f} Earth masses.".\
          format(tot_plan_mass/counter))
    print("Number of planets in circumstellar habitable zone: {:d}.".format\
          (habitable_planets))
    
        
    if rocky_count > 0:  
        #if there was rocky planet found within specified zone of space
        #converting distance of closest rocky to PARSECS from Light Years
        print("Closest rocky planet in the circumstellar habitable zone {}"\
              " is {:.2f} light years away.".format(closest_rocky_name.strip()\
                                                    , closest_rocky*PARSEC_LY))
    else:
        print("No rocky planet in circumstellar habitable zone.")
    
    if gaseous_count > 0:
        #if there was gaseous planet found within specified zone of space
        #converting distance of closest gaseous to PARSECS from Light Years
        print("Closest gaseous planet in the circumstellar habitable "\
              "zone {} is {:.2f} light years away.".\
                  format(closest_gaseous_name.strip()\
                         , closest_gaseous*PARSEC_LY))
    else:
        print("No gaseous planet in circumstellar habitable zone.")

    
      
if __name__ == "__main__":  #calling the main function to execute program. 
    main()
