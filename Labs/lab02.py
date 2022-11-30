#Lab 2
odd_sum = 0
odd_count = 0
even_sum = 0
even_count = 0
positive_int_count = 0

while True:
    n_str = input('Input an integer (0 terminates): \n')
    n_int = int(n_str)
    
    if n_int != 0:
        if n_int > 0:
            if n_int % 2 == 0:
                even_sum = even_sum + n_int
                even_count +=1
            else:
                odd_count += 1
                odd_sum = odd_sum + n_int
                
            positive_int_count += 1
            
        else:
            pass
        
    elif n_int == 0:
        break 
            
                
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
