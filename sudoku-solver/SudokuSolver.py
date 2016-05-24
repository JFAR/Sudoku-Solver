from SudokuBoard import SudokuBoard
import copy


def solver(inputBoard):
    sudokuBoard = solveIteration(sudokuSolver(SudokuBoard(inputBoard)))
    outputBoard = sudokuBoard.returnBoard()
    return outputBoard


def sudokuSolver(sudokuBoard):
    if sudokuBoard is False:
        return False
    elif sudokuBoard.isLegal() is False:
        return False
    else:
        solveIteration(sudokuBoard)

    if sudokuBoard.isSolved():
        return sudokuBoard
    else:
        solveIteration(sudokuBoard)
        cell = sudokuBoard.findFirstUnSetCell()
        for option in cell.getOptions():
            potentialSolution = copy.deepcopy(sudokuBoard)
            potentialCell = potentialSolution.getCell(cell.getRowId(), cell.getColumnId())
            potentialCell.set(option)

            newSudokuBoard = sudokuSolver(solveIteration(potentialSolution))

            if newSudokuBoard is not False:
                return newSudokuBoard

        return False


def prettyPrint(board):
    for row in board:
        print(row)
    print()


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
