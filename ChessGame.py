import pygame
from pygame.locals import *
from HelperFunctions import makeGrid, drawGrid, mainscreen, checkmate, endscreen, render_environment, initialize, draw_pieces, user_move, cpu_move

def main():
    main_screen = True
    while True:
        if main_screen: 
            main_screen, user_turn = mainscreen(main_screen)
            piece_at_grid= initialize([[None]*8 for i in range(8)])
    
        else:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
            user_checkmate, cpu_checkmate = checkmate(piece_at_grid)
            render_environment(piece_at_grid, user_checkmate, cpu_checkmate) 
            winner = None
            if user_turn:
                piece_at_grid, winner = user_move(piece_at_grid)
                user_turn = False
                if winner != None:
                    return endscreen(winner)
                    break
            else:
                piece_at_grid, winner = cpu_move(piece_at_grid)
                user_turn = True
                if winner != None: 
                    return endscreen(winner)
                    break            
         
        pygame.display.update()
        FramePerSec.tick(FPS)

pygame.init()
screen = pygame.display.set_mode((1366, 768))
FPS = 30
FramePerSec = pygame.time.Clock()
background = pygame.image.load("chessboard.jpg")
background = pygame.transform.scale(background, (1366, 768))
grid = makeGrid()

again = main()
while again == True:
    again = main()
pygame.quit()