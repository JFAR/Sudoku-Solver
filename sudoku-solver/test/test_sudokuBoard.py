import unittest
import SudokuBoard
import copy


class SudokuBoardTest(unittest.TestCase):
    outputBoard = [[2, 5, 1,  7, 6, 3,  9, 4, 8],
                   [9, 7, 4,  2, 5, 8,  6, 3, 1],
                   [3, 8, 6,  4, 9, 1,  2, 7, 5],

                   [5, 4, 8,  9, 1, 2,  3, 6, 7],
                   [7, 6, 3,  8, 4, 5,  1, 9, 2],
                   [1, 2, 9,  6, 3, 7,  5, 8, 4],

                   [6, 9, 5,  1, 8, 4,  7, 2, 3],
                   [8, 1, 2,  3, 7, 6,  4, 5, 9],
                   [4, 3, 7,  5, 2, 9,  8, 1, 6]]

    def test_returnBoardReturnsSameCompleteBoard(self):
        self.assertEqual(SudokuBoard.SudokuBoard(self.outputBoard).returnBoard(), self.outputBoard)

    def test_returnBoardReturnsSameIncompleteBoard(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        self.assertEqual(SudokuBoard.SudokuBoard(inputBoard).returnBoard(), inputBoard)

    def test_reduceOptionsReducesOptions(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        completeSudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        sudokuBoard.applyRowRuleForId(8)
        self.assertEqual([cell.getOptions()[0] for cell in sudokuBoard.getRowById(8) if cell.isSet()], [cell.getOptions()[0] for cell in completeSudokuBoard.getRowById(8)])

    def test_reduceOptionsReducesOptionsWithColumnRule(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        completeSudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        sudokuBoard.applyColumnRuleForId(8)
        self.assertEqual([cell.getOptions()[0] for cell in sudokuBoard.getRowById(8) if cell.isSet()], [cell.getOptions()[0] for cell in completeSudokuBoard.getRowById(8)])

    def test_reduceOptionsReducesOptionsWithBlockRule(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        completeSudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        sudokuBoard.applyBlockRuleForId(8)
        self.assertEqual([cell.getOptions()[0] for cell in sudokuBoard.getBlockById(8) if cell.isSet()], [cell.getOptions()[0] for cell in completeSudokuBoard.getBlockById(8)])

    def test_getBlockById(self):
        sudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        self.assertEqual(sudokuBoard.getBlockById(8), sudokuBoard.getBlockByIds(2, 2))

    def test_returnSetCellsInRowAsNumbers(self):
        sudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnRowById(8), [4, 3, 7, 5, 2, 9, 8, 1, 6])

    def test_returnSetCellsInColumnAsNumbers(self):
        sudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnColumnById(8), [8, 1, 5, 7, 2, 4, 3, 9, 6])

    def test_returnSetCellsInBlockAsNumbers(self):
        sudokuBoard = SudokuBoard.SudokuBoard(self.outputBoard)
        self.assertListEqual(sudokuBoard.returnBlockById(8), [7, 2, 3, 4, 5, 9, 8, 1, 6])

    def test_applyRowRuleSolvesSimpleSudoku(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        sudokuBoard.applyRowRule()
        self.assertListEqual(sudokuBoard.returnBoard(), self.outputBoard)

    def test_applyColumnRuleSolvesSimpleSudoku(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        sudokuBoard.applyColumnRule()
        self.assertListEqual(sudokuBoard.returnBoard(), self.outputBoard)

    def test_applyBlockRuleSolvesSimpleSudoku(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        sudokuBoard = SudokuBoard.SudokuBoard(inputBoard)
        sudokuBoard.applyBlockRule()
        self.assertListEqual(sudokuBoard.returnBoard(), self.outputBoard)
