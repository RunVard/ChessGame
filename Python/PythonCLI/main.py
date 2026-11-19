
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

def PrintCurrentBoard():
    print("\n    a   b   c   d   e   f   g   h")
    print("  #---------------------------------#")

    for r_idx, row in enumerate(board):
        rank_num = 8 - r_idx
        print(f"{rank_num} # ", end="")

        for cell in row:
            print(cell, end="   ")

        print(f"# {rank_num}")

    print("  #---------------------------------#")
    print("    a   b   c   d   e   f   g   h\n")



def getInputMove():
    inputV = input("\n \n Enter move (ex e2 e4)   : ")

    parts = inputV.strip().lower().split()

    if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2: 
        print("invalid format Use format like : e2 e4")
        return None

    c1, r1 = parts[0][0], parts[0][1]
    c2, r2 = parts[1][0], parts[1][1]

    if c1 not in "abcdefgh" or c2 not in "abcdefgh" or r1 not in "12345678" or r2 not in "12345678":
        print("Invalid squares")
        return None
    


    col1 = ord(c1) - 97
    row1 = 8 - int(r1)
    col2 = ord(c2) - 97
    row2 = 8 - int(r2)

    return col1, row1, col2, row2



def IsPathClear(c1, r1, c2, r2):
    cstep = 0 if c1 == c2 else (1 if c2 > c1 else -1)
    rstep = 0 if r1 == r2 else (1 if r2 > r1 else -1)

    currc = c1 + cstep
    currr = r1 + rstep

    while currc != c2 or currr != r2:
        if board [currr][currc] != ".":
            return False
        currc += cstep
        currr += rstep

    return True


def CheckIfCanMoveThere(c1, r1, c2, r2, piece):
    target = board[r2][c2]

    if target != ".":
        if piece.isupper() and target.isupper():
            return False
        if piece.islower() and target.islower():
            return False

    p_lower = piece.lower()

    if p_lower == "p":
        is_white = piece.isupper()
        direction = -1 if is_white else 1
        start_row = 6 if is_white else 1

        if c1 == c2:
            if r2 == r1 + direction and target == ".":
                return True
            
            if r1 == start_row and r2 == r1 + (2 * direction) and target == "." and board[r1 + direction][c1] == ".":
                return True
            
        elif abs(c1 - c2) == 1 and r2 == r1 + direction and target != ".":
            return True

        return False

    if p_lower == "r":
        if c1 != c2 and r1 != r2:
            return False
        return IsPathClear(c1, r1, c2, r2)


    return False








def main():
    while True:
        print("\033[H\033[2J", end="")
        PrintCurrentBoard()

        move = getInputMove()
        if move is None:
            continue
        
        c1, r1, c2, r2 = move

        piece = board[r1][c1]
        if piece == ".":
            print("No piece there")
            continue
        
        if CheckIfCanMoveThere(c1, r1, c2, r2, piece):
            board[r1][c1] = "."
            board[r2][c2] = piece
        else:
            print("Invalid move for that piece")






main()