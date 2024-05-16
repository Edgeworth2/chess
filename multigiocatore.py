import os
import time
from copy import deepcopy
from save import *

illegal_moves = []
global check
check = [False, "", [], []]

def multigiocatore():
    global board
    board = [
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]]
    choise = "!"
    if board1 != board or board1 == "":
        while choise != "y" and choise != "n" and choise != "Y" and choise != "N":
            choise = input("E' stata trovata una partita salvata automaticamente.\nSi desidera caricarla? [Y/N]")
            if choise != "y" and choise != "n" and choise != "Y" and choise != "N":
                print("La scelta non è valida, riprova.")
        if choise == "n" or choise == "N":
            turn(True)
        else:
            board = board1
            turn(boolean)
    elif board1 == board:
        turn(boolean)

def printboard(w, board):
    printingboard = deepcopy(board)
    for i in range(8):
        for j in range(8):
            match(printingboard[i][j]):
                case "  ":
                    printingboard[i][j] = " "
                case "BP":
                    printingboard[i][j] = "♙"
                case "BN":
                    printingboard[i][j] = "♘"
                case "BB":
                    printingboard[i][j] = "♗"
                case "BR":
                    printingboard[i][j] = "♖"
                case "BQ":
                    printingboard[i][j] = "♕"
                case "BK":
                    printingboard[i][j] = "♔"
                case "WP":
                    printingboard[i][j] = "♟"
                case "WN":
                    printingboard[i][j] = "♞"
                case "WB":
                    printingboard[i][j] = "♝"
                case "WR":
                    printingboard[i][j] = "♜"
                case "WQ":
                    printingboard[i][j] = "♛"
                case "WK":
                    printingboard[i][j] = "♚"
    match(w):
        case True:
            print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|--")
            for i in range(7, -1, -1):   
                for j in range(8):
                    print(f"{printingboard[i][j]} |", end="")
                print(f"{i+1}\n--|--|--|--|--|--|--|--|--")
        case False:
            print(f"H |G |F |E |D |C |B |A |\n--|--|--|--|--|--|--|--|--")
            for i in range(8):
                for j in range(7, -1, -1):
                    print(f"{printingboard[i][j]} |", end="")
                print(f"{i+1}\n--|--|--|--|--|--|--|--|--")

def saving(w):
    with open("save.py", "w") as save:
        save.write(f"board1 = {board}\n")
        if w:
            save.write("boolean = True")
        else:
            save.write("boolean = False")

def f_check(opponent, me):
    piece_moves = []
    possible_moves = []
    board_copy = deepcopy(board)
    for i in range(8):
        for j in range(8):
            piece_moves = []
            if board_copy[i][j][0] == me:
                match(board_copy[i][j][1]):
                    case "P":
                        pawn(i, j, piece_moves, opponent, False, board_copy)
                        p = "P"
                    case "N":
                        knight(i, j, piece_moves, opponent, False, board_copy)
                        p = "N"
                    case "B":
                        bishop(i, j, piece_moves, me, opponent, False, board_copy)
                        p = "B"
                    case "R":
                        rook(i, j, piece_moves, me, opponent, False, board_copy)
                        p = "R"
                    case "Q":
                        rook(i, j, piece_moves, me, opponent, False, board_copy)
                        bishop(i, j, piece_moves, me, opponent, False, board_copy)
                        p = "Q"
                    case "K":
                        king(i, j, piece_moves, me, opponent, False, board_copy)
                        p = "K"
                if piece_moves == []:
                    continue
                for moving in piece_moves:
                    board_copy[i][j] = "  "
                    board_copy[moving[0]][moving[1]] = f"{me}{p}"
                    attack(opponent, me, board_copy)
                    if check[0] == False:
                        possible_moves.append([i, j])
                        possible_moves.append(moving)
                    printboard(False, board_copy)
                    board_copy = deepcopy(board)
                    print(f"moving = {moving}")
    print(possible_moves)
    return possible_moves

def checking(op, y, x):
    check[0] = True
    check[1] = op
    if check[2] == []:
        check[2] = [y, x]
    else:
        check[3] = [y, x]

