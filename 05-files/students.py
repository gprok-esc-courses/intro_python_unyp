
file = open('students.csv')
lines = file.readlines()

students = {} 

for i in range(1, len(lines)):
    data = lines[i].strip().split(',')
    key = data[0]
    students[key] = data 

print(students)

id = input("ID: ")
if id in students:
    print("GPA: ", students[id][2])
else:
    print(id, "not found")