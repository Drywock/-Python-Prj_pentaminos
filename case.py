class cCase():
    
    def __init__(self):
        self.left=self
        self.right=self
        self.up=self
        self.down=self
        self.column=self

    def restore(self):
        self.left.right=self
        self.right.left=self
        self.up.down=self
        self.down.up=self