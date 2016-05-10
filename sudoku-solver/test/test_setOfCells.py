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

    def test_reduceCells(self):
        cells = []
        for i in range(8):
            cells.append(SudokuCell.Cell(0, i, [i+1]))

        cells.append(SudokuCell.Cell(0, 8))

        expectedCells = set([x + 1 for x in range(9)])

        setOfCells = SetOfCells.SetOfCells(cells)
        setOfCells.reduceCells()

        self.assertSetEqual({cell.getOptions()[0] for cell in setOfCells.returnCells()}, expectedCells)
