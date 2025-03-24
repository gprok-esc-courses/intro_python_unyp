from tictactoe_lib import User, UserInterface, Board 

print("Tic Tac Toe Game")

ui = UserInterface()
board = Board()

namex = ui.get_user_name('X') 
nameo = ui.get_user_name('O')

userx = User(namex, 'X', 1)
usero = User(nameo, 'O', -1)
current = userx 

while True:
    ui.display_board(board.cells)
    row, col = ui.get_user_move(current)
    error = board.is_valid_move(row, col)
    if error is None:
        board.play(row, col, current) 
        current = userx if current == usero else usero
        winner = board.get_winner()
        if winner != 0:
            ui.display_board(board.cells)
            ui.display_winner(winner, userx, usero)
            break
        if board.is_tie():
            ui.display_board(board.cells)
            ui.display_tie()
            break
    else: 
        ui.display_error(error)