def attack(opponent, me, board):
    global check
    king = []
    enemy_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == f"{me}K":
                king = [i, j]
            if board[i][j][0] == opponent:
                match(board[i][j][1]):
                    case "P":
                        pawn(i, j, enemy_moves, me, True, board)
                    case "N":
                        knight(i, j, enemy_moves, me, True, board)
                    case "B":
                        bishop(i, j, enemy_moves, opponent, me, True, board)
                    case "R":
                        rook(i, j, enemy_moves, opponent, me, True, board)
                    case "Q":
                        rook(i, j, enemy_moves, opponent, me, True, board)
                        bishop(i, j, enemy_moves, opponent, me, True, board)
    if king in enemy_moves:
        check[0] = True
        check[1] = me
    else:
        check[0] = False
    return enemy_moves

def turn(w):
    global possible_moves
    possible_moves = []
    dowhile = True
    escapecheck = False
    saving(w)
    os.system("cls")
    global check
    global board
    alpha = "ABCDEFGH"
    nums = "12345678"
    match(w):
        case True:
            attack("B", "W", board)
            player = "Giocatore Bianco"
            printboard(True, board)
        case False:
            attack("W", "B", board)
            player = "Giocatore Nero"
            printboard(False, board)
    if check[0] == True and check[1] == "W":
        print("Il giocatore Bianco e' sotto scacco.")
        time.sleep(1.5)
        possible_moves = f_check("B", "W")
        if possible_moves == []:
            print("Il Nero vince per scacco matto!")
            exit()
        else:
            escapecheck = True
    elif check[0] == True and check[1] == "B":
        print("Il giocatore Nero e' sotto scacco.")
        time.sleep(1.5)
        possible_moves = f_check("W", "B")
        if possible_moves == []:
            print("Il Bianco vince per scacco matto!")
            exit()
        else:
            escapecheck = True
    while dowhile:
        start = input(f"{player}, Scegli Le coordinate della pedina che vuoi muovere. ")
        start = start.capitalize()
        dowhile = False
        if len(start) == 2 and start[0] in alpha and start[1] in nums:
            for i in range(8):
                if alpha[i] == start[0]:
                    x = i
                    break
            y = int(start[1])-1
            if board[y][x][0] == "W" and w == True or board[y][x][0] == "B" and w == False:
                if escapecheck == True:
                    if [y,x] not in possible_moves:
                        print("Questa pedina non ha alcun modo di fermare lo scacco. Riprova.")
                        time.sleep(3)
                        dowhile = True
                        continue
                if w == True:
                    white(y, x, board[y][x][1])
                else:
                    black(y, x, board[y][x][1])
            else:
                print("La casella selezionata non è valida.")
                time.sleep(1)
                if w == True:
                    turn(True)
                else:
                    turn(False)
        else:
            print("La casella selezionata non e' valida, riprova.")
            turn(w)

def white(y, x, p): 
    global board
    attack("B", "W", board)
    me = "W"
    op = "B"
    moves = []
    match(p):
        case "P":
            pawn(y, x, moves, op, False, board)
        case "N":
            knight(y, x, moves, op, False, board)
        case "B":
            bishop(y, x, moves, me, op, False, board)
        case "R":
            rook(y, x, moves, me, op, False, board)
        case "Q":
            bishop(y, x, moves, me, op, False, board)
            rook(y, x, moves, me, op, False, board)
        case "K":
            king(y, x, moves, me, op, False, board)
    if moves == []:
        print("Questa pedina non può eseguire mosse, riprova.")
        turn(True)
    moving(y, x, moves, p, True)
    turn(False)

def black(y, x, p):
    attack("W", "B", board)
    me = "B"
    op = "W"
    moves = []
    match(p):
        case "P":
            pawn(y, x, moves, op, False, board)
        case "N":
            knight(y, x, moves, op, False, board)
        case "B":
            bishop(y, x, moves, me, op, False, board)
        case "R":
            rook(y, x, moves, me, op, False, board)
        case "Q":
            bishop(y, x, moves, me, op, False, board)
            rook(y, x, moves, me, op, False, board)
        case "K":
            king(y, x, moves, me, op, False, board)
    if moves == []:
        print("Questa pedina non può eseguire mosse, riprova.")
        turn(False)
    moving(y, x, moves, p, False)
    turn(True)
               
