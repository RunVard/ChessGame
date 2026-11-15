
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
    inputV = input("\n \n Enter move (e.g e2 e4)   : ")

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



def CheckWhatInBox(c1, r1):
    value = board[c1][r1]
    return value





def main():
    PrintCurrentBoard()
    c1, r1, c2, r2, = getInputMove()
    pawn = CheckWhatInBox(c1, r1)
    print (pawn)




main()