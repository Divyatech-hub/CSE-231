#LAB 5 Part C
file1 = open("output.txt", "w")
file2 = open('data.txt', 'r')
min_height = 100000
max_height = 0
min_weight = 100000
max_weight = 0
min_bmi = 100000
max_bmi = 0
total_height = 0
total_weight = 0
total_bmi = 0
lines = 1
file2.readline()
print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"), file=file1)
for line in file2:
    name = line[0:12].strip()
    height = float(line[12:16])
    weight = float(line[24:29])
    bmi = weight/(height**2)
    total_height += height
    total_weight += weight
    total_bmi += bmi

    if height > max_height:
        max_height = height
    elif height < min_height:
        min_height = height
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi

    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight, bmi))
    name = line[0:12].strip()
    height = float(line[12:16])
    weight = float(line[24:29])
    bmi = weight/(height**2)
    total_height += height
    total_weight += weight
    total_bmi += bmi

    if height > max_height:
        max_height = height
    elif height < min_height:
        min_height = height
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi
    lines += 1
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight, bmi), file = file1)
    
S
print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", (total_height/(lines-1))/2, (total_weight/(lines-1))/2, (total_bmi/(lines-1))/2), file = file1)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", max_height, max_weight, max_bmi), file = file1)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min_height, min_weight, min_bmi), file = file1)
file1.close()
file2.close()