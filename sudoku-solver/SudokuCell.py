class Cell:
    def __init__(self, rowId, columnId, options=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.options = options
        self.rowId = rowId
        self.columnId = columnId

    def isSet(self):
        if len(self.options) == 1:
            return True

        return False

    def set(self, num):
        self.options = [num]

    def getOptions(self):
        return self.options

    def removeOption(self, option):
        self.options = [x for x in self.options if x != option]

    def removeOptions(self, options):
        self.options = [x for x in self.options if (x in options) is False]

    def getRowId(self):
        return self.rowId

    def getColumnId(self):
        return self.columnId

    def getBlockRowId(self):
        return int((self.rowId - (self.rowId % 3)) / 3)

    def getBlockColumnId(self):
        return int((self.columnId - (self.columnId % 3)) / 3)

    def getBlockIds(self):
        return [self.getBlockRowId(), self.getBlockColumnId()]
