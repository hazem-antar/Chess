import pygame
from pygame.locals import *
import math
from ChessPeices import *

screen = pygame.display.set_mode((1366, 768))
FPS = 30
FramePerSec = pygame.time.Clock()
background = pygame.image.load("chessboard.jpg")
background = pygame.transform.scale(background, (1366, 768))
BlockSize = 72
select_border = pygame.image.load('select.png')
select_border = pygame.transform.scale(select_border, (BlockSize, BlockSize))   
move_allowed = pygame.image.load('move.png')
move_allowed = pygame.transform.scale(move_allowed, (BlockSize, BlockSize)) 
attack_allowed = pygame.image.load('attack.png')
attack_allowed = pygame.transform.scale(attack_allowed, (BlockSize, BlockSize)) 
checkmate_boarder = pygame.image.load('checkmate.png')
checkmate_boarder = pygame.transform.scale(checkmate_boarder, (BlockSize, BlockSize)) 

def makeGrid():
    count = 8
    grid = []
    for y in range(0, BlockSize*count, BlockSize):
        grid_raw = []
        for x in range(0,  BlockSize*count, BlockSize):
            block_x = x+398
            block_y = y+98
            grid_raw.append((block_x, block_y))
        grid.append(grid_raw) 
    return grid

grid = makeGrid()

def drawGrid(grid):     
    for raw in grid:
        grid_raw = []
        for block in raw:    
            rect = pygame.Rect(block[0], block[1], BlockSize, BlockSize)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)    


def mainscreen(main_screen):
    global user_color
    user_turn = None
    user_color = None
    B1_pressed, B2_pressed, B3_pressed, B4_pressed = False, False, False, False
    color_light = (170,170,170)
    color_dark = (100,100,100)
    user_text = pygame.font.SysFont('Calibri',35).render('User' , True , (255,255,255))
    computer_text = pygame.font.SysFont('Calibri',35).render('Computer' , True , (255,255,255))
    black_text = pygame.font.SysFont('Calibri',35).render('Black' , True , (255,255,255))
    white_text = pygame.font.SysFont('Calibri',35).render('White' , True , (255,255,255))
    Choose_start = pygame.font.SysFont('Calibri',35).render('Choose who to start..' , True , (0, 0, 0))
    Choose_color = pygame.font.SysFont('Calibri',35).render('Choose your color..' , True , (0, 0, 0))
    while main_screen:
        screen.fill((255,255,255))
        mouse = pygame.mouse.get_pos()        
        if B1_pressed or 370 <= mouse[0] <= 590 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, color_light, [370,220,220,50])  
        else:
            pygame.draw.rect(screen, color_dark, [370,220,220,50])
        if B2_pressed or 760 <= mouse[0] <= 980 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, color_light, [760,220,220,50])
        else:
            pygame.draw.rect(screen, color_dark, [760,220,220,50])
        if B3_pressed or 370 <= mouse[0] <= 590 and 520 <= mouse[1] <= 570:
            pygame.draw.rect(screen, color_light, [370,520,220,50])
        else:
            pygame.draw.rect(screen, color_dark, [370,520,220,50])
        if B4_pressed or 760 <= mouse[0] <= 980 and 520 <= mouse[1] <= 570:
            pygame.draw.rect(screen, color_light, [760,520,220,50]) 
        else:
            pygame.draw.rect(screen, color_dark, [760,520,220,50])     
            
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and 370 <= mouse[0] <= 590 and 220 <= mouse[1] <= 270:
                pygame.draw.rect(screen, color_light, [370,220,220,50])
                if B2_pressed: B2_pressed = False
                B1_pressed = True
                user_turn = True
            elif ev.type == pygame.MOUSEBUTTONDOWN and 760 <= mouse[0] <= 980 and 200 <= mouse[1] <= 270:
                if B1_pressed: B1_pressed = False
                B2_pressed = True
                pygame.draw.rect(screen, color_light, [760,220,220,50])  
                user_turn = False
            elif ev.type == pygame.MOUSEBUTTONDOWN and 370 <= mouse[0] <= 590 and 520 <= mouse[1] <= 570:
                if B4_pressed: B4_pressed = False
                B3_pressed = True
                pygame.draw.rect(screen, color_light, [370,520,220,50])
                user_color = "black"  
            elif ev.type == pygame.MOUSEBUTTONDOWN and 760 <= mouse[0] <= 980 and 520 <= mouse[1] <= 570:
                if B3_pressed: B3_pressed = False
                B4_pressed = True
                pygame.draw.rect(screen, color_light, [760,520,220,50])
                user_color = "white"                
        
        screen.blit(Choose_start, (535,150))
        screen.blit(user_text, (450,227))
        screen.blit(computer_text, (800,227))
        screen.blit(Choose_color, (545,450))
        screen.blit(black_text, (445,529))
        screen.blit(white_text, (830,529))
        
        if user_turn != None and user_color != None:
            main_screen = False
            
        pygame.display.update()
        FramePerSec.tick(FPS)
        
    return main_screen, user_turn    

