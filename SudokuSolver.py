class Cell:
    def __init__(self, rowId, columnId, options=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.options = options
        self.rowId = rowId
        self.columnId = columnId

    def isSet(self):
        if len(self.options) == 1:
            return True

        return False

    def getOptions(self):
        return self.options

    def removeOption(self, option):
        self.options = [x for x in self.options if x != option]

    def getRowId(self):
        return self.rowId

    def getColumnId(self):
        return self.columnId

    def getBlockRowId(self):
        return int((self.rowId - (self.rowId % 3)) / 3)

    def getBlockColumnId(self):
        return int((self.columnId - (self.columnId % 3)) / 3)


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
                for entry in setEntries:
                    cell.removeOption(entry)

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


def checkContainsNumbers(listOfNumbers):
    for i in range(9):
        if (i + 1) not in listOfNumbers:
            return False

    return True


def checkBoard(board):
    sudokuBoard = SudokuBoard(board)
    for i in range(9):
        row = sudokuBoard.getRowById(i)
        rowNumbers = [cell.getOptions()[0] for cell in row if cell.isSet()]
        if checkContainsNumbers(rowNumbers) is False:
            return False

        column = sudokuBoard.getColumnById(i)
        columnNumbers = [cell.getOptions()[0] for cell in column if cell.isSet()]
        if checkContainsNumbers(columnNumbers) is False:
            return False

        x = i % 3
        y = int((i - x) / 3)

        block = sudokuBoard.getBlockByIds(x, y)
        blockNumbers = [cell.getOptions()[0] for cell in block if cell.isSet()]
        if checkContainsNumbers(blockNumbers) is False:
            return False

    return True


def solver(inputBoard):
    oldBoard = []
    while checkBoard(inputBoard) is False and oldBoard != inputBoard:
        oldBoard = inputBoard
        sudokuBoard = SudokuBoard(inputBoard)
        for cellWithOptions in sudokuBoard.findCellsWithOptions():
            sudokuBoard.reduceCellOptions(cellWithOptions.getRowId(), cellWithOptions.getColumnId())

        inputBoard = sudokuBoard.returnBoard()

    return inputBoard
