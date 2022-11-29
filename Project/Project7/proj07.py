###############################################################################
#  CSE 231 Project #6
#  Algorithm
#    declare constants with given value
#    define open_file(s) function that keeps repromting until a valid file name
#    is entered. It takes in a parameter s which specifies what type of file
#    to be inputted.
#  
#    define read_reviews() that reads the reviews.txt file and generates a list
#    of lists of sorted tuples with information related to reviewer: movie_ID 
#    and the rating.
#
#    define read_users() that reads the user.txt file using file pointer fp and
#    returns a list of tuples. The data in file isseparated by vertical bars 
#    (‘|’).
#
#    define read_movies() that reads the movies.txt file using parameter fp, &
#    generates and returns a list of tuples each with info (title, date, 
#    [list of genres]).
#
#    define year_movies() that filters the main movie list returned by the 
#    read_movies()) to find movies for a specific year and returns their 
#    corresponding movieIDs as a sorted list in ascending order.
#
#    define genre_movies() that filters the main movie list to find movies 
#    of a particular genre, returns their movieIDs as a list. 
#
#    define gen_users() that filters the main reviews list to find reviews for  
#    specific gender of users and finds the users in L_users of the specified 
#    gender. Then it takes user’s index to index into the L_reviews to extract
#    their reviews. Returns a list of the reviews. 
#
#    define occu_users() that filters the main reviews list to find records for
#    specific occupational group of users, then returns them as a list of lists
#    of tuples.  
#
#    define highest_rated_by_movie() that calculates average rating for reviews
#    in L_reviews list of the movies in L_in list, then returns list of highest
#    average rated movies and the highest average value.
#
#    define highest_rated_by_reviewers() that calculates average rating for all
#    movies by a specific group of users (L_in), then returns a list of the 
#    highest average rated movies and the highest average value.
#
#    define main() function
#    call open_file(s) with s as 'users' and store it as fp1
#    call open_file(s) with s as 'reviews' and store it as fp2
#    call open_file(s) with s as 'movies' and store it as fp3
#    call read_users(fp1) and assign it to L_users
#    call read_reviews(fp2) and assign it to L_reviews
#    call read_movies(fp3) and assign it to L_movies
#    close all the three files using the respective file pointers
#    display the option MENU
#    main while loop
#        prompt user for an input option between 1 and 5
#        if opt is 1
#           ask user to input a year 
#           if year is an int
#              if year is between 1930 and 1998 (not included)
#                 call year_movies() and assign it to movieIDs_list
#                 call highest_rated_by_movie and assign its values to 
#                 max_avg_movies and max_avg, print the average value, print 
#                 name of each of those movies whose movieIDs are present in 
#                 max_avg_movies one on each line.
#              else if year is not an int or not in given range, print error 
#              message and reprompt
#
#        elif opt is 2
#           display all the valid genres possible using GENRES
#           ask user to input a genre
#           if genre.capitalize() is in GENRES list
#               call genre_movies() and assign it to movieIDs_list
#               call highest_rated_by_movie and assign its values to 
#               max_avg_movies and max_avg, print the average value, print 
#               name of each of those movies whose movieIDs are present in 
#               max_avg_movies one on each line.
#           else if genre is not valid input, print error message & reprompt
#
#        elif opt is 3
#           ask user to input a gender 
#           if gender in ('M', 'm, 'F', 'f')
#              call gen_users() and assign it to movieIDs_list
#              call highest_rated_by_movie and assign its values to 
#              max_avg_movies and max_avg, print the average value, print 
#              name of each of those movies whose movieIDs are present in 
#              max_avg_movies one on each line.
#           else if gender is not valid input, print error message & reprompt
#
#        elif opt is 4
#           display all the valid occupations possible using OCCUPATIONS
#           ask user to input an occupation
#           if occupation is in OCCUPATIONS list
#               call occu_users() and assign it to movieIDs_list
#               call highest_rated_by_movie and assign its values to 
#               max_avg_movies and max_avg, print the average value, print 
#               name of each of those movies whose movieIDs are present in 
#               max_avg_movies one on each line.
#           else if occupation is not valid input, print error message,reprompt
#
#        elif opt is 5
#           break
#  call main() function
#  end of program    

###############################################################################

GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 
               'lawyer', 'librarian', 'marketing', 'none', 'other', 
               'programmer', 'retired', 'salesman', 'scientist', 'student', 
               'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of 
                                              genres)
