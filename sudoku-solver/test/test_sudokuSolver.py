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
        easySudoku = [[7, 5, 0,  0, 4, 2,  0, 6, 9],
                      [2, 4, 3,  0, 9, 0,  0, 0, 8],
                      [0, 0, 0,  1, 0, 7,  0, 4, 0],

                      [0, 1, 0,  6, 5, 0,  8, 9, 7],
                      [0, 0, 8,  0, 0, 0,  4, 0, 0],
                      [6, 7, 9,  0, 8, 4,  0, 3, 0],

                      [0, 6, 0,  4, 0, 5,  0, 0, 0],
                      [8, 0, 0,  0, 6, 0,  2, 7, 4],
                      [1, 2, 0,  9, 7, 0,  0, 5, 3]]

        solvedSudoku = [[7, 5, 1,  8, 4, 2,  3, 6, 9],
                        [2, 4, 3,  5, 9, 6,  7, 1, 8],
                        [9, 8, 6,  1, 3, 7,  5, 4, 2],

                        [4, 1, 2,  6, 5, 3,  8, 9, 7],
                        [5, 3, 8,  7, 1, 9,  4, 2, 6],
                        [6, 7, 9,  2, 8, 4,  1, 3, 5],

                        [3, 6, 7,  4, 2, 5,  9, 8, 1],
                        [8, 9, 5,  3, 6, 1,  2, 7, 4],
                        [1, 2, 4,  9, 7, 8,  6, 5, 3]]

        self.assertEqual(SudokuSolver.solver(easySudoku), solvedSudoku)

    @unittest.skip("Can't solve this one yet!")
    def test_solvesMediumSudoku(self):
        mediumSudoku = [[1, 3, 0,  8, 0, 0,  6, 5, 2],
                        [0, 0, 2,  0, 0, 7,  0, 0, 0],
                        [0, 0, 0,  1, 2, 0,  0, 7, 9],

                        [2, 8, 0,  0, 0, 0,  0, 0, 0],
                        [0, 9, 0,  0, 3, 0,  0, 1, 0],
                        [0, 0, 0,  0, 0, 0,  0, 2, 3],

                        [5, 7, 0,  0, 8, 3,  0, 0, 0],
                        [0, 0, 0,  4, 0, 0,  9, 0, 0],
                        [0, 0, 9,  0, 0, 2,  0, 6, 7]]

        solvedSudoku = [[1, 3, 7,  8, 4, 9,  6, 5, 2],
                        [9, 5, 2,  3, 6, 7,  1, 8, 4],
                        [4, 6, 8,  1, 2, 5,  3, 7, 9],

                        [2, 8, 3,  7, 5, 1,  4, 9, 6],
                        [6, 9, 5,  2, 3, 4,  7, 1, 8],
                        [7, 1, 4,  6, 9, 8,  5, 2, 3],

                        [5, 7, 6,  9, 8, 3,  2, 4, 1],
                        [8, 2, 1,  4, 7, 6,  9, 3, 5],
                        [3, 4, 9,  5, 1, 2,  8, 6, 7]]

        self.assertEqual(SudokuSolver.solver(mediumSudoku), solvedSudoku)

    def test_solvesEasySudoku(self):
        inputBoard = copy.deepcopy(self.outputBoard)
        inputBoard[8][8] = 0
        self.assertEqual(SudokuSolver.solver(inputBoard), self.outputBoard)
