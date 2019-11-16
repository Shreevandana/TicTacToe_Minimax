import math
bestMoveForComputer = 0
import timeit

def drawBoard(board):
    """ Creates a copy of the board.
        :return copy of the board
     """
    
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')


def inputPlayerLetter():
    """ Determines the letter of each player ('X' or 'O') from keyboard input. """
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst(playerLetter):
    """ Determines which player goes first.
        :param playerLetter: the human or computer player
     """
    
    if playerLetter == 'X':
        return 'player'
    else:
        return 'computer'


def playAgain():
    """ Prompts the user to begin another game or not by indicating 'yes' or 'no'. """
    
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    """ Generates a move on the board by assigning the letter ('X' or 'O') to the appropriate spot on the board.
        :param board: the current state of the board
        :param letter: the player letter (either 'X' or 'O')
        :param move: the player move (0-8)
    """
    
    board[move] = letter


def isWinner(bo, le):
    """ Determines if a player wins from eight possibilities. Takes in two parameters,
        the board and the player letter.
        :param board: the current state of the board
        :param letter: the player letter (either 'X' or 'O')
        :return True if there is a winner and False otherwise
      """
    
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom
            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the right side
            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
            (bo[8] == le and bo[4] == le and bo[0] == le))    # diagonal


def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    """ Determines if a spot on the board is free.
        :param board: the current state of the board
        :param move: the move on the board
        :return True if the position is free and False otherwise
     """
    
    return board[move] == ' '


def getPlayerMove(board):
    """ Prompts user to input location in board (0-8) to place their letter. """
    
    move = ' '
    while move not in '0 1 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (0-8)[bottom left to top right]')
        move = input()
    return int(move)


def getfreespots(board):
    """ Returns a list of the spots available on the board.
        :param: board: the current state of the board
        :return list possible_moves
    """
    
    possibleMoves = []

    for i in range(0, 9):
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    # print(possibleMoves)
    if len(possibleMoves) != 0:
        return possibleMoves


def isBoardFull(board):
    """ Determines if the board is full.
        :return True if all the positions on the board are occupied and False otherwise.
    """
    
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True


def getscore(board):
    """Return the current score of the game.
        :return -1 if the human is winning, 1 if the computer is winning, and 0 otherwise.
    """
    
    if isWinner(board, playerLetter):
        return -1
    elif isWinner(board, computerLetter):
        return 1
    elif isBoardFull(board):
        return 0
    else:
        return 2

def bestMove(board, computerLetter, playerLetter):
    copyOfTheBoard = []

    maxvalue = -11
    b = -100
    for i in board:
        copyOfTheBoard.append(i)


    available = getfreespots(copyOfTheBoard)
   
    length = len(available)
    
    for i in range(0, length):
        copyOfTheBoard[available[i]] = computerLetter

        previousMaxValue = maxvalue
        
        maxvalue = max(maxvalue, ((1) * (minFunc(copyOfTheBoard, computerLetter, playerLetter))))
        copyOfTheBoard[available[i]] = ' '
        
        if previousMaxValue < maxvalue:
            b = available[i]


            
    return b


def maxFunc(board, computerLetter, playerLetter, firstCall):
    """ Function that finds best move for the maximizing player.
        :return maxvalue: the best possible score for the maximizing player.
    """
    
    copyOfTheBoard = []
    
    for i in board:
        copyOfTheBoard.append(i)

    score = getscore(copyOfTheBoard)


    #print('Debug maxFunc, score=', score)
    #drawBoard(copyOfTheBoard)

    if score == 1:
        #print('Final maxvalue is 10')
        return 10
    elif score == -1:
        #print('Final maxvalue is -10')
        return -10
    elif score == 0:
        #print('Final maxvalue is 0')
        return 0
    elif score == 2:
        maxvalue = -11


        available = getfreespots(copyOfTheBoard)
        length = len(available)
       
        for i in range(0, length):
            copyOfTheBoard[available[i]] = computerLetter

            previousMaxValue = maxvalue
            
            maxvalue = max(maxvalue, ((1)*(minFunc(copyOfTheBoard, computerLetter, playerLetter))))
            copyOfTheBoard[available[i]] = ' '
           

        return maxvalue


def minFunc(board, computerLetter, playerLetter):
    """ Function that finds best move for the minimizing player.
        :return minvalue: the best possible score for the minimizing player.
    """
    
    copyOfTheBoard = []

    for i in board:
        copyOfTheBoard.append(i)

    score = getscore(copyOfTheBoard)

    count = 0

    #print('Debug minFunc, score=', score)
    #drawBoard(copyOfTheBoard)

    if score == 1:
        #print('Final minFunc result was', 10)

        return 10
    elif score == -1:
        #print('Final minFunc result was', -10)

        return -10
    elif score == 0:
        #print('Final minFunc result was', 0)

        return 0
    elif score == 2:

        minvalue = 11

        available = getfreespots(copyOfTheBoard)
        
        length = len(available)

        for i in range(0, length):
            copyOfTheBoard[available[i]] = playerLetter

            count =  count + 1
        

            minvalue = min(minvalue, ((1)*maxFunc(copyOfTheBoard, computerLetter, playerLetter, 0)))
            copyOfTheBoard[available[i]] = ' '
        #print('Final minFunc result was', minvalue)
        #print(count)
    return minvalue


print('Tic Tac Toe!')

while True:
    # Reset the board

    theBoard = [' '] * 9
    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst(playerLetter)

    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You have won the game!')
             
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                  
                    gameIsPlaying = False
                else:
                    turn = 'computer'

        elif turn == 'computer':

            #start = timeit.timeit()
            x = bestMove(theBoard, computerLetter, playerLetter)
            makeMove(theBoard, computerLetter, x)

            #end = timeit.timeit()
            #print(end - start)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
              
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    
                    gameIsPlaying = False
                else:
                    turn = 'player'

    if not playAgain():
        break
