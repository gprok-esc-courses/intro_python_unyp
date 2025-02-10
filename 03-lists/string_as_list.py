
name = "Kalamazoo"

print(len(name))
print(name[3])

# print like in Hangman game

# print the first letter
print(name[0], end=' ')
# print 9 dashes
for i in range(len(name) - 2):
    print('_', end=' ')
# print the last letter
print(name[-1])