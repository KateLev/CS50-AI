"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    counter = 0  
    length = len(board)
    for i in range (0, length):
        for j in range (0, length):
            if board[i][j]!=EMPTY:
                counter += 1  
    if (counter%2 == 1):        
        return(O)
    else:          
        return(X)


def actions(board):
    possibleAction = []
    length = len(board)
    for i in range (0, length):
        for j in range (0, length):
            if board[i][j] == EMPTY:
                possibleAction.append((i,j))            
    return possibleAction


def result(board, action):
    newState = deepcopy(board) 
    newState [action[0]][action[1]]= player(board)
    return newState

def winner(board):
    if (board[0][0]==board[0][1]==board[0][2]):
        return (board[0][0])
    elif (board[1][0]==board[1][1]==board[1][2]):
        return (board[1][0])
    elif (board[2][0]==board[2][1]==board[2][2]):
        return (board[2][0])
    elif (board[0][0]==board[1][0]==board[2][0]):
        return (board[0][0])
    elif (board[0][1]==board[1][1]==board[2][1]):
        return (board[0][1])
    elif (board[0][2]==board[1][2]==board[2][2]):
        return (board[0][2])
    elif (board[0][0]==board[1][1]==board[2][2]):
        return (board[0][0])
    elif (board[2][0]==board[1][1]==board[0][2]):
        return (board[2][0])
    else:
        return None
        
def slowWinner(board):    
    lines =[]
    singleLine = []
    n = len(board)      
    
    
    """
    Diag
    """
    for i in range(n):        
        for j in range(n):            
            if (i==j):
                singleLine.append(board[i][j])
    lines.append(singleLine)           
    singleLine = []
    """
    Horizontal lines
    """
    for i in range(n):
        lines.append(board[i])   
    
    """
    Reverse diag
    """
    
    for i in range(n):        
        for j in range(n):
            if ((i + j + 1) == n):
                singleLine.append(board[i][j]) 
    lines.append(singleLine)  
    singleLine = []
    """
    Vertical lines
    """
    
    for i in range(n):
        singleLine = []
        for j in range(n):
            singleLine.append(board[j][i]) 
        lines.append(singleLine)       
            
    for i in range(len(lines)): 
        tester = lines[i][0]
        if lines[i].count(tester) == n:
            if tester:
                return(tester)
    return None

def terminal(board):
    if winner(board):        
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:                
                return False    
    return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    whoIsWinner = winner(board)
    if whoIsWinner == X:        
        return 1
    elif whoIsWinner == O:        
        return -1
    else:        
        return 0

def maxValue(state, alphaPrune, betaPrune):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action),alphaPrune, betaPrune))
        if betaPrune < v:
            break
    return v

def minValue(state,alphaPrune, betaPrune):
    if terminal(state):
        return utility(state)
    v = +math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action),alphaPrune, betaPrune)) 
        if alphaPrune > v:
            break
    return v

  
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = minValue(result(board, action))    #FIXED
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = maxValue(result(board, action))    #FIXED
            if k < v:
                v = k
                best_move = action
    return best_move

def minimax(board):
   
    if terminal(board):
        return None

    alphaPrune = - math.inf
    betaPrune = math.inf 
    
    if player(board) == X:
        v = -math.inf        
        for action in actions(board):
            n = minValue(result(board, action),alphaPrune, betaPrune)    
            if n > v:  
                alphaPrune = n
                v = n
                bestMove = action
    else:
        v = math.inf
        for action in actions(board):
            n = maxValue(result(board, action),alphaPrune, betaPrune)    
            if n < v:
                betaPrune = n
                v = n
                bestMove = action
    return bestMove


