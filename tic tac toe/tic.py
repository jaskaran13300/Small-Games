board=[" "," "," "," "," "," "," "," "," "]
filled=0
reservedIndexes=[]
def display_board():
        for i in range(0,9,3):
            print(board[i] +"|"+ board[i+1] +"|"+ board[i+2])
            if i!=6:
                print("-----")
def iniliase(board,filled,reservedIndexes):
    board=[" "," "," "," "," "," "," "," "," "]
    display_board()
    filled=0
    reservedIndexes=[]
iniliase(board,filled,reservedIndexes)
def check_winner(board,ch):
    for i in range(0,9,3):
        if board[i]==ch and board[i+1]==ch and board[i+2]==ch:
            return True
    for i in range(0,3,1):
        if board[i]==ch and board[i+3]==ch and board[i+6]==ch:
            return True
    
    if board[0]==ch and board[4]==ch and board[8]==ch:
        return True

    if board[2]==ch and board[4]==ch and board[6]==ch:
        return True
    return False

    return False
while filled<9:
    print("For Cross Player 1: ")
    crossStr=input()
    try:
        cross=int(crossStr)
        if not (cross>=1 and cross<=9):

            print("Invalid Number")
            continue
    except:
        print("Characters are not allowed")
        continue
    if(cross in reservedIndexes):
        print("Can not update this location try another! ")
        # continue
        while cross in reservedIndexes:
            crossStr=input("Try Another Location for Player 1")
            cross=int(crossStr)
    board[cross-1]='X'
    if(check_winner(board,'X')):
        print('Player 1 Wins!!')
        print("Congratulations!!")
        break
    if(check_winner(board,'0')):
        print('Player 2 Wins!!')
        print("Congratulations!!")
        break
    reservedIndexes.append(cross)
    display_board()
    filled=filled+1
    if filled>=9:
        print("Game is tie")
        display_board()
        break
    print("For Zero Player 2: ")
    ZeroStr=input()
    try:
        Zero=int(ZeroStr)
        if not (Zero>=1 and Zero<=9):
            print("Invalid Number !! ")
            Zero=-1
            while not (Zero>=1 and Zero<=9):
                Zero=-1
                ZeroStr=input()
                try:
                    Zero=int(ZeroStr)
                    if not (Zero>=1 and Zero<=9):
                        print("Invalid Number! ")
                        continue
                except:
                    print("Characters are not allowed ! ")
                    continue
    except:
        print("Invalid Number ! ")
        Zero=-1
        while not (Zero>=1 and Zero<=9):
            Zero=-1
            ZeroStr=input()
            try:
                Zero=int(ZeroStr)
                if not (Zero>=1 and Zero<=9):
                    print("Invalid Number !! ")
                    continue
            except:
                print("Invalid Number !! ")
                continue
    if(Zero in reservedIndexes):
        print("Can not update this location try another!")
        while Zero in reservedIndexes:
            ZeroStr=input("Try Another Location for ZERO Player 2: ")
            Zero=int(ZeroStr)
        # continue
    board[Zero-1]='0'
    if(check_winner(board,'X')):
        print('Player 1 Wins!!')
        break
    if(check_winner(board,'0')):
        print('Player 2 wins!!')
        break
    filled=filled+1
    reservedIndexes.append(Zero)
    display_board()
