import unittest
import SudokuCell


class SudokuCellTest(unittest.TestCase):
    def test_checkIsSetWithNoOptions(self):
        cell = SudokuCell.Cell(0, 0)
        self.assertFalse(cell.isSet())

    def test_checkIsSetWithMoreThanOneOption(self):
        cell = SudokuCell.Cell(0, 0, [1, 2, 3])
        self.assertFalse(cell.isSet())

    def test_checkIsSetWithMoreThanOneOption(self):
        cell = SudokuCell.Cell(0, 0, [1])
        self.assertTrue(cell.isSet())
