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
    turn(True)

def attack(y, x, me, op):
    global board, controlled
    controlled = []
    for i in board:
        if i[0] == op:
            if i[1] == "P":
                pawn(y, x, controlled, me, op, True)
            elif i[1] == "R":
                rook(y, x, controlled, me, op, True)
            elif i[1] == "B":
                bishop(y, x, controlled, me, op, True)
            elif i[1] == "K":
                knight(y, x, controlled, me, op, True)
            elif i[1] == "Q":
                rook(y, x, controlled, me, op, True)
                bishop(y, x, controlled, me, op, True)
    print(controlled)

def controller_fill(moves):
    global controlled
    if len(controlled) == 0:
            controlled.append(moves[0])
    for i in controlled:
        for j in range(len(moves)):
            if i==moves[j]:
                break
            else:
                controlled.append(moves[j])
    
def turn(w):
    global board
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
        print("La casella selezionata non e' valida.")

def white(y, x, p):
    me = "W"
    op = "B"
    global board
    print(x, y)
    moves = []
    if p == "P":
        pawn(y, x, moves, op, False)
    if p == "N":
        knight(y, x, moves, op, False)
    if p == "B":
        bishop(y, x, moves, me, op, False)
    if p == "R":
        rook(y, x, moves, me, op, False)
    if p == "Q":
        bishop(y, x, moves, me, op, False)
        rook(y, x, moves, me, op, False)
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
    if p == "P":
        pawn(y, x, moves, op, False)
    if p == "N":
        knight(y, x, moves, op, False)
    if p == "B":
        bishop(y, x, moves, me, op, False)
    if p == "R":
        rook(y, x, moves, me, op, False)
    if p == "Q":
        bishop(y, x, moves, me, op, False)
        rook(y, x, moves, me, op, False)
    if moves == []:
        print("Questa pedina non può eseguire mosse, riprova.")
        turn(False)
    moving(y, x, moves, p, False)
    turn(True)
               
def moving(y, x, moves, p, w):
    move = input("Inserisci le coordinate della destinazione. ")        
    if len(move) == 2 and move[0] in "ABCDEFGH" and move[1] in "12345678":
        for i in range(8):
            if "ABCDEFGH"[i] == move[0]:
                x1 = i
                break
        y1 = int(move[1])-1
    print([y1, x1])
    if([y1, x1] not in moves):
            print("Questa mossa non e' valida, riprova.")
            white(y, x, p)
    elif w == True:
        board[y][x] = "  "
        if p == "P":
            board[y1][x1] = "WP"
        elif p == "N":
            board[y1][x1] = "WN"
        elif p == "B":
            board[y1][x1] = "WB"
        elif p == "R":
            board[y1][x1] = "WR"
        elif p == "Q":
            board[y1][x1] = "WQ"
        print("mossa eseguita.")
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(7, -1, -1):
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")
    elif w == False:
        board[y][x] = "  "
        if p == "P":
            board[y1][x1] = "BP"
        elif p == "N":
            board[y1][x1] = "BN"
        elif p == "B":
            board[y1][x1] = "BB"
        elif p == "R":
            board[y1][x1] = "BR"
        elif p == "Q":
            board[y1][x1] = "BQ"
        print("mossa eseguita.")
        print(f"A |B |C |D |E |F |G |H |\n--|--|--|--|--|--|--|--|-")
        for i in range(8): 
            for j in range(8):
                print(f"{board[i][j]}|", end="")
            print(f"{i+1}\n--|--|--|--|--|--|--|--|-")

def king(y, x, moves, me, op, control):
    if (board[y+1][x+1] == "  " or board[y+1][x+1][0] == f"{op}") and attack(x, y, me, op) == False:
        pass


def pawn(y, x, moves, op, control):
    global controlled
    if op == "B":
        if y == 7:
            print("Promozione.")
        if board[y+1][x] == "  ":
            moves.append([y+1,x])
        if y == 1 and board[y+1][x] == "  " and board[y+2][x] == "  ":
            moves.append([y+2,x])
        if x != 7 and y != 7:
            if board[y+1][x+1][0] == f"{op}":
                moves.append([y+1,x+1])
        if y != 7 and x != 0:    
            if board[y+1][x-1][0] == f"{op}":
                moves.append([y+1,x-1])
    elif op == "W":
        if y == 0:
            print("Promozione.")
        if board[y-1][x] == "  ":
            moves.append([y-1,x])
        if y == 6 and board[y-1][x] == "  " and board[y-2][x] == "  ":
            moves.append([y-2,x])
        if x != 0 and y != 0:
            if board[y-1][x-1][0] == f"{op}":
                moves.append([y-1,x-1])
        if y != 0 and x != 7:    
            if board[y-1][x+1][0] == f"{op}":
                moves.append([y-1,x+1])
    if control == False:
        return
    else:
        controller_fill(moves)
        

def knight(y, x, moves, op, control):
    global controlled
    if y < 5 and x < 6:
        if board[y+2][x+1] == "  " or board[y+2][x+1][0] == f"{op}":
            moves.append([y+2,x+1])
    if y < 5 and x > 0:
        if board[y+2][x-1] == "  " or board[y+2][x-1][0] == f"{op}":
            moves.append([y+2,x-1])
    if y < 6 and x < 5:
        if board[y+1][x+2] == "  " or board[y+1][x+2][0] == f"{op}":
            moves.append([y+2,x+1])
    if y < 6 and x > 2:
        if board[y+1][x-2] == "  " or board[y+1][x-2][0] == f"{op}":
            moves.append([y+2,x+1])
    if y > 0 and x < 5:
        if board[y-1][x+2] == "  " or board[y-1][x+2][0] == f"{op}":
            moves.append([y+2,x+1])
    if y > 0 and x > 1:
        if board[y-1][x-2] == "  " or board[y-1][x-2][0] == f"{op}":
            moves.append([y+2,x+1])
    if y > 1 and x < 6:
        if board[y-2][x+1] == "  " or board[y-2][x+1][0] == f"{op}":
            moves.append([y+2,x+1])
    if y > 1 and x > 0:
        if board[y-2][x-1] == "  " or board[y-2][x-1][0] == f"{op}":
            moves.append([y+2,x+1])
    if control == False:
        return
    else:
        controller_fill(moves)

def rook(y, x, moves, me, op, control):
    global controlled
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
    if control == False:
        return
    else:
        controller_fill(moves)

def bishop(y, x, moves, me, op, control):
    global controlled
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
    if control == False:
        return
    else:
        controller_fill(moves)

multigiocatore()