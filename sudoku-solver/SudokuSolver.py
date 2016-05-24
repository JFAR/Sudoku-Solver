from SudokuBoard import SudokuBoard
import copy


def solver(inputBoard):
    sudokuBoard = solveIteration(sudokuSolver(SudokuBoard(inputBoard)))
    return sudokuBoard.returnBoard()


def sudokuSolver(sudokuBoard):
    if sudokuBoard is False:
        return False
    elif sudokuBoard.isSolved():
        return sudokuBoard
    else:
        cell = sudokuBoard.findFirstUnSetCell()
        for option in cell.getOptions():
            cell.set(option)
            newSudokuBoard = solveIteration(copy.deepcopy(sudokuBoard))
            if newSudokuBoard.isLegal():
                return sudokuSolver(newSudokuBoard)

        return False


def solveIteration(sudokuBoard):
    oldBoard = []
    newBoard = sudokuBoard.returnBoard()

    while newBoard != oldBoard:
        oldBoard = sudokuBoard.returnBoard()
        sudokuBoard.applyRowRule()
        sudokuBoard.applyColumnRule()
        sudokuBoard.applyBlockRule()

        newBoard = sudokuBoard.returnBoard()

    return sudokuBoard
