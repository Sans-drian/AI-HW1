#setting up board
gameboard = { 1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}

#create gameboard
def printBoard(gameboard):
    print(gameboard[1]+ '|' + gameboard[2] + '|' + gameboard[3])
    print('-+-+-')
    print(gameboard[4]+ '|' + gameboard[5] + '|' + gameboard[6])
    print('-+-+-')
    print(gameboard[7]+ '|' + gameboard[8] + '|' + gameboard[9])
    print('\n')
    
#check if space is empty or not
def checkSpaceFree(position):
    if (gameboard[position] == ' '):
        return True
    else:
        return False
    
#check if the game is a draw
def checkDraw():
    for key in gameboard.keys():
        if gameboard[key] == ' ':
            return False
        
    return True

#check win
def checkForWin():
    if (gameboard[1] == gameboard[2] and gameboard[1] == gameboard[3] and gameboard[1] != ' '):
        return True
    elif (gameboard[4] == gameboard[5] and gameboard[4] == gameboard[6] and gameboard[4] != ' '):
        return True
    elif (gameboard[7] == gameboard[8] and gameboard[7] == gameboard[9] and gameboard[7] != ' '):
        return True
    elif (gameboard[1] == gameboard[4] and gameboard[1] == gameboard[7] and gameboard[1] != ' '):
        return True
    elif (gameboard[2] == gameboard[5] and gameboard[2] == gameboard[8] and gameboard[2] != ' '):
        return True
    elif (gameboard[3] == gameboard[6] and gameboard[3] == gameboard[9] and gameboard[3] != ' '):
        return True
    elif (gameboard[1] == gameboard[5] and gameboard[1] == gameboard[9] and gameboard[1] != ' '):
        return True
    elif (gameboard[7] == gameboard[5] and gameboard[7] == gameboard[3] and gameboard[7] != ' '):
        return True
    else:
        return False

#check win for specific symbol
def checkForWinSymbol(symbol):
    if (gameboard[1] == gameboard[2] and gameboard[1] == gameboard[3] and gameboard[1] == symbol):
        return True
    elif (gameboard[4] == gameboard[5] and gameboard[4] == gameboard[6] and gameboard[4] == symbol):
        return True
    elif (gameboard[7] == gameboard[8] and gameboard[7] == gameboard[9] and gameboard[7] == symbol):
        return True
    elif (gameboard[1] == gameboard[4] and gameboard[1] == gameboard[7] and gameboard[1] == symbol):
        return True
    elif (gameboard[2] == gameboard[5] and gameboard[2] == gameboard[8] and gameboard[2] == symbol):
        return True
    elif (gameboard[3] == gameboard[6] and gameboard[3] == gameboard[9] and gameboard[3] == symbol):
        return True
    elif (gameboard[1] == gameboard[5] and gameboard[1] == gameboard[9] and gameboard[1] == symbol):
        return True
    elif (gameboard[7] == gameboard[5] and gameboard[7] == gameboard[3] and gameboard[7] == symbol):
        return True
    else:
        return False

#function to add symbol
def insertLetter(letter, position):

    if checkSpaceFree(position):
        gameboard[position] = letter
        printBoard(gameboard)

        #checking if the game is a draw
        if(checkDraw()):
            print("It's a draw.")
            exit()
        
        #after inserting, check the state for wins
        if checkForWin():
            if letter == 'x':
                print ("The bot wins.")
                exit()
            else:
                print("You win.")
                exit()

        return

    #checking if space selected is filled or not
    else: 
        print ("This space is filled.")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return
    

#test if check space function works
#print(checkSpaceFree(1))
#printBoard(gameboard)
#insertLetter('x', 1)
#insertLetter('x', 1)


#set symbols
player = '0'
bot = 'x'

#function of player's move
def playerMove():
    position = int(input("Enter the position for '0': "))
    insertLetter(player, position)
    return

#bot moving function
def pcMove():
    bestScore = -1000
    bestMove = 0

    for key in gameboard.keys():
        if(gameboard[key] == ' '):
            gameboard[key] = bot
            score = minimax(gameboard, 0, False)
            gameboard[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

#minimax 
def minimax(board, depth, isMaximizing):
    #check pc win
    if checkForWinSymbol(bot):
        return 100
    #check player win
    elif checkForWinSymbol(player):
        return -100
    
    elif checkDraw():
        return 0
    

    if isMaximizing:
        bestScore = -1000
        
        for key in gameboard.keys():
            if(gameboard[key] == ' '):
                gameboard[key] = bot
                score = minimax(gameboard, 0, False)
                gameboard[key] = ' '
                if(score > bestScore):
                    bestScore = score

        return bestScore
    
    else:
        bestScore = 800
        
        for key in gameboard.keys():
            if(gameboard[key] == ' '):
                gameboard[key] = player
                score = minimax(gameboard, 0, True)
                gameboard[key] = ' '
                if(score < bestScore):
                    bestScore = score

        return bestScore


#game running
while not checkForWin():
    pcMove()
    playerMove()