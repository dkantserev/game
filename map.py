class Map:
    icon='🟩🌳🌊🚁🏘️🔥🌩️🔵'

    def __init__(self,h,w):
        self.map=[[0 for i in   range(w)]for j  in  range(h)]
        
    def printMap(self):
        print("🔵" * int(len(self.map)+2))
        for raw in self.map:
            print("🔵",end="")
            for cell in raw:
                
                print(self.icon[cell],end="")
            print("🔵",end="")
            print()
        print("🔵" * int(len(self.map)+2))
 
k=Map(8,8)
k.map[3][2]=2
k.map[4][3]=3
k.printMap()
   