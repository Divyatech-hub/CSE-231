#Lab 3
while True:
    VOWELS= "aeiou"
    word = input("Enter a word ('quit' to quit):\n")
    lowerword = word.lower()
    
    if lowerword != 'quit':
        if lowerword[0] in VOWELS:
            pig_latin = lowerword + 'way'
        
        elif lowerword[0] not in VOWELS:
            pig_latin = ""
            for i, ch in enumerate(lowerword):
                if ch in VOWELS:
                    first_vowel = ch 
                    first_vowel_index = i
                    break
            pig_latin = lowerword[i:] + lowerword[0:i] + 'ay'
                    


        print(pig_latin)
        
    elif lowerword == 'quit':
        break 
                
                 
