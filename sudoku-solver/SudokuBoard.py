from SudokuCell import Cell


class SudokuBoard:
    def __init__(self, board):
        self.cells = []
        for rowId in range(9):
            for columnId in range(9):
                if board[rowId][columnId] != 0:
                    self.cells.append(Cell(rowId, columnId, options=[board[rowId][columnId]]))
                else:
                    self.cells.append(Cell(rowId, columnId))

    def applyRowRuleForId(self, rowId):
        rowOfInterest = [cell for cell in self.cells if cell.getRowId() == rowId]
        setEntries = [cell.getOptions()[0] for cell in rowOfInterest if cell.isSet()]

        for cell in rowOfInterest:
            if cell.isSet() is False:
                cell.removeOptions(setEntries)

    def getCell(self, rowId, columnId):
        return [cell for cell in self.cells if cell.getRowId() == rowId and cell.getColumnId() == columnId][0]

    def getRowById(self, rowId):
        return [cell for cell in self.cells if cell.getRowId() == rowId]

    def getColumnById(self, columnId):
        return [cell for cell in self.cells if cell.getColumnId() == columnId]

    def getBlockByIds(self, blockRowId, blockColumnId):
        return [cell for cell in self.cells if cell.getBlockRowId() == blockRowId and cell.getBlockColumnId() == blockColumnId]

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

    def returnBlockByIds(self, blockRowId, blockColumnId):
        return [cell.getOptions()[0] for cell in self.cells if cell.getBlockIds() == [blockRowId, blockColumnId] and cell.isSet()]

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