def moving(y, x, moves, p, w):
    global illegal_moves
    dowhile = True
    while dowhile == True:
        move = input("Inserisci le coordinate della destinazione. ")
        move = move.capitalize()
        dowhile = False
        if len(move) == 2 and move[0] in "ABCDEFGH" and move[1] in "12345678":
            for i in range(8):
                if "ABCDEFGH"[i] == move[0]:
                    x1 = i
                    break
            y1 = int(move[1])-1
        if possible_moves != []:
            if [y1, x1] not in possible_moves:
                print("Quella mossa non ferma in alcun modo lo scacco, riprova.")
                time.sleep(2)
                dowhile = True
                continue
    if([y1, x1] in illegal_moves):
        print("Il Re non può muoversi in case controllate dall'avversario, riprova.")
        time.sleep(3)
        turn(w)
    elif([y1, x1] not in moves):
            print("Questa mossa non e' valida, riprova.")
            time.sleep(2)
            if w:
                white(y, x, p)
            else:
                black(y, x, p)
    elif w == True:
        board[y][x] = "  "
        match(p):
            case "P":
                board[y1][x1] = "WP"
            case "N":
                board[y1][x1] = "WN"
            case "B":
                board[y1][x1] = "WB"
            case "R":
                board[y1][x1] = "WR"
            case "Q":
                board[y1][x1] = "WQ"
            case "K":
                board[y1][x1] = "WK"
        print("mossa eseguita.")
        time.sleep(1)
        printboard(True, board)
    elif w == False:
        board[y][x] = "  "
        match(p):
            case "P":
                board[y1][x1] = "BP"
            case "N":
                board[y1][x1] = "BN"
            case "B":
                board[y1][x1] = "BB"
            case "R":
                board[y1][x1] = "BR"
            case "Q":
                board[y1][x1] = "BQ"
            case "K":
                board[y1][x1] = "BK"
        print("mossa eseguita.")
        time.sleep(1)
        printboard(False, board)
        

def king(y, x, moves, me, op, control, board):
    global illegal_moves
    illegal_moves = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j==0 and i==0:
                continue
            if [y+i, x+j] in attack(op, me, board):
                illegal_moves.append([y+i, x+j])
            if y+i >= 0 and y+i < 8 and x+j >= 0 and x+j < 8:
                if board[y+i][x+j][0] != f"{me}":
                    moves.append([y+i, x+j])

def pawn(y, x, moves, op, control, board):
    if op == "W":
        a = 7
        b = -1
        c = 0
    elif op == "B":
        a = 0
        b = 1
        c = 7
    if y == c:
        print("Promozione.")
    if not control:
        if board[y+(1*b)][x] == "  ":
            moves.append([y+(1*b),x])
        if y == (a + (1*b)) and board[y+(1*b)][x] == "  " and board[y+(2*b)][x] == "  ":
            moves.append([y+(2*b),x])
        if x != c and y != c:
            if board[y+(1*b)][x+(1*b)][0] == f"{op}":
                moves.append([y+(1*b),x+(1*b)])
                if board[y+(1*b)][x+(1*b)] == f"{op}K":
                    checking(op, y, x)    
        if y != c and x != a:
            if board[y+(1*b)][x-(1*b)][0] == f"{op}":
                moves.append([y+(1*b),x-(1*b)])   
                if board[y+(1*b)][x-(1*b)] == f"{op}K" :
                    checking(op, y, x)
    elif control:
        if x != c and y != c:
                moves.append([y+(1*b),x+(1*b)])
        if y != c and x != a:
            moves.append([y+(1*b),x-(1*b)])
        return moves       

def knight(y, x, moves, op, control, board):
    if y < 5 and x < 6:
        if board[y+2][x+1] == "  " or board[y+2][x+1][0] == f"{op}":
            moves.append([y+2,x+1])
            if board[y+2][x+1] == f"{op}K":
                checking(op, y, x)
    if y < 5 and x > 0:
        if board[y+2][x-1] == "  " or board[y+2][x-1][0] == f"{op}":
            moves.append([y+2,x-1])
            if board[y+2][x-1] == f"{op}K":
                checking(op, y, x)
    if y < 6 and x < 5:
        if board[y+1][x+2] == "  " or board[y+1][x+2][0] == f"{op}":
            moves.append([y+1,x+2])
            if board[y+2][x+1] == f"{op}K":
                    checking(op, y, x)
    if y < 6 and x > 2:
        if board[y+1][x-2] == "  " or board[y+1][x-2][0] == f"{op}":
            moves.append([y+1,x-2])
            if board[y+1][x-2] == f"{op}K":
                checking(op, y, x)
    if y > 0 and x < 5:
        if board[y-1][x+2] == "  " or board[y-1][x+2][0] == f"{op}":
            moves.append([y-1,x+2])
            if board[y-1][x+2] == f"{op}K":
                checking(op, y, x)
    if y > 0 and x > 1:
        if board[y-1][x-2] == "  " or board[y-1][x-2][0] == f"{op}":
            moves.append([y-1,x-2])
            if board[y-1][x-2] == f"{op}K":
                checking(op, y, x)
    if y > 1 and x < 6:
        if board[y-2][x+1] == "  " or board[y-2][x+1][0] == f"{op}":
            moves.append([y-2,x+1])
            if board[y-2][x+1] == f"{op}K":
                checking(op, y, x)
    if y > 1 and x > 0:
        if board[y-2][x-1] == "  " or board[y-2][x-1][0] == f"{op}":
            moves.append([y-2,x-1])
            if board[y-2][x-1] == f"{op}K":
                checking(op, y, x)
    if control:
        return moves

