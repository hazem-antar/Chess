import pygame, copy

BlockSize = 72

class Pawn(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        super().__init__() 
        self.color = color
        if color == "black":
            self.image = pygame.image.load('BPawn.png')
        else:
            self.image = pygame.image.load('WPawn.png')            
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]           
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.first_move = True
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
    
    def get_location(self):
        return(self.raw, self.col)
    
    def copy(self):
        copyobj = Pawn(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj

class Knight(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        super().__init__() 
        self.color = color
        if color == "black":
            self.image = pygame.image.load('BKnight.png')
        else:
            self.image = pygame.image.load('WKnight.png')         
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
            
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
    
    def get_location(self):
        return(self.raw, self.col)
    
    def copy(self):
        copyobj = Knight(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj
    
class Rook(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        super().__init__() 
        self.color = color
        if color == "black":
            self.image = pygame.image.load('BRook.png')
        else:
            self.image = pygame.image.load('WRook.png')        
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
            
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            
    def get_location(self):
        return(self.raw, self.col)    
    
    def copy(self):
        copyobj = Rook(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj
    
class Bishop(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        super().__init__() 
        self.color = color
        if color == "black":
            self.image = pygame.image.load('BBishop.png')
        else:
            self.image = pygame.image.load('WBishop.png')
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
            
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)   
    
    def get_location(self):
        return(self.raw, self.col) 
    
    def copy(self):
        copyobj = Bishop(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj
    
class Queen(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        self.color = color
        super().__init__() 
        if color == "black":
            self.image = pygame.image.load('BQueen.png')
        else:
            self.image = pygame.image.load('WQueen.png')
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
            
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect) 
    
    def get_location(self):
        return(self.raw, self.col)     
    
    def copy(self):
        copyobj = Queen(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj
    
class King(pygame.sprite.Sprite):
    def __init__(self, grid, position, color, team):
        super().__init__() 
        self.color = color
        if color == "black":
            self.image = pygame.image.load('BKing.png')
        else:
            self.image = pygame.image.load('WKing.png')
        self.image = pygame.transform.scale(self.image, (BlockSize, BlockSize))   
        self.rect = self.image.get_rect()
        self.grid = grid
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
        self.alive = True
        self.team = team
        
    def move(self, position):
        self.raw = position[0]
        self.col = position[1]          
        self.rect.x = self.grid[self.raw][self.col][0]
        self.rect.y = self.grid[self.raw][self.col][1]
            
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
        
    def get_location(self):
        return(self.raw, self.col)     
    
    def copy(self):
        copyobj = King(self.grid, (self.raw, self.col), self.color, self.team)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copyobj.__dict__[name] = attr.copy()
            else:
                copyobj.__dict__[name] = copy.deepcopy(attr)
        return copyobj    
