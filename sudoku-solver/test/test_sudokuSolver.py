import unittest
import copy
import SudokuSolver


class SudokuTest(unittest.TestCase):
    outputBoard = [[2, 5, 1,  7, 6, 3,  9, 4, 8],
                   [9, 7, 4,  2, 5, 8,  6, 3, 1],
                   [3, 8, 6,  4, 9, 1,  2, 7, 5],

                   [5, 4, 8,  9, 1, 2,  3, 6, 7],
                   [7, 6, 3,  8, 4, 5,  1, 9, 2],
                   [1, 2, 9,  6, 3, 7,  5, 8, 4],

                   [6, 9, 5,  1, 8, 4,  7, 2, 3],
                   [8, 1, 2,  3, 7, 6,  4, 5, 9],
                   [4, 3, 7,  5, 2, 9,  8, 1, 6]]

    def test_solvesCompletedSudoku(self):
        inputBoard = self.outputBoard
        self.assertEqual(SudokuSolver.solver(inputBoard), self.outputBoard)

    def test_reduceOptionsReducesOptions(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuSolver.SudokuBoard(inputBoard)
        completeSudokuBoard = SudokuSolver.SudokuBoard(self.outputBoard)
        sudokuBoard.applyRowRuleForId(8)
        self.assertEqual([cell.getOptions()[0] for cell in sudokuBoard.getRowById(8) if cell.isSet()], [cell.getOptions()[0] for cell in completeSudokuBoard.getRowById(8)])

    def test_removeOptions(self):
        cell = SudokuSolver.Cell(0, 0)
        cell.removeOptions([1, 2, 3])
        self.assertListEqual(cell.getOptions(), [4, 5, 6, 7, 8, 9])

    def test_returnSetCellsInRowAsNumbers(self):
        sudokuBoard = SudokuSolver.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnRowById(8), [4, 3, 7, 5, 2, 9, 8, 1, 6])

    def test_returnSetCellsInColumnAsNumbers(self):
        sudokuBoard = SudokuSolver.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnColumnById(8), [8, 1, 5, 7, 2, 4, 3, 9, 6])

    def test_returnCellBlockIds(self):
        cell = SudokuSolver.Cell(8, 5)
        self.assertListEqual(cell.getBlockIds(), [2, 1])

    def test_returnSetCellsInBlockAsNumbers(self):
        sudokuBoard = SudokuSolver.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnBlockByIds(2, 2), [7, 2, 3, 4, 5, 9, 8, 1, 6])

    @unittest.skip("skip")
    def test_solvesSimpleSudoku(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        self.assertEqual(SudokuSolver.solver(inputBoard), self.outputBoard)

    def test_checkBoardCorrect(self):
        self.assertTrue(SudokuSolver.checkBoard(self.outputBoard))

    def test_checkBoardIncorrect(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        self.assertFalse(SudokuSolver.checkBoard(inputBoard))

    def test_returnBoardReturnsSameCompleteBoard(self):
        self.assertEqual(SudokuSolver.SudokuBoard(self.outputBoard).returnBoard(), self.outputBoard)

    def test_returnBoardReturnsSameCompleteBoard(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        self.assertEqual(SudokuSolver.SudokuBoard(inputBoard).returnBoard(), inputBoard)
