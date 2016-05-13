from SudokuBoard import SudokuBoard


def solver(inputBoard):
    oldBoard = []
    newBoard = inputBoard
    sudokuBoard = SudokuBoard(inputBoard)

    while (sudokuBoard.isSolved() is False) and (newBoard != oldBoard):
        sudokuBoard.applyRowRule()
        sudokuBoard.applyColumnRule()
        sudokuBoard.applyBlockRule()

        oldBoard = newBoard
        newBoard = sudokuBoard.returnBoard()

    return newBoard
