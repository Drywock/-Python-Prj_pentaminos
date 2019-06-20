class cGrid:

    def __init__(self,hauteur):
        self.cases= []
        
        if(60%hauteur == 0):
            self.hauteur=hauteur
            self.largeur=60/hauteur

            for y in range(self.hauteur):
                self.cases.append([])
                for x in range(self.largeur):
                    self.cases[y].append('X')
    
    def __repr__(self):
        output_str = 'Grid : \n' + "*"*(2+self.largeur) +'\n'

        for y in range(0,self.hauteur):
            output_str += '*'

            for x in range(self.largeur):
                output_str+=self.cases[y][x]

            output_str += '*\n'

        output_str += "*"*(2+self.largeur)
        return output_str

    def show(self):
        print self

grid=cGrid(3)
grid.show()