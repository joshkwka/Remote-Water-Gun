import pygame
from time import sleep

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))
    
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    
    myKey = getattr(pygame,'K_{}'.format(keyName))
    
    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    
    return ans

def main():
    if getKey('a') or getKey('LEFT'):
        print('left')
    elif getKey('w') or getKey('UP'):
        print('up')
    elif getKey('s') or getKey('DOWN'):
        print('down')
    elif getKey('d') or getKey('RIGHT'):
        print('right')
    elif getKey('SPACE'):
        print('shoot')
        
if __name__ == '__main__':
    init()
    while True:
        main()
        sleep(0.2)
        if getKey('q'):
            break
