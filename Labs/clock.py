#clock module

class Time(object):
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        '''This function is used to initialize the clock 
        with the 3 parameters - hours, minutes, seconds
        '''
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        
    def __repr__(self):
        '''this function is to represent the clock elements in required format
        '''
        time = "{}:{}:{}".format(self.__hours, self.__minutes, self.__seconds)
        l = time.split(":")
        L1 = []
        for x in l:
            y = str(x)
            if int(x) < 10 :
                y = "0"+str(x)
            L1.append(y)    
            
        a = "Class Time: {}:{}:{}".format(L1[0], L1[1], L1[2])
        return a
        
    def __str__(self):
        '''this function is to represent the clock elements in a human-readable
        format.
        '''
        time = "{}:{}:{}".format(self.__hours, self.__minutes, self.__seconds)
        l = time.split(":")
        L1 = []
        for x in l:
            y = str(x)
            if int(x) < 10 :
                y = "0"+str(x)
            L1.append(y)    
            
        a = "{}:{}:{}".format(L1[0], L1[1], L1[2])
        return a
    
    def from__str(self, time_str):
        '''This function is ued to update an object of type Time after it has 
        been created.
        '''
        time_list = time_str.replace(",","").split()
                    
        self.__hours = time_list[0]
        self.__minutes   = time_list[1]
        self.__seconds  = time_list[2]
