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

    def test_returnBoardReturnsSameBoard(self):
        self.assertEqual(SudokuSolver.SudokuBoard(self.outputBoard).returnBoard(), self.outputBoard)


if __name__ == '__main__':
    unittest.main()
