"""chattering cell type, subclass from izhCell"""
import izhikevich_cells as izh

class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        #define parameters that need modification 
        self.celltype = 'chattering'
        self.C = 50
        self.vr = -60
        self.vt= -40
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 50

myCell = ibCell(4000)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)