def rook(y, x, moves, me, op, control, board):
    for i in range(1, 8):
            if y+i < 8:
                if board[y+i][x][0] == f"{me}":
                    break
                elif board[y+i][x][0] == f"{op}":
                    moves.append([y+i, x])
                    if board[y+i][x][1] == "K":
                        checking(op, y, x)
                        if y+i < 8:
                            moves.append([y+i+1, x])
                    break
                elif board[y+i][x] == "  ":
                    moves.append([y+i, x])
    for i in range(1, 8):
        if y-i >= 0:
            if board[y-i][x][0] == f"{me}":
                break
            elif board[y-i][x][0] == f"{op}":
                moves.append([y-i, x])
                if board[y-i][x][1] == "K":
                    checking(op, y, x)
                    if y-i >= 0:
                        moves.append([y-i-1, x])
                break
            elif board[y-i][x] == "  ":
                moves.append([y-i, x])
    for i in range(1, 8):
        if x+i < 8:
            if board[y][x+i][0] == f"{me}":
                break
            elif board[y][x+i][0] == f"{op}":
                moves.append([y, x+i])
                if board[y][x+i][1] == "K":
                    checking(op, y, x)
                    if x+i < 8:
                        moves.append([y, x+i+1])
                break
            elif board[y][x+i] == "  ":
                moves.append([y, x+i])
    for i in range(1, 8):
        if x-i >= 0:
            if board[y][x-i][0] == f"{me}":
                break
            elif board[y][x-i][0] == f"{op}":
                moves.append([y, x-i])
                if board[y][x-i][1] == "K":
                        checking(op, y, x)
                        if x-i >= 0:
                            moves.append([y, x-i-1])
                break
            elif board[y][x-i] == "  ":
                moves.append([y, x-i])
    if control:
        return moves

def bishop(y, x, moves, me, op, control, board):
    for i in range(1, 8):
            if y+i < 8 and x+i < 8:
                if board[y+i][x+i][0] == f"{me}":
                    break
                elif board[y+i][x+i][0] == f"{op}":
                    moves.append([y+i, x+i])
                    if board[y+i][x+i][1] == "K":
                        checking(op, y, x)
                        if y+i < 8 and x+i < 8:
                            moves.append([y+i+1, x+i+1])
                    break
                elif board[y+i][x+i] == "  ":
                    moves.append([y+i, x+i])
    for i in range(1, 8):
        if y+i < 8 and x-i >= 0:
            if board[y+i][x-i][0] == f"{me}":
                break
            elif board[y+i][x-i][0] == f"{op}":
                moves.append([y+i, x-i])
                if board[y+i][x-i][1] == "K":
                    checking(op, y, x)
                    if y+i < 8 and x-i >= 0:
                        moves.append([y+i+1, x-i-1])
                break
            elif board[y+i][x-i] == "  ":
                moves.append([y+i, x-i])
    for i in range(1, 8):
        if y-i >= 0 and x+i < 8:
            if board[y-i][x+i][0] == f"{me}":
                break
            elif board[y-i][x+i][0] == f"{op}":
                moves.append([y-i, x+i])
                if board[y-i][x+i][1] == "K":
                    checking(op, y, x)
                    if y-i >= 0 and x+i < 8:
                        moves.append([y-i-1, x+i+1])
                break
            elif board[y-i][x+i] == "  ":
                moves.append([y-i, x+i])
    for i in range(1, 8):
        if y-i >= 0 and x-i >= 0:
            if board[y-i][x-i][0] == f"{me}":
                break
            elif board[y-i][x-i][0] == f"{op}":
                moves.append([y-i, x-i])
                if board[y-i][x-i][1] == "K":
                    checking(op, y, x)
                    if y-i >= 0 and x-i >= 0:
                        moves.append([y-i-1, x-i-1])
                break
            elif board[y-i][x-i] == "  ":
                moves.append([y-i, x-i])
    if control:
        return moves

multigiocatore()