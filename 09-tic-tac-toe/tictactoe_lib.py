
class User:
    def __init__(self, name, symbol, value):
        self.name = name 
        self.symbol = symbol 
        self.value = value 

class Board:
    def __init__(self):
        self.cells = [[0] * 3 for i in range(3)]

    def is_valid_move(self, row, col):
        if row < 1 or row > 3 or col < 1 or col > 3:
            return "Value out of board"
        if self.cells[row-1][col-1] != 0:
            return "Cell is already occupied"
        return None
    
    def play(self, row, col, user):
        row -= 1
        col -= 1
        self.cells[row][col] = user.value

    def get_winner(self):
        for i in range(3):
            if abs(self.cells[i][0] + self.cells[i][1] + self.cells[i][2]) == 3:
                return self.cells[i][0]
            if abs(self.cells[0][i] + self.cells[1][i] + self.cells[2][i]) == 3:
                return self.cells[0][i]
        if abs(self.cells[0][0] + self.cells[1][1] + self.cells[2][2]) == 3:
            return self.cells[1][1]
        if abs(self.cells[0][2] + self.cells[1][1] + self.cells[2][0]) == 3:
            return self.cells[1][1]
        return 0
    
    def is_tie(self):
        for r in range(3):
            for c in range(3):
                if self.cells[r][c] == 0:
                    return False 
        return True



class UserInterface:
    def get_user_name(self, n):
        name = input("Name of user " + n + ": ")
        return name
    
    def display_board(self, cells):
        symbols = ['O', '-', 'X']
        for r in range(3):
            for c in range(3):
                p = cells[r][c] + 1
                print(symbols[p], end=' ')
            print()

    def get_user_move(self, user):
        print(user.name + " plays")
        row = int(input("Row (1-3): "))
        col = int(input("Col (1-3): "))
        return row, col
    
    def display_error(self, msg):
        print("ERROR: " + msg)

    def display_winner(self, value, userx, usero):
        if userx.value == value:
            print(userx.name + " WINS!")
        else:
            print(usero.name + " WINS!")

    def display_tie(self):
        print("It's a TIE")

