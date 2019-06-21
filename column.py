from case import cCase

class cColumn():

    def __init__(self,name):
        self.name=name
        self.left=self
        self.right=self
        self.up=self
        self.down=self
        self.c=self
        self.L=self

    def size(self):
        cpt = 0
        x = self
        while(x.down!=self):
            cpt+=1
            x=self.down

        return cpt


        