def endscreen(winner):
    Playagain = None
    color_light = (170,170,170)
    color_dark = (100,100,100)
    yes_text = pygame.font.SysFont('Calibri',35).render('Yes' , True , (255,255,255))
    no_text = pygame.font.SysFont('Calibri',35).render('No' , True , (255,255,255))
    if winner == "user":
        winner_text = pygame.font.SysFont('Calibri',38).render("You won! Want to play again?" , True , (0, 0, 0))
    else:
        winner_text = pygame.font.SysFont('Calibri',38).render("Game lost.. Want to play again?" , True , (0, 0, 0))
    
    while True:
        screen.fill((255,255,255))
        mouse = pygame.mouse.get_pos()        
        if 370 <= mouse[0] <= 590 and 400 <= mouse[1] <= 450:
            pygame.draw.rect(screen, color_light, [370,400,220,50])  
        else:
            pygame.draw.rect(screen, color_dark, [370,400,220,50])
        if 760 <= mouse[0] <= 980 and 400 <= mouse[1] <= 450:
            pygame.draw.rect(screen, color_light, [760,400,220,50])
        else:
            pygame.draw.rect(screen, color_dark, [760,400,220,50])
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and 370 <= mouse[0] <= 590 and 400 <= mouse[1] <= 450:
                pygame.draw.rect(screen, color_light, [370,220,220,50])
                Playagain = True
            elif ev.type == pygame.MOUSEBUTTONDOWN and 760 <= mouse[0] <= 980 and 400 <= mouse[1] <= 450:
                pygame.draw.rect(screen, color_light, [760,220,220,50])  
                Playagain = False
            
        
        screen.blit(yes_text, (460,409))
        screen.blit(no_text, (855,409))
        screen.blit(winner_text, (445,260))
        
        if Playagain != None:
            break
            
        pygame.display.update()
        FramePerSec.tick(FPS)
       
    return Playagain

def render_environment(piece_at_grid, user_checkmate = None, cpu_checkmate = None): 
    screen.blit(background, (0,0))
    drawGrid(grid)
    if user_checkmate != None:
        screen.blit(checkmate_boarder, (user_checkmate.rect.x,user_checkmate.rect.y))
    if cpu_checkmate != None:
        screen.blit(checkmate_boarder, (cpu_checkmate.rect.x,cpu_checkmate.rect.y))
    draw_pieces(piece_at_grid)
    pygame.display.update()

