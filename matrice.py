from column import cColumn
from case import cCase

class cMatrice():
    def __init__(self):
        self.left=self
        self.right=self

        lnames=['F','I','L','P','N','T','U','V','W','X','Y','Z']
        
        for name in lnames:
            self.addColumn(name)

        for i in range(60):
            self.addColumn('{}'.format(i))

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

    def addRow(self,masque):
        x=self
        last=self

        isFirst=True
        first=self

        for i in range(self.countColumn()):
            x=x.right
            if(masque[i]==1):
                newCase=cCase
                newCase.up = x.up
                newCase.down = x
                x.up=newCase

                if(last != self):
                    newCase.left=last
                    last.right=newCase
                
                last=newCase
                if(isFirst):
                    first=newCase
                    isFirst=False
        
        #close the circle
        last.right=first
        first.left=last

            