'''

MENU = '''                
        Options:           
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
        
def open_file(s):
    ''' This function prompts user to input file name to open and keeps 
    prompting until valid name is given.  s is a parameter, that tells
    the user what kind of file is being prompted for. s can be ("user",
    "review","movie"). 
    Parameters: string
    Returns: a file pointer
    Display: prompts and error messages '''
    
    while True:
        try:
            file_name = input('\nInput {} filename: '.format(s))
            fp = open(file_name,"r",encoding ="windows-1252")    
            break
        except FileNotFoundError: 
            #if invalide filename inputted, exception is raised
            print('\nError: No such file; please try again.') 
            continue
    return fp   #returning file pointer 
    


def read_reviews(N,fp):
    '''This function reads the reviews.txt file using the file pointer fp. 
    The file has no header. N, an int, is the number of users. It generates a 
    list of lists of sorted tuples with information related to reviewer: 
    movie_ID and the rating.
    Parameter: a file pointer
    Returns: list of sorted lists of tuples of ints
    Display: nothing'''
    
    L_reviews = []  
    
    for i in range(N+1):  #creating a list of empty lists 
        empty_list = []
        L_reviews.append(empty_list)
        
    fp = fp.readlines()   #creating a list with each line of file as an string
    for line in fp:
        s_line = line.split('\t')
        user_ID = int(s_line[0])
        movie_ID = int(s_line[1])
        rating = int(s_line[2])
        reviewer_tup = (movie_ID, rating)
        L_reviews[user_ID].append(reviewer_tup)
        #each tuple corresponds to 1 reviewer
    
    for i in range(N+1):
        L_reviews[i].sort()
        
    return L_reviews  #returns a list of sorted lists of tuples of ints
        
    

def read_users(fp):
    '''This function reads the user.txt file using file pointer fp and returns 
    a list of tuples. The file has no header.  The data is separated by 
    vertical bars (‘|’). 
    Parameter: file pointer 
    Returns: list of tuples 
    Displays: nothing '''
    
    L_users = []
    index_zero = []
    L_users.append(index_zero)  #having an empty list at index 0 of L_users
    fp = fp.readlines()
    for line in fp:
        s_line = line.split('|') #splitting file data using by vertical bars
        reviewer_ID = int(s_line[0])
        age = int(s_line[1])   
        gender = s_line[2]
        occupation = s_line[3]
        #creating a tuple for every user with their demographics
        user_tup = (age, gender, occupation)
        L_users.append(user_tup) #appending users tuple to L_user list
    return L_users
    
        

def read_movies(fp):
    ''' This function reads the movies.txt file using the parameter fp. The 
    file has no header and items are separated by bars (‘|’). It generates and 
    returns a list of tuples each in the format
    (title, date, [list of genres]).
    Parameter: a file pointer
    Returns: list of lists
    Display: nothing '''
    global GENRES
    
    L_movies = []
    index_zero = []
    L_movies.append(index_zero) #having an empty list at index 0 of L_users
    fp = fp.readlines()
    for line in fp:
        s_line = line.split('|') #splitting file data using vertical bars
        #removing newline character from end of last element of s_line
        s_line[len(s_line)-1] = s_line[len(s_line)-1].strip("\n") 
        movie_ID = int(s_line[0])
        title = s_line[1]
        date = s_line[2]
        l_of_genres = []
        for i in range(5, len(s_line)): 
            if s_line[i] == '1':   
                #if the value for that genre is 1,then add it to list of genres
                genre = GENRES[i-5]
                l_of_genres.append(genre)
                
        movie_tup = (title, date, l_of_genres)
        L_movies.append(movie_tup)
    return L_movies
        
            

def year_movies(year, L_movies):
    '''This function filters the main movie list (returned by the read_movies
    function) to find movies for a specific year and returns their ids movieID
    (ints) as a sorted list in ascending order. 
    Paremeters: int, list of tuples
    Returns: sorted list of ints
    Display:  nothing '''
    movie_ID_list = []
    for i in range(1, len(L_movies)):
        date = L_movies[i][1]
        new_date = date[-4::] #extracting the year from the file using slicing
        if new_date == str(year): #check if year extracted equals parameter
             movie_ID_list.append(i) #add the movieID to list of movieIDs 
            
    movie_ID_list.sort() #sorting movieID list
    return movie_ID_list

        

