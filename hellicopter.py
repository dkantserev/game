from utils import randCell
import os

class Hellicopter:

    def __init__(self,w,h):
        rc = randCell(w,h)
        cx,cy=rc[0],rc[1]
        self.x=cx
        self.y=cy
        self.h=h
        self.w=w
        self.tank=0
        self.mxTank=1
        self.score=0
        self.life =3

    def move(self,dx,dy):
        nx= dx +self.x
        ny=dy + self.y
        if(nx>=0 and ny >=0 and nx < self.h and ny<self.w):
            self.x,self.y= nx,ny

    def printStats(self):
        print('💧',self.tank,"/",self.mxTank,' | ','💥score ', self.score,' | ','🧡 ',self.life, sep="")
                      
    def gameOver(self):
            clear='clear'
            if os.name=='nt':
                clear='cls'
            os.system(clear)
            for i in range(5):
                print("")     
            print("GAME OVER, YOUR SCORE IS ",self.score)
            for i in range(5):
                print("")

    def exportData(self):
        return {"score": self.score,
              "lives":self.life,
              "x":self.x,
              "y":self.y,
              "tank": self.tank,
              "mxTank":self.mxTank}
    
    def importData(self,data):
        self.x= data['x'] or 0
        self.y= data['y'] or 0
        self.tank= data['tank'] or 0
        self.mxTank = data['mxTank'] or 1
        self.life= data['lives'] or 3
        self.score = data['score'] or 0