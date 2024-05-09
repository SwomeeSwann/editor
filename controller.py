import pygame


class Player():
    def __init__(self, surface ,pos, size, color) -> None:
        self.surface = surface
        self.pos = pos
        self.size = size
        self.color = color
        pass
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.size)