def genre_movies(genre,L_movies):
    '''This function filters the main movie list to find movies for a specific 
    genre and returns their ids as a list. A movie can have multiple genres so 
    if any of the genres is the specified genre the movie would be selected. 
    Parameters: string, list of tuples
    Return : sorted list of ints
    Display: nothing '''
    
    movie_ID_list = [] 
    for i in range(1, len(L_movies)): 
        # looping from first index onwards as 0th index has empty list. 
        #check if genre is in main movie list. 
        if genre in L_movies[i][2]:
            movie_ID_list.append(i)
            
    movie_ID_list.sort()
    return movie_ID_list
    

def gen_users (gender, L_users, L_reviews):
    ''' This function filters the main reviews list to find reviews for a 
    specific gender of users and finds the users in L_users of the specified 
    gender then use the user’s number (index) to index into the L_reviews 
    to get their reviews. Return a list of the reviews. 
    Parameters: str, list of tuples, list of list of tuples
    Return: list of list of tuples
    Display: nothing '''
    
    review_list = []
    for i in range(1, len(L_users)):
        u_gender = L_users[i][1]
        if gender.upper() == u_gender: 
            #check if gender extracted matches parameter for gender passed
            req_index = i  #required index of the review
            review = L_reviews[req_index]
            review_list.append(review)
    return review_list
            
            
            
          
def occ_users (occupation, L_users, L_reviews):
    ''' This function filters the main reviews list to find records for a 
    specific occupational group of users and returns them as a list of lists
    of tuples.  
    Parameters: str, list of tuples, list of list of tuples 
    Return: list of list of tuples
    Display: nothing'''
    
    review_list = []
    for i in range(1, len(L_users)):  
        u_occupation = L_users[i][2]
        if occupation == u_occupation:
            #check if occupation extracted matches parameter for occupation
            req_index = i #required index of the review
            review = L_reviews[req_index]
            review_list.append(review)
    return review_list
            
    
    

def highest_rated_by_movie(L_in, L_reviews, N_movies):
    '''  This function calculates the average rating for the reviews in 
    L_reviews list of the movies in L_in list and returns a list of the highest
    average rated movies and the highest average.
    Parameters: list of ints, list of lists of tuples, int 
    Return: list of floats, float
    Display: nothing '''
    counting_List = [[0,0]] 
    #creating a list of lists to keep track of sum of ratings and count
    average_list = [0]  #creating a list of averages 
    
    for i in range(N_movies+1):  
        #iterating through to add nested lists to counting_List and zeros
        #to average_list N_movies+1 times to account for all values
            empty_list = [0, 0]
            counting_List.append(empty_list)
            average_list.append(0)
    
    for movieID in L_in:
        #re-initializing sum and counter to zero for every iteration
        summ = 0        
        counter = 0
        for i in range(1, len(L_reviews)):
            if L_reviews[i] == []:  #if it's empty list, skip it
                continue
            for review in L_reviews[i]:
                if review[0] == movieID:
                    #updating sum and counter where moveieID found in L_reviews
                    summ += review[1]    
                    counter += 1
                    counting_List.insert(movieID, [summ, counter])
                 
        average = round(summ/counter, 2)
        average_list.insert(movieID, average)

                
    max_avg = max(average_list)
    max_avg_movies = []
    
    for j in range(len(average_list)):
           if average_list[j] == max_avg:
               max_avg_movies.append(j)
               
    return max_avg_movies, max_avg
        
                     
        
    
    
def highest_rated_by_reviewer(L_in,N_movies):
    '''  This function calculates the average rating for all movies by a 
    specific group of users (L_in) and returns a list of the highest average 
    rated movies and the highest average.
    Parameters: list of list of tuples, int
    Return: list of floats, float
    Display: nothing'''
    
    counting_List = [[0,0]]
    #creating a list of lists to keep track of sum of ratings and count
    average_list = [0] #creating a list of averages 
    
    for i in range(N_movies+1):
        #iterating through to add nested lists to counting_List and zeros
        #to average_list N_movies+1 times to account for all values
        empty_list = [0, 0]
        counting_List.append(empty_list)
        average_list.append(0)
        
    try:
        
        for users in L_in:
            for review in users:
                movieID = review[0]
                counting_List[movieID][0] += review[1]
                counting_List[movieID][1] += 1
                average = round(counting_List[movieID][0]/\
                            counting_List[movieID][1], 2)
                average_list[movieID] = average
    
                    
        max_avg = max(average_list) #max of the average values generated
        max_avg_movies = []
        
        for j in range(len(average_list)):
                if average_list[j] == max_avg:
                    max_avg_movies.append(j)
                   
        return max_avg_movies, max_avg  
    except:
        pass


                
    
