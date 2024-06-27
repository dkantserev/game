from map import Map
import time
import os
from hellicopter import Hellicopter as Helico
from pynput import keyboard

tick =1
TICK_SLEEP=0.1
TYPE_SYSTEM=os.name
TREE_UPDATE=50
FIRE_UPDATE=100
MAP_H,MAP_W=10,20


k=Map(MAP_H,MAP_W)



hel=Helico(MAP_W,MAP_H)

MOVES ={'a': (0,-1),'ф':(0,-1),'d':(0,1),'в':(0,1),'w':(-1,0),'ц':(-1,0),'s':(1,0),'ы':(1,0)}

def on_release(key):
    global hel
    c= key.char.lower()
    if c in MOVES.keys():
        cx=MOVES[c][0]
        cy=MOVES[c][1]
        hel.move(cx,cy)
    # if key.char =='ф':
    #     print('yes')
    # print('{0} released'.format(
    #     key))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return Falsedddddddwwwwwwwwwwdddddddddsaaaaaaaaaaaadaawwwwddddddsdsssssswwwwwwwwddssssssssdddwaaaasssswwadddddssdaaaddddddwaaaasdaaaaaaadwwwwwwwwdddddddaaaaaaaaaaassssssssssaaaaawwwaasssdddddddddddddddwwwaaaaaassssaaawwwwwwdssssssaaaaawwwwddsddsssdddddddwwwwwssssssaaaaaaaaaadddssdwdddddsaaaasssdwddaaaaaaawwwwaaaaaaaawwwwwddddddddsssssssssdddddddaaaaaawwwwwawwwddsdddddaaaaaaasasaaaaaaaaddddaaaadddddddsddsssssdddddddwaaaaaaaaaaaaaawwwdsssddsswwasdddddddddddddddddddddwdddddddddddddwwwwaaaaaaaaaaaaaaaaaasddddsdddddddwddwaddsssssssssaaaaaawdsdddaaaaaaaaawssd


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
    k.processHelicoptert(hel)
    hel.printStats()
    k.printMap(hel)

    tick+=1
    time.sleep(TICK_SLEEP)
    
    if (tick%TREE_UPDATE==0):
        k.generateTree()
    if (tick%FIRE_UPDATE==0):
        k.updateFires()
        