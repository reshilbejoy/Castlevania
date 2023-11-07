import pygame

class Grid:
    def __init__(self):
        self.length = 12
        self.height = 16
        self.row = ['' for i in range(self.length)]
        self.grid = [self.row for i in range(self.height)]
    def grid_return(self):
        return self.grid