def main():
    '''
    Inside this function we have the whole program code wherein functions 
    are called and inputs and outputs are present.
    No arguments passed
    No values returned but they are printed according to condition satisfaction
    '''
    global MENU
    global GENRES
    global OCCUPATIONS
    
    fp1 = open_file('users')
    fp2 = open_file('reviews')
    fp3 = open_file('movies')
   
    L_users = read_users(fp1)   #generating the 3 master lists.
    L_movies = read_movies(fp3)
    L_reviews = read_reviews(len(L_movies), fp2)
    N = len(L_movies) 
    
    fp1.close()         #closing all the files
    fp2.close()
    fp3.close()
    
    print(MENU)
    while True:
        opt = int(input('\nSelect an option (1-5): '))
       
        if opt == 1:
            year = input('\nInput a year: ')
            for j in range(N): 
                    try:
                        year = int(year)  #check if year is an int
                        if year > 1930 and year < 1998: 
                            #if year in specified range of 1930 and 1998 
                            #(not inclusive), creating a list of movieIDs
                            #of movies released that year
                            moviesID_list = year_movies(year, L_movies)
                            
                            #finding max_avg values and list of movieIDs where
                            #max_avg value is found
                            max_avg_movies, max_avg = highest_rated_by_movie\
                                (moviesID_list, L_reviews, N)
                            print('\nAvg max rating for the year is:', max_avg)
                            for i in max_avg_movies:
                                print(L_movies[i][0])
                                
                            break
                                
                                
                        elif year < 1930 or year > 1998:
                            print("\nError in year.")
                            year = input('\nInput a year: ')
                            
                    except ValueError:
                            print("\nError in year.")
                            year = input('\nInput a year: ')
                
        elif opt == 2:
            print('\nValid Genres are: ', GENRES)
            genre = input('Input a genre: ')
            while True:
                if genre.capitalize() in GENRES: 
                    #check if genre (any upper, lower, mixed case) is in list 
                    #of GENRES given as constant
                    list_of_movieIDs = genre_movies(genre.capitalize(),\
                                                    L_movies)
                        
                    #finding max_avg values and list of movieIDs where
                    #max_avg value is found
                    max_avg_movies, max_avg = highest_rated_by_movie\
                        (list_of_movieIDs, L_reviews, N)
                    print('\nAvg max rating for the Genre is:' , max_avg)
                    for i in max_avg_movies:
                        print(L_movies[i][0])
                    break
                else:
                    print("\nError in genre.")
                    genre = input('Input a genre: ')
                        
     
            
            
        elif opt == 3:
            flag = False
            while not flag:
                gender = input('\nInput a gender (M,F): ')
                try:
                    if gender.upper() in ['M', 'F']: 
                        #check if gender inputted is valid 'M' or 'F'(any case)
                        moviesID_list = gen_users(gender, L_users, L_reviews)
                        
                        #finding max_avg values and list of movieIDs where
                        #max_avg value is found
                        max_avg_movies, max_avg = highest_rated_by_reviewer\
                            (moviesID_list, N)
                        print('\nAvg max rating for the Gender is:', max_avg)
                        for i in max_avg_movies:
                            print(L_movies[i][0])
                        flag = True
                        continue
                    else:
                        print("\nError in gender.")
                except:
                    print("\nError in gender.")
                                
                 
        elif opt == 4:
            print('\nValid Occupatipns are: ', OCCUPATIONS)
            while True:
                occupation = input('Input an occupation: ')
                if occupation in OCCUPATIONS :
                    #check if occupation parameter inputted is in list of 
                    #possible OCCUPATIONS constant given
                    moviesID_list = occ_users(occupation, L_users, L_reviews)
                    
                    #finding max_avg values and list of movieIDs where
                    #max_avg value is found
                    max_avg_movies, max_avg = highest_rated_by_reviewer\
                        (moviesID_list, N)
                    print('\nAvg max rating for the occupation is:', max_avg)
                    for i in max_avg_movies:
                        print(L_movies[i][0])
                    break
                                    
                else:
                    print("\nError in occupation.")

                
        elif opt == 5:
            break
        
        else:
            #if user inputs a value other than 1-5, print this error message
            print("\nError: not a valid option.")
        
       
if __name__ == "__main__":
    main()
                                           


