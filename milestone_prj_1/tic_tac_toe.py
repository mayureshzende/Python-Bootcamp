import random
def select_first_move():
    return 'player 1' if random.randint(0,1) == 0 else 'player 2'

def select_player_XO(p):
    print(f"{p} please select the -> X or O ")
    player1 = '' 
    player2 = ''
    if  p == 'player 1':
        player1 = input("X or O")
        if player1.upper() == 'X' or player1 == 'x':
            player2 = 'O'.upper()
        else:
            player2 = 'X'.upper()
    if p == 'player 2':
        player2 = input("X or O")
        if player2.upper() == 'x' or player2 == 'x':
            player1 = 'O'.upper() 
        else:
            player1 = 'X'.upper()
            
    return (player1.upper() , player2.upper())

def display_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("-- --- --")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("-- --- --")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def win_check(board , mark ):
    return (
        (board[1] == mark and board[2] == mark and board[3] == mark) or 
        (board[4] == mark and board[5] == mark and board[6] == mark) or 
        (board[7] == mark and board[8] == mark and board[9] == mark) or 
        (board[1] == mark and board[4] == mark and board[7] == mark) or 
        (board[2] == mark and board[5] == mark and board[8] == mark) or 
        (board[3] == mark and board[6] == mark and board[9] == mark) or 
        (board[1] == mark and board[5] == mark and board[9] == mark) or 
        (board[7] == mark and board[5] == mark and board[7] == mark)  
    )

def place_marker(board , position , marker ):
    # display_board(board)
    # position = input(" put the position from (1 ro 9 )")
    board[int(position)] = marker
    # active = 'p1'
    # if active == 'p1':
    #     board[int(position)] = 'X' if player1 == 'X' else 'O'
    # else:
    #     board[int(position)] = 'X' if player2 == 'X' else 'O'
    # display_board(board)

def space_check(board, position ):
    return board[position] in range(1,10)

def full_board_check(board):
    for i in range(1,10):
        if space_check(board , i ):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board , position):
        position = int(input("choose your position between (1 to 9)"))
    return position

def replay():
    return input(' do you want to play again y/n').lower().startswith('y')

def play_game():

    tic_board = list(range(0,10)) 

    # display_board(tic_board)

    game_on = False

    
    while True:

        ready = input(" Ready to play (yes / no || y / n)")

        if ready.lower() == 'yes' or ready.lower() == 'y':
            game_on = True
            display_board(tic_board)
        else:
            game_on = False
        p = select_first_move()
        p1,p2 = select_player_XO(p)
        print( f"player 1 is {p1}, player 2 is {p2} \n")
        print(f" {p} goes first ")
        
        while game_on:
            if p == 'player 1':
               display_board(tic_board)
               position = player_choice(tic_board)
               place_marker(tic_board , position , p1 )

               if win_check(tic_board , p1):
                    display_board(tic_board)
                    print(f" congratulation {p} you have won the game!!!!")
                    game_on = False
               else:
                    if full_board_check(tic_board):
                        display_board(tic_board)
                        print(" the game is drawn ")
                        break   
                    else:
                        p = 'player 2'
                    
            else:   
                display_board(tic_board)
                position = player_choice(tic_board)
                place_marker(tic_board , position , p2)

                if win_check(tic_board , p2):
                    display_board(tic_board)
                    print(f"congratulation {p} hass won the game!!!")
                    game_on = False
                else:
                    if full_board_check(tic_board):
                        display_board(tic_board)
                        print("the game is drawn!")
                        break
                    else:
                        p = 'player 1'
        if not replay():
            break

play_game()
