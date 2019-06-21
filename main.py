from pentamino import cPentamino
from grid import cGrid


def initGrille():
    lColumnNames = ['A','B','C','D','E','F','G','H','I','J','K','L']
    nbRows = 60/len(lColumnNames)

    grid = cGrid()

    for columnName in lColumnNames:
        grid.addColumn(columnName)

    for row in range(nbRows):
        grid.addRow()
    
    return grid