
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

def PrintLine(lineNumber):
    print("#", end=" ")
    i = 0
    while i < 8:
        print(board[lineNumber][i], end="  ")
        i = i + 1

    print("#", end="")

    print("\n")
    return


def PrintCurrentBoard():
    i = 0
    while i <= 9:
        if i == 0 or i == 9:
            print("  #  #  #  #  #  #  #  #")
        else:
            PrintLine(i - 1)

        i = i + 1

    return


def getInputMove():
    inputV = input("\n \n Enter move (e.g e2 e4)")
    print(inputV)


def CanMoveThere():
    print()


def main():
    PrintCurrentBoard()
    getInputMove()




main()