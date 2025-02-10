
board = [
    [' ', 'O', 'X'],
    ['O', ' ', 'X'],
    [' ', 'X', 'O']
]

for row in board:
    for value in row:
        print(value, end=' ')
    print()