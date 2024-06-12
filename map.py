from utils import randBool
from utils import randCell

class Map:
    icon='🟩🌳🌊🚁🏘️🔥🌩️🔵'

    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.map=[[0 for i in   range(w)]for j  in  range(h)]
    
    def generateForest(self,r,mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randBool(r,mxr):
                    self.map[ri][ci]=1
    def generateRiver(self,l):
        rc=randCell(self.w,self.h)
        rx=rc[0]
        ry=rc[1]
        self.map[rx][ry]=2    
    def printMap(self):
        print("🔵" * int(len(self.map)+2))
        for raw in self.map:
            print("🔵",end="")
            for cell in raw:
                
                print(self.icon[cell],end="")
            print("🔵",end="")
            print()
        print("🔵" * int(len(self.map)+2))
        
    def checkBounds(self,x,y):
        if (x<0 or y<0 or x>=self.w or y>=self.h):
            return False
        return True
 
k=Map(10,10)

k.generateRiver(10)
k.printMap()
   