def get_possible_moves(player, piece, piece_at_grid, raw, col, blit_path = False):
    if player == "user":
        s = 1
    else:
        s = -1
    allowed_movments = []
    attack_range = []
    if type(piece) == Pawn:
        if raw-(1*s) in range(8) and col <= 6 and piece_at_grid[raw-(1*s)][col+1] != None and piece.team != piece_at_grid[raw-(1*s)][col+1].team:
            allowed_movments.append((raw-(1*s),col+1))
            attack_range.append((raw-(1*s),col+1))
            if blit_path: screen.blit(attack_allowed, (grid[raw-(1*s)][col+1][0], grid[raw-(1*s)][col+1][1]))
        if raw-(1*s) in range(8) and col >= 1 and piece_at_grid[raw-(1*s)][col-1] != None and piece.team != piece_at_grid[raw-(1*s)][col-1].team:
            allowed_movments.append((raw-(1*s),col-1))    
            attack_range.append((raw-(1*s),col-1))
            if blit_path: screen.blit(attack_allowed, (grid[raw-(1*s)][col-1][0], grid[raw-(1*s)][col-1][1]))        
        if piece.first_move and piece_at_grid[raw-(1*s)][col] == None and piece_at_grid[raw-(2*s)][col] == None and ((piece.raw == 6 and piece.team =="user")or(piece.raw == 1 and piece.team =="cpu")):
            allowed_movments.append((raw-(2*s),col))
            if blit_path: screen.blit(move_allowed, (grid[raw-(2*s)][col][0], grid[raw-(2*s)][col][1]))
        if raw-(1*s) in range(8) and piece_at_grid[raw-(1*s)][col] == None:
            allowed_movments.append((raw-(1*s),col))
            if blit_path: screen.blit(move_allowed, (grid[raw-(1*s)][col][0], grid[raw-(1*s)][col][1]))
        
    elif type(piece) == Knight:
        places = [(-(2*s),1), (-(1*s),2), (-(2*s),-1), (-(1*s),-2), ((2*s),1), ((1*s),2), ((2*s),-1), ((1*s),-2)]
        for (x, y) in places:
            if raw+(x*s) in range(8) and col+y in range(8):
                if piece_at_grid[raw+(x*s)][col+y] == None:
                    allowed_movments.append((raw+(x*s),col+y))
                    if blit_path: screen.blit(move_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                elif piece.team != piece_at_grid[raw+(x*s)][col+y].team:
                    allowed_movments.append((raw+(x*s),col+y))
                    attack_range.append((raw+(x*s),col+y))
                    if blit_path: screen.blit(attack_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
    elif type(piece) == Rook:
        places = []
        places.append([(0,x) for x in range(1,8)])
        places.append([(0,-x) for x in range(1,8)])
        places.append([(x,0) for x in range(1,8)])
        places.append([(-x,0) for x in range(1,8)])
        for direction in places:
            for (x, y) in direction:
                if raw+(x*s) in range(8) and col+y in range(8):
                    if piece_at_grid[raw+(x*s)][col+y] == None:
                        allowed_movments.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(move_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                    elif piece.team != piece_at_grid[raw+(x*s)][col+y].team:
                        allowed_movments.append((raw+(x*s),col+y))
                        attack_range.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(attack_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                        break
                    else:
                        break
    elif type(piece) == Bishop:
        places = []
        places.append([(x,x) for x in range(1,8)])
        places.append([(-x,-x) for x in range(1,8)])
        places.append([(x,-x) for x in range(1,8)])
        places.append([(-x,x) for x in range(1,8)])                                
        for direction in places:
            for (x, y) in direction:
                if raw+(x*s) in range(8) and col+y in range(8):
                    if piece_at_grid[raw+(x*s)][col+y] == None:
                        allowed_movments.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(move_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                    elif piece.team != piece_at_grid[raw+(x*s)][col+y].team:
                        allowed_movments.append((raw+(x*s),col+y))
                        attack_range.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(attack_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                        break
                    else:
                        break                                                
    elif type(piece) == Queen:
        places = []
        places.append([(x,x) for x in range(1,8)])
        places.append([(-x,-x) for x in range(1,8)])
        places.append([(x,-x) for x in range(1,8)])
        places.append([(-x,x) for x in range(1,8)]) 
        places.append([(0,x) for x in range(1,8)])
        places.append([(0,-x) for x in range(1,8)])
        places.append([(x,0) for x in range(1,8)])
        places.append([(-x,0) for x in range(1,8)])  
        for direction in places:
            for (x, y) in direction:
                if raw+(x*s) in range(8) and col+y in range(8):
                    if piece_at_grid[raw+(x*s)][col+y] == None:
                        allowed_movments.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(move_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                    elif piece.team != piece_at_grid[raw+(x*s)][col+y].team:
                        allowed_movments.append((raw+(x*s),col+y))
                        attack_range.append((raw+(x*s),col+y))
                        if blit_path: screen.blit(attack_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                        break
                    else:
                        break                                                  
    elif type(piece) == King:
        places = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
        for (x, y) in places:
            if raw+(x*s) in range(8) and col+y in range(8):
                if piece_at_grid[raw+(x*s)][col+y] == None:
                    allowed_movments.append((raw+(x*s),col+y))
                    if blit_path: screen.blit(move_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))
                elif piece.team != piece_at_grid[raw+(x*s)][col+y].team:
                    allowed_movments.append((raw+(x*s),col+y))
                    attack_range.append((raw+(x*s),col+y))
                    if blit_path: screen.blit(attack_allowed, (grid[raw+(x*s)][col+y][0],grid[raw+(x*s)][col+y][1]))   
    pygame.display.update() 
    return allowed_movments, attack_range

def attempt_move(piece, piece_at_grid, to_raw, to_col):
    global user_color, cpu_color
    winner = None
    existed = piece_at_grid[to_raw][to_col]
    position = piece.get_location()
    undo_process = [None, None, None, None, None, None]
    undo_process[0] = piece  
    if existed != None:
        undo_process[3] = existed
        for raw in piece_at_grid:
            for p in raw:
                if type(p) == King and p.team == "user":
                    user_king = p
                elif type(p) == King and p.team == "cpu":
                    cpu_king = p        
        if existed == cpu_king and piece.team == "user":
            cpu_king.alive = False
            winner = "user"
            
        elif existed.team == "cpu" and piece.team == "user":
            existed.alive = False
            
        if existed == user_king and piece.team == "cpu":
            user_king.alive = False
            winner = "cpu"
        elif existed.team == "user" and piece.team == "cpu":
            existed.alive = False

    if type(piece) == Pawn and abs(position[0]-to_raw) == 2:
        piece.first_move = False
        undo_process[5] = True
    if type(piece) == Pawn and to_raw == 0 and piece.team == "user":
        piece.alive = False
        piece = Queen(grid, (position[0], position[1]), user_color , "user")
        undo_process[4] = piece

    if type(piece) == Pawn and to_raw == 7 and piece.team == "cpu":
        piece.alive = False
        piece = Queen(grid, (position[0], position[1]), cpu_color, "cpu")
        undo_process[4] = piece

    undo_process[1] = position
    undo_process[2] = (to_raw, to_col)
    piece.move((to_raw,to_col))
    piece_at_grid[position[0]][position[1]] = None
    piece_at_grid[to_raw][to_col] = piece  

    return piece_at_grid, winner, undo_process 

def undo_move(piece_at_grid, undo_process):
    new_pos = undo_process[2]
    old_pos = undo_process[1]
    piece = undo_process[0]
    killed_piece = undo_process[3]
    promoted = undo_process[4]
    pawn_first_move = undo_process[5]

    if pawn_first_move != None:
        piece.first_move = True
    if killed_piece != None:
        killed_piece.alive = True
    if promoted != None:
        promoted.alive = False
        piece.alive = True
    piece_at_grid[new_pos[0]][new_pos[1]] = killed_piece
    piece_at_grid[old_pos[0]][old_pos[1]] = piece
    piece.move((old_pos[0],old_pos[1]))

    return piece, piece_at_grid


def select_piece(piece_at_grid):
    selected_piece = None
    allowed_movments, attack_range = [], []    
    selected = False
    while selected == False:
        mouse = pygame.mouse.get_pos() 
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                for raw in range(8):
                    for col in range(8):
                        block =  grid[raw][col]
                        if (block[0] <= mouse[0] <= block[0] + BlockSize) and (block[1] <= mouse[1] <= block[1] + BlockSize) and (piece_at_grid[raw][col].team == "user"):
                            selected_piece = piece_at_grid[raw][col]
                            allowed_movments, attack_range = get_possible_moves("user", selected_piece, piece_at_grid, raw, col ,True)
                            if len(allowed_movments) > 0:
                                selected = True  
                                screen.blit(select_border, (block[0],block[1]))
            pygame.display.update()    
    return selected_piece, allowed_movments, attack_range

def user_move(piece_at_grid):
    selected_piece, allowed_movments, attack_range = select_piece(piece_at_grid)     
    winner = None
    action = False
    while action == False:
        mouse = pygame.mouse.get_pos() 
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                for raw in range(8):
                    for col in range(8):
                        block =  grid[raw][col]
                        if (block[0] <= mouse[0] <= block[0] + BlockSize) and (block[1] <= mouse[1] <= block[1] + BlockSize) and ((raw, col) in allowed_movments):  
                            piece_at_grid, winner, undo_process = attempt_move(selected_piece, piece_at_grid, raw, col)
                            action = True
                        elif (block[0] <= mouse[0] <= block[0] + BlockSize) and (block[1] <= mouse[1] <= block[1] + BlockSize) and ((raw, col) not in allowed_movments):   
                            screen.blit(background, (0,0))
                            render_environment(piece_at_grid)                
                            selected_piece, allowed_movments, attack_range = select_piece(piece_at_grid)

    pygame.display.update() 
    return piece_at_grid, winner
    
def checkmate(piece_at_grid):
    user_checkmate, cpu_checkmate = None, None
    for raw in piece_at_grid:
        for p in raw:
            if p==None: continue
            position = p.get_location()
            allowed_movments, attack_range = get_possible_moves(p.team, p, piece_at_grid, position[0], position[1])
            for a in attack_range:
                i = piece_at_grid[a[0]][a[1]]
                if type(i) == King and i.team == "user":
                    user_checkmate = i
                elif type(i) == King and i.team == "cpu":
                    cpu_checkmate = i
    return user_checkmate, cpu_checkmate

def deepcopy(matrix):
    '''A function that I implemented to copy the entire grid with all pieces information
    for trying the legal moves without affecting the original chess board but later discarded
    the idea due to time-consuming and replaced it with an undo function'''
    new_matrix = []
    for raw in matrix:
        new_raw = []
        for element in raw:
            if element == None: 
                new_raw.append(None)
            else:
                new_raw.append(element.copy())
        new_matrix.append(new_raw)   
    return new_matrix

def cpu_move(piece_at_grid):
    best, best_move = N_ply_look_ahead(0, piece_at_grid, "cpu", -1000, 1000)
    piece = best_move[0]
    new_pos = best_move[1]
    piece_at_grid, winner, undo_process =  attempt_move(piece, piece_at_grid, new_pos[0], new_pos[1])
    return piece_at_grid, winner
    
    
def attack_range(piece_at_grid):
    user_in_attack_range, cpu_in_attack_range = [], []
    for raw in piece_at_grid:
        for p in raw:
            if p == None: continue
            position = p.get_location()
            if p.team == "user":
                allowed_movments, attack_range = get_possible_moves("user", p, piece_at_grid, position[0], position[1])
                cpu_in_attack_range += attack_range
            elif p.team == "cpu":
                allowed_movments, attack_range = get_possible_moves("cpu", p, piece_at_grid, position[0], position[1])
                user_in_attack_range += attack_range
    user_in_attack_range, cpu_in_attack_range = set(user_in_attack_range), set(cpu_in_attack_range)  
    return user_in_attack_range, cpu_in_attack_range

def heuristic(piece_at_grid):
    user_pieces = []
    cpu_pieces = []
    user_king = None
    cpu_king = None
    winner = None
    for raw in piece_at_grid:
        for p in raw:
            if type(p) == King and p.team == "user":
                user_king = p
            elif type(p) == King and p.team == "cpu":
                cpu_king = p
    if user_king == None:
        H = 10000
        winner = "cpu"
    elif cpu_king == None:
        H = -10000
        winner = "user"
    else:
        distance_to_cpu_king = distance_to_user_king = 0.0
        user_pawns_avg_distance_final = user_pawns_count = 0.0
        cpu_pawns_avg_distance_final  = cpu_pawns_count= 0
        user_queens_count = cpu_queens_count = 0
        for raw in piece_at_grid:
            for p in raw:
                if p != None and p.team == "user":
                    user_pieces.append(p)
                    distance_to_cpu_king += math.sqrt(math.pow((p.raw - cpu_king.raw),2) + math.pow((p.col - cpu_king.col),2))
                    if type(p) == Pawn:
                        user_pawns_avg_distance_final += (p.raw)
                        user_pawns_count += 1
                    elif type(p) == Queen:
                        user_queens_count += 1
                elif p != None and p.team == "cpu":
                    cpu_pieces.append(p)
                    distance_to_user_king += math.sqrt(math.pow((p.raw - user_king.raw),2) + math.pow((p.col - user_king.col),2))
                    if type(p) == Pawn:
                        cpu_pawns_avg_distance_final += (7-p.raw)
                        cpu_pawns_count += 1
                    elif type(p) == Queen:
                        cpu_queens_count += 1

        distance_to_cpu_king = distance_to_cpu_king / len(user_pieces)
        distance_to_user_king = distance_to_cpu_king / len(cpu_pieces)
        user_pieces_in_attack_range, cpu_pieces_in_attack_range = attack_range(piece_at_grid)
        user_king_in_attack_range = int(user_king.get_location() in user_pieces_in_attack_range)
        cpu_king_in_attack_range = int(cpu_king.get_location() in cpu_pieces_in_attack_range)
        user_pawns_avg_distance_final = user_pawns_avg_distance_final / user_pawns_count
        cpu_pawns_avg_distance_final = cpu_pawns_avg_distance_final / cpu_pawns_count
        maximize = 25*len(cpu_pieces) + 10*len(user_pieces_in_attack_range) + 5 * user_king_in_attack_range + distance_to_cpu_king + 5*cpu_queens_count + 2*user_pawns_avg_distance_final   
        minimize = 15*len(user_pieces) + 25* len(cpu_pieces_in_attack_range) + 40 * cpu_king_in_attack_range + 2*distance_to_user_king + 5*user_queens_count + 5*cpu_pawns_avg_distance_final
        H = maximize / minimize
    
    return H, winner

def N_ply_look_ahead(depth, piece_at_grid, turn, alpha, beta):

    if depth >= 3: return heuristic(piece_at_grid), []
    
    best_move = []
    winner = None
    brune = False
    if turn == "cpu":
        max_eval = -1000
        for raw in piece_at_grid:
            if brune : break
            for piece in raw:
                if brune : break
                if piece == None or piece.team == "user" : continue            
                position = piece.get_location()
                allowed_movments, attack_range = get_possible_moves("cpu", piece, piece_at_grid, position[0], position[1])
                if allowed_movments == [] : continue
                for to_raw, to_col in allowed_movments:

                    piece_at_grid, winner, undo_process =  attempt_move(piece, piece_at_grid, to_raw, to_col)
                    #Uncomment the below line in case you wanted to see how the algorithm tries all different legal moves
                    #render_environment(piece_at_grid)    
                    val = N_ply_look_ahead(depth+1, piece_at_grid, "user", alpha, beta)
                    piece, piece_at_grid = undo_move(piece_at_grid, undo_process)
                     
                    if val[0][0] >= max_eval:
                        max_eval = val[0][0]
                        winner = val[0][1]
                        best_move = [piece, (to_raw, to_col)]
                    alpha = max(alpha, max_eval)

                    if beta <= alpha or winner != None:
                        brune = True
                        break 
                    
        return (max_eval,winner), best_move

    else:
        min_eval = 1000
        for raw in piece_at_grid:
            if brune : break
            for piece in raw:
                if brune : break
                if piece == None or piece.team == "cpu" : continue
                position = piece.get_location()
                allowed_movments, attack_range = get_possible_moves("user", piece, piece_at_grid, position[0], position[1])
                if allowed_movments == [] : continue
                for to_raw, to_col in allowed_movments:
                    
                    piece_at_grid, winner, undo_process =  attempt_move(piece, piece_at_grid, to_raw, to_col)     
                    #Uncomment the below line in case you wanted to see how the algorithm tries all different legal moves
                    #render_environment(piece_at_grid) 
                    val = N_ply_look_ahead(depth+1, piece_at_grid, "cpu", alpha, beta)
                    piece, piece_at_grid = undo_move(piece_at_grid, undo_process)

                    if val[0][0] <= min_eval:
                        min_eval = val[0][0]
                        winner = val[0][1]
                        best_move = [piece, (to_raw, to_col)]                
                    beta = min(beta, min_eval)

                    if beta <= alpha or winner!= None:
                        brune = True
                        break    
                    
        return (min_eval,winner), best_move

def draw_pieces(piece_at_grid):
    for raw in piece_at_grid:
        for piece in raw:
            if piece != None:
                piece.draw(screen)
    
user_color, cpu_color = None, None
def initialize(piece_at_grid): 
    global user_color, cpu_color
    
    if user_color == "white" :
        user_color = "white"
        cpu_color = "black"
    else:
        user_color = "black"
        cpu_color = "white"        
        
    # Cloning objects for the user
    Pawn_user_1 = Pawn(grid, (6,0), user_color, "user")
    piece_at_grid[6][0] = Pawn_user_1
    Pawn_user_2 = Pawn(grid, (6,1), user_color, "user")
    piece_at_grid[6][1] = Pawn_user_2
    Pawn_user_3 = Pawn(grid, (6,2), user_color, "user")
    piece_at_grid[6][2] = Pawn_user_3
    Pawn_user_4 = Pawn(grid, (6,3), user_color, "user")
    piece_at_grid[6][3] = Pawn_user_4
    Pawn_user_5 = Pawn(grid, (6,4), user_color, "user")
    piece_at_grid[6][4] = Pawn_user_5
    Pawn_user_6 = Pawn(grid, (6,5), user_color, "user")
    piece_at_grid[6][5] = Pawn_user_6
    Pawn_user_7 = Pawn(grid, (6,6), user_color, "user")
    piece_at_grid[6][6] = Pawn_user_7
    Pawn_user_8 = Pawn(grid, (6,7), user_color, "user")
    piece_at_grid[6][7] = Pawn_user_8
    Rook_user_1 = Rook(grid, (7,0), user_color, "user")
    piece_at_grid[7][0] = Rook_user_1  
    Knight_user_1 = Knight(grid, (7,1), user_color, "user")
    piece_at_grid[7][1] = Knight_user_1   
    Bishop_user_1 = Bishop(grid, (7,2), user_color, "user")
    piece_at_grid[7][2] = Bishop_user_1   
    King_user = King(grid, (7,3), user_color, "user")    
    piece_at_grid[7][3] = King_user  
    Queen_user = Queen(grid, (7,4), user_color, "user")
    piece_at_grid[7][4] = Queen_user 
    Bishop_user_2 = Bishop(grid, (7,5), user_color, "user")
    piece_at_grid[7][5] = Bishop_user_2  
    Knight_user_2 = Knight(grid, (7,6), user_color, "user")
    piece_at_grid[7][6] = Knight_user_2 
    Rook_user_2 = Rook(grid, (7,7), user_color, "user")
    piece_at_grid[7][7] = Rook_user_2  

    
    # Cloning objects for the cpu
    Pawn_cpu_1 = Pawn(grid, (1,0), cpu_color, "cpu")
    piece_at_grid[1][0] = Pawn_cpu_1
    Pawn_cpu_2 = Pawn(grid, (1,1), cpu_color, "cpu")
    piece_at_grid[1][1] = Pawn_cpu_2
    Pawn_cpu_3 = Pawn(grid, (1,2), cpu_color, "cpu")
    piece_at_grid[1][2] = Pawn_cpu_3
    Pawn_cpu_4 = Pawn(grid, (1,3), cpu_color, "cpu")
    piece_at_grid[1][3] = Pawn_cpu_4
    Pawn_cpu_5 = Pawn(grid, (1,4), cpu_color, "cpu")
    piece_at_grid[1][4] = Pawn_cpu_5
    Pawn_cpu_6 = Pawn(grid, (1,5), cpu_color, "cpu")
    piece_at_grid[1][5] = Pawn_cpu_6
    Pawn_cpu_7 = Pawn(grid, (1,6), cpu_color, "cpu")
    piece_at_grid[1][6] = Pawn_cpu_7
    Pawn_cpu_8 = Pawn(grid, (1,7), cpu_color, "cpu")
    piece_at_grid[1][7] = Pawn_cpu_8
    Rook_cpu_1 = Rook(grid, (0,0), cpu_color, "cpu")
    piece_at_grid[0][0] = Rook_cpu_1  
    Knight_cpu_1 = Knight(grid, (0,1), cpu_color, "cpu")
    piece_at_grid[0][1] = Knight_cpu_1     
    Bishop_cpu_1 = Bishop(grid, (0,2), cpu_color, "cpu")
    piece_at_grid[0][2] = Bishop_cpu_1  
    Queen_cpu = Queen(grid, (0,3), cpu_color, "cpu")
    piece_at_grid[0][3] = Queen_cpu  
    King_cpu = King(grid, (0,4), cpu_color, "cpu")    
    piece_at_grid[0][4] = King_cpu 
    Bishop_cpu_2 = Bishop(grid, (0,5), cpu_color, "cpu")
    piece_at_grid[0][5] = Bishop_cpu_2 
    Knight_cpu_2 = Knight(grid, (0,6), cpu_color, "cpu")
    piece_at_grid[0][6] = Knight_cpu_2 
    Rook_cpu_2 = Rook(grid, (0,7), cpu_color, "cpu")
    piece_at_grid[0][7] = Rook_cpu_2 
    
    return piece_at_grid