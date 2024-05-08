import pygame
import random

class Circle():
    def __init__(self, pos, color, name) -> None:
        self.color = color
        self.pos = pos
        self.name = name
        pass
        

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
run = True

names = ["Dale", "Mahogany", "Bruh", "Cool"]
circles = []
hovered = []

font = pygame.font.Font(None, 80)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        circle = Circle(pygame.Vector2(random.randint(850, 1280), random.randint(0, 720)), "blue", names[random.randint(0, len(names) - 1)])
        circles.append(circle)
            
    screen.fill("black")
    
    pygame.draw.rect(screen, "gray", pygame.Rect(0, 0, 800, 720))
    
    for circle in circles:
        pygame.draw.circle(screen, circle.color, circle.pos, 40)
        if abs(mouse_pos[0] - circle.pos.x) < 25 and abs(mouse_pos[1] - circle.pos.y) < 25:
            
            text_surface = font.render(str(circle.pos) + ", " + str(circle.name), False, (255, 255, 255))
            
            if not circle in hovered:
                hovered.append(circle)
            screen.blit(text_surface, (25, 25 + (75 * hovered.index(circle))))
        else:
            if circle in hovered:
                hovered.pop(hovered.index(circle))
    
    

                
    
    pygame.display.flip()


            

pygame.quit()
