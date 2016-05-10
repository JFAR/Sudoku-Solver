class SetOfCells:
    def __init__(self, cells):
        self.cells = set(cells)

    def returnCells(self):
        return self.cells

    def reduceCells(self):
        determinedValues = {cell.getOptions()[0] for cell in self.cells if cell.isSet()}

        for cell in self.cells:
            if cell.isSet() is False:
                cell.removeOptions(determinedValues)

                if cell.isSet():
                    self.reduceCells()
                    break
