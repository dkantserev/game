from map import Map
import time
import os
from hellicopter import Hellicopter as Helico
from pynput import keyboard

tick =1
TICK_SLEEP=0.05
TYPE_SYSTEM=os.name
TREE_UPDATE=50
FIRE_UPDATE=100
MAP_H,MAP_W=10,20

k=Map(MAP_H,MAP_W)
k.generateRiver(10)
k.generateRiver(10)
k.generateForest(3,10)


hel=Helico(MAP_H,MAP_W)


while True:
    clear=''
    if TYPE_SYSTEM=='nt':
        clear='cls'
    else:
        clear='clear'
    os.system(clear)
    print(tick)
    k.printMap(hel)
    tick+=1
    time.sleep(TICK_SLEEP)
    
    if (tick%TREE_UPDATE==0):
        k.generateTree()
    if (tick%FIRE_UPDATE==0):
        k.updateFires()
        