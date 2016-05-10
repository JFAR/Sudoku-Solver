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

    def test_removeOptions(self):
        cell = SudokuCell.Cell(0, 0)
        cell.removeOptions([1, 2, 3])
        self.assertListEqual(cell.getOptions(), [4, 5, 6, 7, 8, 9])
        self.assertFalse(cell.isSet())

    def test_removeOption(self):
        cell = SudokuCell.Cell(0, 0)
        cell.removeOption(1)
        self.assertListEqual(cell.getOptions(), [2, 3, 4, 5, 6, 7, 8, 9])
        self.assertFalse(cell.isSet())

    def test_removeEightOptions(self):
        cell = SudokuCell.Cell(0, 0)
        cell.removeOptions([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertListEqual(cell.getOptions(), [9])
        self.assertTrue(cell.isSet())

    def test_removeOptionsTwice(self):
        cell = SudokuCell.Cell(0, 0)
        cell.removeOptions([1, 2, 3, 4])
        cell.removeOptions([4, 5, 6, 7, 8])
        self.assertListEqual(cell.getOptions(), [9])
        self.assertTrue(cell.isSet())

    def test_returnCellBlockIds(self):
        cell = SudokuCell.Cell(8, 5)
        self.assertListEqual(cell.getBlockIds(), [2, 1])
