#Lab4
import math 

def leap_year(year):
     if int(year) % 400 == 0:
         return True
     elif int(year) % 4 == 0 and int(year) % 100 != 0:
         return True
     else:
         return False

def rotate(s,n):
    if s == '' or len(s) == 1:
        return s
    else:
        new_s = ""
        new_s += s[-n:] + s[0:-n]
        return new_s
    
def digit_count(number):
    even_count = 0
    odd_count = 0
    zero_count = 0
    number = math.floor(number)
    
    for ch in str(number):
        if int(ch) % 2 == 0 and int(ch) != 0:
            even_count += 1
        elif int(ch) % 2 != 0:
            odd_count += 1
        if int(ch) == 0:
            zero_count += 1     
    return even_count, odd_count, zero_count
            

def float_check(strg):
    dot_count = 0
    for x in strg:
        if x == '.':
            dot_count += 1
        elif x.isalpha():
            return False
        
    if dot_count > 1:
        return False
    else:
        return True 
    
    
    
year = int(input(''))
print(leap_year(year))
strg = input("")
num = int(input(""))
print(rotate(strg, num))
number = float(input())
even_count, odd_count, zero_count = digit_count(number)
print('(', even_count, ',', odd_count, ',' , zero_count,')')
strg = input()
result = float_check(strg)
print(result)
