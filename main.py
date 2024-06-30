from map import Map
import time
import os
from hellicopter import Hellicopter as Helico
from pynput import keyboard
from clouds import Clouds
import json
TICK_SLEEP=0.08
TYPE_SYSTEM=os.name
TREE_UPDATE=50
FIRE_UPDATE=100
MAP_H,MAP_W=10,20
CLOUDS_UPDATE=100
tick =1


map=Map(MAP_H,MAP_W)


clouds=Clouds(MAP_W,MAP_H)
hel=Helico(MAP_W,MAP_H)

MOVES ={'a': (0,-1),'ф':(0,-1),'d':(0,1),'в':(0,1),'w':(-1,0),'ц':(-1,0),'s':(1,0),'ы':(1,0)}


def on_release(key):
    global hel, tick , clouds, map, hel
    c= key.char.lower()
    if c in MOVES.keys():
        cx=MOVES[c][0]
        cy=MOVES[c][1]
        hel.move(cx,cy)
    elif (c == 'f' or c=='а'):
        data= {"helicopter":hel.exportData(),
               "clouds": clouds.exportData(),
               "field": map.exportData(),
               "tick": tick}
        with open("level.json",'w') as lvl:
            json.dump(data,lvl)
            lvl.close

    elif (c == 'g' or c=='п'):

        with open("level.json","r") as lvl:
            data=json.load(lvl)
            print(data["helicopter"]["lives"])
            hel.importData(data["helicopter"])
            tick= data["tick"] or 1
            map.importData(data["field"])
            clouds.importData(data["clouds"])


listener = keyboard.Listener(
    
    on_release=on_release)
listener.start()

          
while True:
    clear=''
    if TYPE_SYSTEM=='nt':
        clear='cls'
    else:
        clear='clear'
    os.system(clear)
    print(tick)
    map.processHelicoptert(hel,clouds)
    hel.printStats()
    map.printMap(hel,clouds)

    tick+=1
    time.sleep(TICK_SLEEP)
    
    if (tick%TREE_UPDATE==0):
        map.generateTree()
    if (tick%FIRE_UPDATE==0):
        map.updateFires()
    if (tick%CLOUDS_UPDATE==0):
        clouds.updateClouds()
        