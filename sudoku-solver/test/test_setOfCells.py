import unittest
import SetOfCells
import SudokuCell


class SetOfCellsTest(unittest.TestCase):
    def test_containsCells(self):
        cells = []
        for i in range(9):
            cells.append(SudokuCell.Cell(0, i))

        setOfCells = SetOfCells.SetOfCells(cells)

        self.assertSetEqual(setOfCells.returnCells(), set(cells))
