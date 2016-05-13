from SudokuCell import Cell
from SetOfCells import SetOfCells


class SudokuBoard:
    def __init__(self, board):
        self.cells = []
        self.rows = []
        self.columns = []
        self.blocks = []
        for rowId in range(9):
            for columnId in range(9):
                if board[rowId][columnId] != 0:
                    self.cells.append(Cell(rowId, columnId, options=[board[rowId][columnId]]))
                else:
                    self.cells.append(Cell(rowId, columnId))

        for rowId in range(9):
            self.rows.append(SetOfCells([cell for cell in self.cells if cell.getRowId() == rowId]))

        for columnId in range(9):
            self.columns.append(SetOfCells([cell for cell in self.cells if cell.getColumnId() == columnId]))

        for blockId in range(9):
            x = blockId % 3
            y = int((blockId - x) / 3)
            self.blocks.append(SetOfCells([cell for cell in self.cells if cell.getBlockRowId() == x and cell.getBlockColumnId() == y]))

    def applyRowRuleForId(self, rowId):
        self.rows[rowId].reduceCells()

    def applyRowRule(self):
        for i in range(9):
            self.applyRowRuleForId(i)

    def applyColumnRuleForId(self, columnId):
        self.columns[columnId].reduceCells()

    def applyBlockRuleForId(self, blockId):
        self.blocks[blockId].reduceCells()

    def applyBlockRule(self):
        for i in range(9):
            self.applyBlockRuleForId(i)

    def applyColumnRule(self):
        for i in range(9):
            self.applyColumnRuleForId(i)

    def getCell(self, rowId, columnId):
        return [cell for cell in self.cells if cell.getRowId() == rowId and cell.getColumnId() == columnId][0]

    def findCellsWithOptions(self):
        return [cell for cell in self.cells if cell.isSet() is False]

    def findFirstUnSetCell(self):
        return self.findCellsWithOptions()[0]

    def returnBoard(self):
        output = []
        for i in range(9):
            output.append([])
            for j in range(9):
                if self.getCell(i, j).isSet():
                    output[i].append(self.getCell(i, j).getOptions()[0])
                else:
                    output[i].append(0)

        return output

    def isSolved(self):
        if self.findCellsWithOptions() == []:
            return True
        else:
            return False
