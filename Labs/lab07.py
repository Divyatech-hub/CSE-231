#LAB07
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Docstring'''
    reader = csv.reader(fp)
    next(reader, None)
    next(reader, None)
    next(reader, None)
    next(reader, None)
    states = []
    for line in reader:
        if line == []:
            continue
        elif '' in line:
            continue
        else: 
            states.append(line)
    return states 
    

def get_totals(L):
    '''Docstring'''
    calc_total = 0 
    US_total = L[0][1]
    US_total = US_total.split(',')
    number = int(US_total[0] + US_total[1] + US_total[2])
    for state in L: 
        imm_popu = state[1]
        if imm_popu == '10,700,000':
            continue
        imm_popu = imm_popu.replace(',','')
        if '<' in imm_popu:
            imm_popu = imm_popu.replace('<','')
        imm_popu = int(imm_popu)
        calc_total += imm_popu
            
    return number, calc_total
            

        

def get_industry_counts(L):
    '''Docstring'''
    industry_list = []
    for line in L:
        if line == L[0]:
            continue
        industry_list.append(line[9])
        main_list = []
    for x in industry_list:
        if main_list == []:
            continue 
        if x in main_list[0]:
            continue
        else:
            y = industry_list.count(x)
            z = [x,y]
            main_list.append(z)
    return main_list
    

def get_largest_states(L):
    '''Docstring'''
    greater_states = []
    summ_percent = L[0][2]
    summ_percent = summ_percent.replace('%', '')
    number = float(summ_percent)
    for line in L:
        imm_percent = line[2]
        if imm_percent == '3.30%':
            continue
        imm_percent = imm_percent.replace('%','')
        imm_percent = float(imm_percent)
        if imm_percent > number:
            greater_states.append(line[0])
    return greater_states
            
def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    print(L)
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()

