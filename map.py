from utils import randBool
from utils import randCell
from utils import randCell2


UPGRADE_COST=500
TREE_BONUS=100
LIFE_COST = 300
ICON='✅🌳🌊🚁🔥🔵🏭🏥🌌💀'
class Map:
    
    
    
    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.map=[[0 for i in   range(w)]for j  in  range(h)]
        self.generateRiver(10)
        self.generateRiver(10)
        self.generateForest(3,10)
        self.genUpdateShope()
        self.genHospital()
    
    def checkBounds(self,x,y):
        if (x<0 or y<0 or x>=self.h or y>=self.w):
            return False
        return True
    
    def printMap(self,helico,clouds):
        print(helico.x,helico.y)
        print("🔵" * int(len(self.map[0])+2))
        for ri in range(self.h):
            print("🔵",end="")
            for ci in range(self.w):
                
                cell=self.map[ri][ci]
                if (clouds.cells[ri][ci]==1):
                    print(ICON[8],end='')
                elif (clouds.cells[ri][ci]==2):
                    print(ICON[9],end='')
                elif(helico.x ==ri and helico.y ==ci):
                    print(ICON[3],end='')
                else:
                    print(ICON[cell],end='')
            print("🔵",end='')
            print()
        print("🔵" * int(len(self.map[0])+2))


    def generateForest(self,r,mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randBool(r,mxr):
                    self.map[ri][ci]=1

    def genUpdateShope(self):
        c=randCell(self.w,self.h)
        self.map[c[0]][c[1]]=6

    
    def genHospital(self):
        c=randCell(self.w,self.h)
        if self.map[c[0]][c[1]]!=6:
            self.map[c[0]][c[1]]=7
        else:
            self.genHospital()   


    def generateTree(self):
        c=randCell(self.w,self.h)
        cx,cy= c[0],c[1]
        if(self.checkBounds(cx,cy)and self.map[cx][cy]==0):
            self.map[cx][cy]=1

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

    def addFire(self):
        c=randCell(self.w,self.h)
        cx,cy=c[0],c[1]
        if(self.map[cx][cy]==1):
            self.map[cx][cy]=4

    def updateFires(self):
        for i in range (self.h):
            for j in range(self.w):
                if(self.map[i][j]==4):
                    self.map[i][j]=0
        for i in range(10):
            self.addFire()
        
    def processHelicoptert(self,helicopter,clouds):
        c=self.map[helicopter.x][helicopter.y]
        d=clouds.cells[helicopter.x][helicopter.y]
        if(c== 2):
            helicopter.tank=helicopter.mxTank
        elif(c== 4 and helicopter.tank>0):
            helicopter.tank-=1
            helicopter.score+=TREE_BONUS
            self.map[helicopter.x][helicopter.y]=1
        elif(c==6 and helicopter.score>=500):
            helicopter.mxTank +=1
            helicopter.score-=UPGRADE_COST
        elif(c==7 and helicopter.score>=LIFE_COST):
            helicopter.life +=1
            helicopter.score-=LIFE_COST
        if (d==2):
            helicopter.life-=1
            if (helicopter.life==0):
                    helicopter.gameOver()
                    exit(0)
        
 
    def importData(self,data):
        self.map = data["cells"] or [[0 for i in   range(w)]for j  in  range(h)]

    def exportData(self):
        return {'cells': self.map}

   