from SudokuBoard import SudokuBoard


def checkContainsNumbers(listOfNumbers):
    for i in range(9):
        if (i + 1) not in listOfNumbers:
            return False

    return True


def checkBoard(board):
    sudokuBoard = SudokuBoard(board)
    for i in range(9):
        if checkContainsNumbers(sudokuBoard.returnRowById(i)) is False:
            return False

        if checkContainsNumbers(sudokuBoard.returnColumnById(i)) is False:
            return False

        rowId = i % 3
        columnId = int((i - rowId) / 3)

        if checkContainsNumbers(sudokuBoard.returnBlockByIds(rowId, columnId)) is False:
            return False

    return True


def solver(inputBoard):
    oldBoard = []
    newBoard = inputBoard
    sudokuBoard = SudokuBoard(inputBoard)
    while (checkBoard(newBoard) is False) and (newBoard != oldBoard):
        oldBoard = newBoard
        sudokuBoard.applyRowRule()
        sudokuBoard.applyColumnRule()
        newBoard = sudokuBoard.returnBoard()

    return newBoard
