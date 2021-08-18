TicTacToeBoard = {'1':' ' , '2':' ' , '3':' ',
                  '4':' ' , '5':' ' , '6':' ',
                  '7':' ' , '8':' ' , '9':' '}

player1 = input("Enter Your Name[Player 1]: ")
player2 = input("Enter Your Name[Player 2]: ")
player = 1
turns = 0

def declareSymbol():
    print("---------------------------")
    print(player1+" Assigned -> X")
    print(player2+" Assigned -> O")
    print("---------------------------")


def winCheck():
    #FOR PLAYER 1
    #First Horizontal
    if TicTacToeBoard['1'] == 'X' and TicTacToeBoard['2'] == 'X' and TicTacToeBoard['3'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1
        
    #Second Horizontal
    if TicTacToeBoard['4'] == 'X' and TicTacToeBoard['5'] == 'X' and TicTacToeBoard['6'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #Third Horizontal
    if TicTacToeBoard['7'] == 'X' and TicTacToeBoard['8'] == 'X' and TicTacToeBoard['9'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #First Vertical
    if TicTacToeBoard['1'] == 'X' and TicTacToeBoard['4'] == 'X' and TicTacToeBoard['7'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #Second Vertical
    if TicTacToeBoard['2'] == 'X' and TicTacToeBoard['5'] == 'X' and TicTacToeBoard['8'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #Third Vertical
    if TicTacToeBoard['3'] == 'X' and TicTacToeBoard['6'] == 'X' and TicTacToeBoard['9'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #First Diagonal
    if TicTacToeBoard['1'] == 'X' and TicTacToeBoard['5'] == 'X' and TicTacToeBoard['9'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #Second Diagonal
    if TicTacToeBoard['7'] == 'X' and TicTacToeBoard['5'] == 'X' and TicTacToeBoard['3'] == 'X':
        print("---------------------------\n"+player1+" Won!")
        return 1

    #FOR PLAYER 2
    #First Horizontal
    if TicTacToeBoard['1'] == 'O' and TicTacToeBoard['2'] == 'O' and TicTacToeBoard['3'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1
        
    #Second Horizontal
    if TicTacToeBoard['4'] == 'O' and TicTacToeBoard['5'] == 'O' and TicTacToeBoard['6'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #Third Horizontal
    if TicTacToeBoard['7'] == 'O' and TicTacToeBoard['8'] == 'O' and TicTacToeBoard['9'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #First Vertical
    if TicTacToeBoard['1'] == 'O' and TicTacToeBoard['4'] == 'O' and TicTacToeBoard['7'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #Second Vertical
    if TicTacToeBoard['2'] == 'O' and TicTacToeBoard['5'] == 'O' and TicTacToeBoard['8'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #Third Vertical
    if TicTacToeBoard['3'] == 'O' and TicTacToeBoard['6'] == 'O' and TicTacToeBoard['9'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #First Diagonal
    if TicTacToeBoard['1'] == 'O' and TicTacToeBoard['5'] == 'O' and TicTacToeBoard['9'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

    #Second Diagonal
    if TicTacToeBoard['7'] == 'O' and TicTacToeBoard['5'] == 'O' and TicTacToeBoard['3'] == 'O':
        print("---------------------------\n"+player2+" Won!")
        return 1

def boardStatus():
    print(TicTacToeBoard['1']+'|'+TicTacToeBoard['2']+'|'+TicTacToeBoard['3'])
    print(TicTacToeBoard['4']+'|'+TicTacToeBoard['5']+'|'+TicTacToeBoard['6'])
    print(TicTacToeBoard['7']+'|'+TicTacToeBoard['8']+'|'+TicTacToeBoard['9'])

def caseTie():
    print("---------------------------\nIt's a tie between "+player1+" & "+player2+"!")
    boardStatus()
    return 1

declareSymbol()
print("Press the corresponding key to place your position at each turn")

def printEmptyBoard():
    print("1|2|3")
    print("-----")
    print("4|5|6")
    print("-----")
    print("7|8|9")

printEmptyBoard()

while True:
    boardStatus()
    if turns == 9:
    	if caseTie() == 1:
            exit(1)
    while True:
        if player == 1:
            print(player1+"'s Turn:[Enter position]")
            playerturn = input()
            if playerturn in TicTacToeBoard and TicTacToeBoard[playerturn] == ' ':
                TicTacToeBoard[playerturn] = 'X'
                if winCheck():
                    boardStatus()
                    exit(1)
                player = 2
                break
            else:
                print("Wrong Input")
                continue
        else:
            print(player2+"'s Turn:[Enter position]")
            playerturn = input()
            if playerturn in TicTacToeBoard and TicTacToeBoard[playerturn] == ' ':
                TicTacToeBoard[playerturn] = 'O' 
                if winCheck() :
                    boardStatus()
                    exit(1) 
                player = 1
                break
            else:
                print("Wrong Input")
                continue
    turns = turns+1
    print("---------------------------")