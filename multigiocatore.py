import os

def multigiocatore():
    global board
    board = [
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "WK", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]]
    turn(True)

def attack(y, x, op, me):
    global board
    enemy_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j][0] == op:
                match(board[i][j][1]):
                    case "P":
                        enemy_moves.append(pawn(i, j, enemy_moves, me, True))
                    case "R":
                        enemy_moves.append(rook(i, j, enemy_moves, op, me, True))
                    case "N":
                        enemy_moves.append(knight(i, j, enemy_moves, me, True))
                    case "B":
                        enemy_moves.append(bishop(i, j, enemy_moves, op, me, True))
                    case "Q":
                        enemy_moves.append(rook(i, j, enemy_moves, op, me, True))
                        enemy_moves.append(bishop(i, j, enemy_moves, op, me, True))
    for k in enemy_moves:
        for j in enemy_moves:
            if k==j:
                enemy_moves.remove(j) 
    if [y, x] in enemy_moves:
        return True
    else:
        return False

def turn(w):
    os.system("cls")
    global board
    attack(7, 5, "B", "W")
    alpha = "ABCDEFGH"
    nums = "12345678"
    if w == True:
        player = "Giocatore Bianco"
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(7, -1, -1):   
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")
    elif w == False:
        player = "Giocatore Nero"
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(8): 
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")
    start = input(f"{player}, Scegli Le coordinate della pedina che vuoi muovere. ")
    start = start.capitalize()
    print(start)
    if len(start) == 2 and start[0] in alpha and start[1] in nums:
        for i in range(8):
            if alpha[i] == start[0]:
                x = i
                break
        y = int(start[1])-1
        if board[y][x][0] == "W" and w == True or board[y][x][0] == "B" and w == False:
            print(board[y][x])
            if w == True:
                white(y, x, board[y][x][1])
            else:
                black(y, x, board[y][x][1])
        else:
            print("La casella selezionata non è valida.")
            if w == True:
                turn(True)
            else:
                turn(False)
    else:
        print("La casella selezionata non e' valida, riprova.")
        turn(w)

def white(y, x, p):
    me = "W"
    op = "B"
    global board
    print(x, y)
    moves = []
    match(p):
        case "P":
            pawn(y, x, moves, op, False)
        case "N":
            knight(y, x, moves, op, False)
        case "B":
            bishop(y, x, moves, me, op, False)
        case "R":
            rook(y, x, moves, me, op, False)
        case "Q":
            bishop(y, x, moves, me, op, False)
            rook(y, x, moves, me, op, False)
        case "K":
            king(y, x, moves, me, op, False)
    if moves == []:
        print("Questa pedina non può eseguire mosse, riprova.")
        turn(True)
    moving(y, x, moves, p, True)
    turn(False)

def black(y, x, p):
    me = "B"
    op = "W"
    global board
    moves = []
    match(p):
        case "P":
            pawn(y, x, moves, op, False)
        case "N":
            knight(y, x, moves, op, False)
        case "B":
            bishop(y, x, moves, me, op, False)
        case "R":
            rook(y, x, moves, me, op, False)
        case "Q":
            bishop(y, x, moves, me, op, False)
            rook(y, x, moves, me, op, False)
        case "K":
            king(y, x, moves, me, op, False)
    if moves == []:
        print("Questa pedina non può eseguire mosse, riprova.")
        turn(False)
    moving(y, x, moves, p, False)
    turn(True)
               
def moving(y, x, moves, p, w):
    move = input("Inserisci le coordinate della destinazione. ")
    move = move.capitalize()
    if len(move) == 2 and move[0] in "ABCDEFGH" and move[1] in "12345678":
        for i in range(8):
            if "ABCDEFGH"[i] == move[0]:
                x1 = i
                break
        y1 = int(move[1])-1
    print([y1, x1])
    if([y1, x1] not in moves):
            print("Questa mossa non e' valida, riprova.")
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
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(7, -1, -1):
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")
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
                board[y1][x1] = "WK"
        print("mossa eseguita.")
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(8): 
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")

def king(y, x, moves, me, op, control):
    global board
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j==0 and i==0:
                continue
            elif board[y+i][x+j][0] != me and (attack(y+i, x+j, op, me) == False):
                moves.append([y+i, x+j])
        print(moves)

