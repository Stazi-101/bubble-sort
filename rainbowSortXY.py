
import pygame
import numpy as np
import random

SCALE = 8
PIXX = 400
PIXY = 400
ARRX = PIXX//SCALE
ARRY = PIXY//SCALE

speed = 5

def draw(arr,screen):

    for i in range(ARRX):
        for j in range(ARRX):
            col = arr[ i,j ]
            #screen.set_at( (i,j) , (r,r,r) )
            pygame.draw.rect(screen, col, (i*SCALE,j*SCALE,SCALE,SCALE) )

    pygame.display.update()

def sort(pos,arr):

    def sortAlgX(col1,col2):
        return col1[0]>col2[0]

    def sortAlgY(col1,col2):
        return sum(col1)>sum(col2)

    def nextPos(pos):
        return random.randint(0,ARRX-1),random.randint(0,ARRY-1)
        

        
    if random.randint(0,1):
        if sortAlgX( arr[ pos[0],pos[1] ],arr[ pos[0],pos[1]+1 ] ):
            arr[ pos[0],pos[1]:pos[1]+2 ] = arr[ pos[0],pos[1]:pos[1]+2 ][::-1]
    else:
        if sortAlgY( arr[ pos[0],pos[1] ],arr[ pos[0]+1,pos[1] ] ):
            arr[ pos[0]:pos[0]+2,pos[1] ] = arr[ pos[0]:pos[0]+2,pos[1] ][::-1]

    pos = nextPos(pos)

    return pos  



def main():

    speed = 5
    
    arr = np.random.randint( 0,255, (ARRX+1,ARRY+1,3) )
    arr[:,:,1]=0

    pos = (0,0)

    pygame.init()
    screen = pygame.display.set_mode( (PIXX,PIXY) )


    clock = pygame.time.Clock()
    running = True
    while running:
        
        sinceLast = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    print(speed)
                elif event.key==pygame.K_f:
                    print(1000/sinceLast)
                
            if pygame.mouse.get_pressed()[0]:
                speed+=10
            elif pygame.mouse.get_pressed()[2]:
                speed-=10
                

        for i in range(speed):
            pos = sort(pos,arr)
                
        draw(arr,screen)


if __name__ == '__main__':
    main()

