import csv
with open('SOCR-HeightWeight.csv', newline= '') as f:
    readCsv = csv.reader(f)
    list1 = list(readCsv)
    list1.pop(0)
    list2 = []

    for i in range (len(list1)):
        a = list1[i][1]
        list2.append(float(a))

#Displaying mean
listlength = len(list2)
total = 0

for i in list2:
    total = total+i
mean = total/listlength
print("The mean(Average) is " + str(mean))

list2.sort

#Median
if listlength%2 == 0:
    median1 = float(list2[listlength//2])
    median2 = float(list2[listlength//2] - 1)
    median = (median1 + median2) / 2
else:
    median = list2[listlength//2]
print("The median is " + str(median))

#Mode
from collections import Counter
mode = Counter(list2)
print("The mode is " + str(mode))