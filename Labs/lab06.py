#LAB06 - New
f = open("scores.txt", 'r')
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format('Name', 'Exam1', 'Exam2', 'Exam3', 'Exam4', 'Mean'))
tot_exam1 = 0
tot_exam2 = 0
tot_exam3 = 0
tot_exam4 = 0
list_of_studs = []

for line in f:
    items = line.split()
    names = items[0] + ' '+ items[1]
    exam1 = int(items[2])
    exam2 = int(items[3])
    exam3 = int(items[4])
    exam4 = int(items[5])
    stud_mean = (exam1 + exam2 + exam3 + exam4)/ 4
    student = (names, exam1, exam2, exam3, exam4, stud_mean)
    list_of_studs.append(student)
    list_of_studs = sorted(list_of_studs)
   
    
for stud in list_of_studs:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(stud[0], stud[1], stud[2], stud[3], stud[4], stud[5]))

for stud in list_of_studs:
    tot_exam1 += stud[1]
    tot_exam2 += stud[2]
    tot_exam3 += stud[3]
    tot_exam4 += stud[4]
    mean_exam1 = tot_exam1/5
    mean_exam2 = tot_exam2/5
    mean_exam3 = tot_exam3/5
    mean_exam4 = tot_exam4/5

print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format('Exam Mean', mean_exam1, mean_exam2, mean_exam3, mean_exam4))
f.close()