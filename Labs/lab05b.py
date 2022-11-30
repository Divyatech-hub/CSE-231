#LAB 5 partb
import math
file = open("data.txt", "r")
file.readline()
min_height = 100000
max_height = 0
min_weight = 100000
max_weight = 0
min_bmi = 100000
max_bmi = 0
total_height = 0
total_weight = 0
total_bmi = 0
lines = 0
# print()
print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"))
for line in file:
    lines += 1
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
file.close()


print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", total_height/lines, total_weight/lines, total_bmi/lines))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", max_height, max_weight, max_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min_height, min_weight, min_bmi))