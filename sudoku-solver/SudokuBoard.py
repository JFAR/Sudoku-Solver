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

    def applyColumnRule(self):
        for i in range(9):
            self.applyColumnRuleForId(i)

    def getCell(self, rowId, columnId):
        return [cell for cell in self.cells if cell.getRowId() == rowId and cell.getColumnId() == columnId][0]

    def getRowById(self, rowId):
        return [cell for cell in self.cells if cell.getRowId() == rowId]

    def getColumnById(self, columnId):
        return [cell for cell in self.cells if cell.getColumnId() == columnId]

    def getBlockByIds(self, blockRowId, blockColumnId):
        return [cell for cell in self.cells if cell.getBlockRowId() == blockRowId and cell.getBlockColumnId() == blockColumnId]

    def getBlockById(self, blockId):
        x = blockId % 3
        y = int((blockId - x) / 3)
        return self.getBlockByIds(x, y)

    def reduceCellOptions(self, rowId, columnId):
        cellOfInterest = self.getCell(rowId, columnId)
        if cellOfInterest.isSet() is False:
            print(str(cellOfInterest.getRowId()) + " " + str(cellOfInterest.getColumnId()))
            print(cellOfInterest.getOptions())
            rowOfCellNumbers = [cell.getOptions()[0] for cell in self.getRowById(rowId) if cell.isSet()]
            for x in rowOfCellNumbers:
                cellOfInterest.removeOption(x)

            print(cellOfInterest.getOptions())

            columnOfCellNumbers = [cell.getOptions()[0] for cell in self.getColumnById(columnId) if cell.isSet()]
            for x in columnOfCellNumbers:
                cellOfInterest.removeOption(x)

            print(cellOfInterest.getOptions())

            blockOfCellNumbers = [cell.getOptions()[0] for cell in self.getBlockByIds(cellOfInterest.getBlockRowId(), cellOfInterest.getBlockColumnId()) if cell.isSet()]
            for x in blockOfCellNumbers:
                cellOfInterest.removeOption(x)

            print(cellOfInterest.getOptions())

    def findCellsWithOptions(self):
        return [cell for cell in self.cells if cell.isSet() is False]

    def returnRowById(self, rowId):
        return [cell.getOptions()[0] for cell in self.cells if cell.getRowId() == rowId and cell.isSet()]

    def returnColumnById(self, columnId):
        return [cell.getOptions()[0] for cell in self.cells if cell.getColumnId() == columnId and cell.isSet()]

    def returnBlockById(self, blockId):
        x = blockId % 3
        y = int((blockId - x) / 3)
        return [cell.getOptions()[0] for cell in self.cells if cell.getBlockIds() == [x, y] and cell.isSet()]

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
