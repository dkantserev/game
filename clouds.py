from utils import randBool

class Clouds:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.cells=[[0 for i in range(w)]for i in range(h)]

    def updateClouds(self,r=1,mxr=20,g=1,mxg=10):
        for i in range(self.h):
            for j in range(self.w):
                if randBool(r,mxr):
                    self.cells[i][j]=1
                    if randBool(g,mxg):
                        self.cells[i][j]=2
                else:
                    self.cells[i][j]=0

    def exportData(self):
        return {"cells": self.cells}
    
    def importData(self,data):
        self.cells = data['cells'] or [[0 for i in   range(w)]for j  in  range(h)]
