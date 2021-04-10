import random


def printgame(cells):
    print("---------")
    for i in range(3):
        print("|", end=' ')
        for j in range(3):
            print(cells[i][j], end=" ")
        print("|")
    print("---------")


def checkWinner(cells):
    for i in range(3):
        if all(cells[i][j] == 'X' for j in range(3)) or \
                all(cells[j][i] == 'X' for j in range(3)):
            print("X wins")
            exit(0)
        elif all(cells[i][j] == 'O' for j in range(3)) or \
                all(cells[j][i] == 'O' for j in range(3)):
            print("O wins")
            exit(0)
    if all(cells[i][i] == 'X' for i in range(3)) or \
            all(cells[i][-(i + 1)] == 'X' for i in range(3)):
        print("X wins")
        exit(0)
    elif all(cells[i][i] == 'O' for i in range(3)) or \
            all(cells[i][-(i + 1)] == 'O' for i in range(3)):
        print("O wins")
        exit(0)
    # if any(cells[i][j] == ' ' for i in range(3) for j in range(3)):
    #    return 'Game not finished'
    if all(cells[i][j] != ' ' for i in range(3) for j in range(3)):
        print('Draw')
        exit(0)


def main():
    cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    x = 0
    y = 0
    user = 1
    printgame(cells)
    while True:
        if user == 1:
            try:
                x, y = map(int, input("Enter the coordinates:").split())
            except ValueError:
                print("You should enter numbers!")
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif (cells[x - 1][y - 1]) == "X" or (cells[x - 1][y - 1]) == "O":
                print("This cell is occupied! Choose another one!")
            cells[x - 1][y - 1] = "X"
            user = 0
        elif user == 0:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while cells[x - 1][y - 1] != " ":
                x = random.randint(1, 3)
                y = random.randint(1, 3)
            print('Making move level "easy"')
            cells[x - 1][y - 1] = "O"
            user = 1
        printgame(cells)
        checkWinner(cells)


main()
