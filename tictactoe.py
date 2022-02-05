from flask import request,Blueprint, render_template

tictactoe=Blueprint('tictactoe',__name__)

global buttons
buttons = {'b1': '', 'b2': '', 'b3': '', 'b4': '', 'b5': '', 'b6': '', 'b7': '', 'b8': '', 'b9': ''}

@tictactoe.route('/')
def index():
    global buttons
    buttons = {'b1': '', 'b2': '', 'b3': '', 'b4': '', 'b5': '', 'b6': '', 'b7': '', 'b8': '', 'b9': ''}
    print (buttons)
    print ("player=1")
    return render_template('tictactoe.html',buttons=buttons,player='1')

@tictactoe.route('/play')
def play():
    player=request.args['player']
    button=request.args['button']
    buttons[button]=player
    print (buttons)
    print ("player="+player)
        
    if windraw():
        winner="Player "+player
    elif buttonfull():
        winner='Nobody'
    else:
        winner=''

    if player == "1":
        player = "2"
    else:
        player = "1"
    
    return render_template('tictactoe.html',buttons=buttons,player=player,winner=winner)
    
def buttonfull():
    if buttons['b1'] and buttons['b2'] and buttons['b3'] and buttons['b4'] and buttons['b5'] and buttons['b6'] and buttons['b7'] and buttons['b8'] and buttons['b9']:
        return True
    else:
        return False
# def display(board):
#     return(f'{board[1]}|{board[2]}|{board[3]}\n{board[4]}|{board[5]}|{board[6]}\n{board[7]}|{board[8]}|{board[9]}')
# @tictactoe.route('/')   
# def player_input():
#     player1=request.args['player1']
#     player2=request.args['player2']
#     while player1 not in ['X','O']:
#         player1=request.args['player1']
#         if player1 not in ['X','Y']:
#             continue
        
#     if player1=='X':
#         player2='O'
#     else:
#         player2='X'
#     return (player1,player2)
    
# def position(board):
#     pos=0
#     while pos not in ['1','2','3','4','5','6','7','8','9']:
#         pos=request.args['pos']
#         if pos not in range(1,10):
#             print("Please enter a number between 1-9 ")
#     return int(pos)
    
def windraw():
    condition = ( 
        ( (buttons['b1'] != '') and buttons['b1']==buttons['b2'] and buttons['b2']==buttons['b3'] ) or 
        ( (buttons['b4'] != '') and buttons['b4']==buttons['b5'] and buttons['b5']==buttons['b6'] ) or 
        ( (buttons['b7'] != '') and buttons['b7']==buttons['b8'] and buttons['b8']==buttons['b9'] ) or
        ( (buttons['b1'] != '') and buttons['b1']==buttons['b4'] and buttons['b4']==buttons['b7'] ) or
        ( (buttons['b2'] != '') and buttons['b2']==buttons['b5'] and buttons['b5']==buttons['b8'] ) or
        ( (buttons['b3'] != '') and buttons['b3']==buttons['b6'] and buttons['b6']==buttons['b9'] ) or
        ( (buttons['b1'] != '') and buttons['b1']==buttons['b5'] and buttons['b5']==buttons['b9'] ) or
        ( (buttons['b3'] != '') and buttons['b3']==buttons['b5'] and buttons['b5']==buttons['b7'] ) 
    )
    
    if  condition:
        print ("windraw=TRUE")
        return True
    else:
        print ("windraw=FALSE")
        return False
# @  
# board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# print('Welcome to Tic Tac Toe')
# player1marker,player2marker=player_input()
# turn=choose_first()
# print(f'{turn} goes first')
# display(board)

# gameover=False
# while gameover==False:
#     from IPython.display import clear_output
#     if turn=='player 1':
#         print("player 1's turn")
#         pos=position(board)
#         board[pos]=player1marker
#         clear_output()
#         display(board)
#         gameover=windraw(board,player1marker)
#         turn='player 2'
#     else:
#         print("player 2's turn")
#         pos=position(board)
#         board[pos]=player2marker
#         clear_output()
#         display(board)
#         gameover=windraw(board,player2marker)
#         turn='player 1'