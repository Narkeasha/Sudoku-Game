import pygame

#need to create the window of the game  
surface = pygame.display.set_mode((1200, 900)) #extra 300 width for the side FIX-size of the grid to fit
pygame.display.set_caption("Narkeasha's Personal Sudoku")

running = True #create game loop
while running:
    #chcek for event on pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if x is pressed upper right corner to stop
            running = False



