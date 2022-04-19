import random
#Creates Board 
board = [' ' for x in range(10)]

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
#Inserts the letters in the board game   
def insertLetter(letter, pos):
    board[pos] = letter  
#Checks if any spaces are free 
def spaceFree(pos):
    return board[pos] == ' '
    
#Coin flip to see who starts 
def coinFlip(): 
    return random.randint(1,2)
#All ways to check if someone wins 
def checkWinner(boardPos, letters): 
   return ((boardPos[7] == letters and boardPos[8] == letters and boardPos[9] == letters) or # across the top
    (boardPos[4] == letters and boardPos[5] == letters and boardPos[6] == letters) or # across the middle
    (boardPos[1] == letters and boardPos[2] == letters and boardPos[3] == letters) or # across the bottom
    (boardPos[7] == letters and boardPos[4] == letters and boardPos[1] == letters) or # down the left side
    (boardPos[8] == letters and boardPos[5] == letters and boardPos[2] == letters) or # down the middle
    (boardPos[9] == letters and boardPos[6] == letters and boardPos[3] == letters) or # down the right side
    (boardPos[7] == letters and boardPos[5] == letters and boardPos[3] == letters) or # diagonal
    (boardPos[9] == letters and boardPos[5] == letters and boardPos[1] == letters)) # diagonal

#Players turn
def player1():   
    turn = True  
    while turn: 
            #Asks user to input a number it will give back 
            move = int(input("Please enter an open slot > "))
            if move >0 and move <10: 
                #Checks if space is free 
                if spaceFree(move): 
                    turn = False
                    insertLetter('X', move)
                else: 
                    print("That space is taken ")
            else: 
                print("That space is not valid ")
#Computers turn                
def computer():
    turn = True
    while turn: 
        #Randomizes its move 
        move = random.randint(1,9)
        #Checks if space is free 
        if spaceFree(move):
            turn = False
            insertLetter('O', move)
            
#Checks if the board is full 
def full(board): 
    if board.count(' ') >1: 
        return False 
    else: 
        return True 
    
#plays the game   
def playGame(): 
    printBoard(board) 
    #Coin flip to see who goes first 
    if coinFlip() == 1: 
        player1() 
        printBoard(board)
        computer()
        printBoard(board)
    else: 
        computer() 
        printBoard(board)
    #goes into a while loops until there is a winner   
    while not full(board): 
       
        if not(checkWinner(board, 'O')):
            player1()
            printBoard(board)
        else:
            print("You Lost!")
            break
        if not(checkWinner(board, 'X')):
            computer()
            printBoard(board)
        else:
            print("You Win!")
            break
    if full(board):
        print('Tie Game!')
        
        
playGame()
            

        

