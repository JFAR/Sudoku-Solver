from SudokuCell import Cell
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
    while checkBoard(inputBoard) is False and oldBoard != inputBoard:
        oldBoard = inputBoard
        sudokuBoard = SudokuBoard(inputBoard)
        for cellWithOptions in sudokuBoard.findCellsWithOptions():
            sudokuBoard.reduceCellOptions(cellWithOptions.getRowId(), cellWithOptions.getColumnId())

        inputBoard = sudokuBoard.returnBoard()

    return inputBoard
