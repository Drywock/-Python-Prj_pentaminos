from column import cColumn
from case import cCase

class cGrid():
    def __init__(self):
        self.left=self
        self.right=self
    
    def __repr__(self):
        output_str = 'Grid : \n'
        return output_str

    def countColumn(self):
        cpt=0
        x=self
        while(x.right!=self):
            x=x.right
            cpt+=1

        return cpt

    def addColumn(self,name):
        x=self.left
        newColumn = cColumn(name)
        newColumn.left=x.left
        newColumn.right=x
        x.left=newColumn

    def addRow(self):
        x=self
        while(x.right != self):
            x=x.right
            newCase = cCase()
            newCase.up = x.up
            newCase.down = x
            x.up=newCase

            if(x.left!=self):
                newCase.left=x.left.up
                x.left.up.right=newCase
            
            newCase.column=x

    def show(self):
        print self