def pawn(y, x, moves, op, control):
    if op == "W":
        a = 7
        b = -1
        c = 0
    elif op == "B":
        a = 0
        b = 1
        c = 7
    if y == a:
        print("Promozione.")
    if not control:
        if board[y+(1*b)][x] == "  ":
            moves.append([y+(1*b),x])
        if y == (a + (1*b)) and board[y+(1*b)][x] == "  " and board[y+(2*b)][x] == "  ":
            moves.append([y+(2*b),x])
        if x != c and y != c:
            if board[y+(1*b)][x+(1*b)][0] == f"{op}":
                moves.append([y+(1*b),x+(1*b)])
        if y != c and x != a:
            if board[y+(1*b)][x-(1*b)][0] == f"{op}":
                moves.append([y+(1*b),x-(1*b)])    
    else:
        if x != c and y != c:
            if board[y+(1*b)][x+(1*b)] == "  ":
                moves.append([y+(1*b),x+(1*b)])
        if y != c and x != a:
            if board[y+(1*b)][x-(1*b)] == "  ":
                moves.append([y+(1*b),x-(1*b)])
        return moves
        

def knight(y, x, moves, op, control):
    if y < 5 and x < 6:
        if board[y+2][x+1] == "  " or board[y+2][x+1][0] == f"{op}":
            moves.append([y+2,x+1])
    if y < 5 and x > 0:
        if board[y+2][x-1] == "  " or board[y+2][x-1][0] == f"{op}":
            moves.append([y+2,x-1])
    if y < 6 and x < 5:
        if board[y+1][x+2] == "  " or board[y+1][x+2][0] == f"{op}":
            moves.append([y+1,x+2])
    if y < 6 and x > 2:
        if board[y+1][x-2] == "  " or board[y+1][x-2][0] == f"{op}":
            moves.append([y+1,x-2])
    if y > 0 and x < 5:
        if board[y-1][x+2] == "  " or board[y-1][x+2][0] == f"{op}":
            moves.append([y-1,x+2])
    if y > 0 and x > 1:
        if board[y-1][x-2] == "  " or board[y-1][x-2][0] == f"{op}":
            moves.append([y-1,x-2])
    if y > 1 and x < 6:
        if board[y-2][x+1] == "  " or board[y-2][x+1][0] == f"{op}":
            moves.append([y-2,x+1])
    if y > 1 and x > 0:
        if board[y-2][x-1] == "  " or board[y-2][x-1][0] == f"{op}":
            moves.append([y-2,x-1])
    if control:
        return moves

def rook(y, x, moves, me, op, control):
    for i in range(1, 8):
            if y+i < 8:
                if board[y+i][x][0] == f"{me}":
                    break
                elif board[y+i][x][0] == f"{op}":
                    moves.append([y+i, x])
                    break
                elif board[y+i][x] == "  ":
                    moves.append([y+i, x])
    for i in range(1, 8):
        if y-i >= 0:
            if board[y-i][x][0] == f"{me}":
                break
            elif board[y-i][x][0] == f"{op}":
                moves.append([y-i, x])
                break
            elif board[y-i][x] == "  ":
                moves.append([y-i, x])
    for i in range(1, 8):
        if x+i < 8:
            if board[y][x+i][0] == f"{me}":
                break
            elif board[y][x+i][0] == f"{op}":
                moves.append([y, x+i])
                break
            elif board[y][x+i] == "  ":
                moves.append([y, x+i])
    for i in range(1, 8):
        if x-i >= 0:
            if board[y][x-i][0] == f"{me}":
                break
            elif board[y][x-i][0] == f"{op}":
                moves.append([y, x-i])
                break
            elif board[y][x-i] == "  ":
                moves.append([y, x-i])
    if control:
        return moves

def bishop(y, x, moves, me, op, control):
    for i in range(1, 8):
            if y+i < 8 and x+i < 8:
                if board[y+i][x+i][0] == f"{me}":
                    break
                elif board[y+i][x+i][0] == f"{op}":
                    moves.append([y+i, x+i])
                    break
                elif board[y+i][x+i] == "  ":
                    moves.append([y+i, x+i])
    for i in range(1, 8):
        if y+i < 8 and x-i >= 0:
            if board[y+i][x-i][0] == f"{me}":
                break
            elif board[y+i][x-i][0] == f"{op}":
                moves.append([y+i, x-i])
                break
            elif board[y+i][x-i] == "  ":
                moves.append([y+i, x-i])
    for i in range(1, 8):
        if y-i >= 0 and x+i < 8:
            if board[y-i][x+i][0] == f"{me}":
                break
            elif board[y-i][x+i][0] == f"{op}":
                moves.append([y-i, x+i])
                break
            elif board[y-i][x+i] == "  ":
                moves.append([y-i, x+i])
    for i in range(1, 8):
        if y-i >= 0 and x-i >= 0:
            if board[y-i][x-i][0] == f"{me}":
                break
            elif board[y-i][x-i][0] == f"{op}":
                moves.append([y-i, x-i])
                break
            elif board[y-i][x-i] == "  ":
                moves.append([y-i, x-i])
    if control:
        return moves
    
multigiocatore()
