# Ask user for a number n 
# then print n asterisks

n = input("Give a number: ")
n = int(n)

for i in range(n):
    print('*', end=' ')

print()