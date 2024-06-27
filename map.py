from utils import randBool
from utils import randCell
from utils import randCell2

class Map:
    icon='🟩🌳🌊🚁🔥🌩️🔵'

    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.map=[[0 for i in   range(w)]for j  in  range(h)]
    
    def checkBounds(self,x,y):
        if (x<0 or y<0 or x>=self.h or y>=self.w):
            return False
        return True
    
    def printMap(self,helico):
        print("🔵" * int(len(self.map[0])+2))
        for ri in range(self.h):
            print("🔵",end="")
            for ci in range(self.w):
                cell=self.map[ri][ci]
                if(helico.x ==ri and helico.y ==ci):
                    print(self.icon[3],end='')
                else:
                    print(self.icon[cell],end="")
            print("🔵",end="")
            print()
        print("🔵" * int(len(self.map[0])+2))

    def generateForest(self,r,mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randBool(r,mxr):
                    self.map[ri][ci]=1
    def addFire(self):
        c=randCell(self.w,self.h)
        cx,cy=c[0],c[1]
        if(self.map[cx][cy]==1):
            self.map[cx][cy]=4

    def generateTree(self):
        c=randCell(self.w,self.h)
        cx,cy= c[0],c[1]
        if(self.checkBounds(cx,cy)and self.map[cx][cy]==0):
            self.map[cx][cy]=1

    def updateFires(self):
        for i in range (self.h):
            for j in range(self.w):
                if(self.map[i][j]==4):
                    self.map[i][j]=0
        for i in range(5):
            self.addFire()
        
    def generateRiver(self,l):
        rc=randCell(self.w,self.h)

        
        rx=rc[0]
        ry=rc[1]
        self.map[rx][ry]=2  
        while l>0:
            rc2=randCell2(rx,ry)
            rx2,ry2=rc2[0],rc2[1]
            if (self.checkBounds(rx2,ry2)):
                self.map[rx2][ry2]=2
                rx,ry=rx2,ry2
                l-=1

        
 



   