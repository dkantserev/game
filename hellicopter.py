from utils import randCell
class Hellicopter:
    def __init__(self,w,h):
        rc = randCell(w,h)
        cx,cy=rc[0],rc[1]
        self.x=cx
        self.y=cy