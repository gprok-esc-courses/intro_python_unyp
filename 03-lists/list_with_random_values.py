import random

data = []

for i in range(5):
    data.append(random.randint(1, 100))

print(data)

# Find the average value
total = 0
# for i in range(len(data)):
#     total = total + data[i]
for value in data:
    total += value

avg = total/len(data)
print(avg)


# Find and print the max
m = 0
for v in data:
    if v > m:
        m = v
print("Maximum is ", m)