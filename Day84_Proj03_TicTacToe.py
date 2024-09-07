import os

def is_cats_game():
    """Checks if the board is in a cats game, 
    Return False if any 0 (blank spots) are found, 
    otherwise return True"""    
    for row in board:
        for value in row:
            if value == 0:
                return False
    return True

def index_error():
    print("Row or Column value was invalid:")

def get_player():
    """Gets the players character by it's index value"""
    if player1:
        return players[0]
    else:
        return players[1]    

def match_row(row):
    """Checks if row is all the same greater than zero value
    If this condition is met, the winner_index is set
    and True is returned
    """
    global winner_index
    if board[row][0] > 0:
        if row >= 0 and row <= 2:    
            if board[row][0] == board[row][1] == board[row][2]:
                winner_index = board[row][0]
                #print(f"row {row} match")
                return True
    return False

def match_column(column):
    """Checks if column is all the same greater than zero value
    If this condition is met, the winner_index is set
    and True is returned
    """
    global winner_index
    if board[0][column] > 0:
        if column >= 0 and column <= 2:    
            if board[0][column] == board[1][column] == board[2][column]:
                #print(f"column {column} match")
                winner_index = board[0][column]
                return True
    return False

def match_diagonals():
    """Checks if one of the two diagonals is all the same greater than zero value
    If this condition is met, the winner_index is set
    and True is returned
    """
    global winner_index
    if board[0][0] > 0:
        if board[0][0] == board[1][1] == board[2][2]:
            #print(f"\ diagonal match")
            winner_index = board[0][0]
            return True
    if board[0][2] > 0:
        if  board[0][2] == board[1][1] == board[2][0]:
            #print(f"/ diagonal match")
            winner_index = board[0][2]
            return True
    return False

def check_if_winner():
    """ Checks all the row, column and diagonal winning states"""
    if(match_row(0) or match_row(1) or match_row(2) or match_column(0) or match_column(1) or match_column(2) or match_diagonals()):
        return True

    #reference to the indexes for each game position
    # 0,0   0,1   0,2
    
    # 1,0   1,1   1,2
    
    # 2,0   2,1   2,2
    

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def draw_board():
    """ Clears the screen and draws the players character symbol if a non-zero (blank) value exists in the board matrix"""
    os.system('cls')
    for row in board:
        print("")
        for value in row:
            if value == 0:
                print ("_", end="")
            elif value == 1:
                print("O", end="")
            elif value == 2:
                print("X", end="")
    print("")

valid_move = False # controls the player input while look
players = [(1, "0"), (2, "X")] #look up of player character symbol based on index
player1 = True # Used to control who is current player
winner_index = 0 #controls the game loop and handling of the winner

while winner_index == 0:
    valid_move = False
    while not valid_move :
        draw_board()
        player = get_player()    

        try:
            move_x = int(input(f"Player {player[0]} you are {player[1]}'s, Make a move, select a row:")) -1
            move_y = int(input("and a column:")) -1

            #check no negative values are used in game inputs
            if(move_y < 0 or move_x < 0):
                index_error()
                break
            
            #checks if spot on the board is already taken
            if board[move_x][move_y] != 0:
                print("Invalid Selection, try again")
            else:
                #valid move
                player1 = not player1 # Toggle Player
                board[move_x][move_y] = player[0] # assign the postion to the player
                check_if_winner()
                if  winner_index> 0:
                    break;
                valid_move = True
    
        except (IndexError,ValueError) as exception:
             index_error()
             
        if is_cats_game():
            draw_board()
            print("Cats Game, no one wins :(")
            winner_index = -1
            break;
        
if winner_index > 0:
    draw_board()
    print(F"Player {winner_index} is the winner!")
              
