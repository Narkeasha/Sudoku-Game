import pygame
import os 
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (400, 100) #400 to right, 100 down setting window position as appears
#need to create the window of the game  
surface = pygame.display.set_mode((1200, 900)) #extra 300 width for the side FIX-size of the grid to fit
pygame.display.set_caption("Narkeasha's Personal Sudoku")


#instentiate grid object 
grid = Grid() #creating acutal object
running = True #create game loop

while running:
    #chcek for event on pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if x is pressed upper right corner to stop
            running = False

    
    surface.fill ((124, 163, 124)) #fill surface to black


    #drawing grid here
    grid.draw_lines(pygame, surface)



    #updating window surface
    pygame.display.flip() 





 