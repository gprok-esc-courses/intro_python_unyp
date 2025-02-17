import csv

file = open('students.csv')

dict_reader = csv.DictReader(file)

for row in dict_reader:
    print(row)