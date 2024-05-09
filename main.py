import pygame
import random
import controller

class Circle():
    def __init__(self, pos, color, name) -> None:
        self.color = color
        self.pos = pos
        self.name = name
        pass
        
class Button():
    def __init__(self, pos, length, width, color) -> None:
        self.pos = pos
        self.length = length
        self.width = width
        self.color = color
        pass

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos[0], self.pos[1], self.length, self.width))


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
run = True
mode = "view"

colors = ["red", "green", "blue"]
names = ["Dale", "Mahogany", "Bruh", "Cool", "Bob", "Joe"]
circles = []
color_buttons = []
editor_buttons = []
hovered = []

font = pygame.font.Font(None, 80)
circle_color = "blue"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "view":
                for circle in circles:
                    if abs(mouse_pos[0] - circle.pos.x) < 25 and abs(mouse_pos[1] - circle.pos.y) < 25:
                        circles.pop(circles.index(circle))
                        circles = circles[:1] + circles[1:]
                        if circle in hovered:
                            hovered.pop(hovered.index(circle))
                            hovered = hovered[:1] + hovered[1:]
            elif mode == "edit":
                for button in color_buttons:
                    if abs(mouse_pos[0] - button.pos[0]) < 75 and abs(mouse_pos[1] - button.pos[1]) < 75:
                        for circle in circles:
                            circle_color = button.color
                
                for button in editor_buttons:
                    if abs(mouse_pos[0] - button.pos[0]) < 75 and abs(mouse_pos[1] - button.pos[1]) < 75:
                        



    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
            
    screen.fill("black")
    
    if keys[pygame.K_0]:
        mode = "view"
    if keys[pygame.K_1]:
        mode = "edit"
    if keys[pygame.K_9]:
        circles.clear()
    
    if mode == "view":
        if keys[pygame.K_SPACE]: 
            circle = Circle(pygame.Vector2(random.randint(850, 1280), random.randint(0, 720)), circle_color, names[random.randint(0, len(names) - 1)])
            circles.append(circle)
        
        pygame.draw.rect(screen, "gray", pygame.Rect(0, 0, 800, 720))
        
        for circle in circles:
            if abs(mouse_pos[0] - circle.pos.x) < 25 and abs(mouse_pos[1] - circle.pos.y) < 25:

                pygame.draw.circle(screen, "white", circle.pos, 45)

                text_surface = font.render(str(circle.pos) + ", " + str(circle.name) + ", " + circle.color, False, (255, 255, 255))
                if not circle in hovered:
                    hovered.append(circle)
                screen.blit(text_surface, (25, 25 + (75 * hovered.index(circle))))
            else:
                if circle in hovered:
                    hovered.pop(hovered.index(circle))
            
            pygame.draw.circle(screen, circle.color, circle.pos, 40)
    elif mode == "edit":
        buttons = color_buttons + editor_buttons
        
        if not color_buttons and not editor_buttons:
            button = Button((50, 200), 75, 75, "gray")
            editor_buttons.append(button)
            
            for i in range(0, 3):
                pos = [20 + (i * 150), 30]
                button = Button(pos, 75, 75, colors[i])
                color_buttons.append(button)
            
        for button in buttons:
            button.draw()
        
        color_text = font.render("Colors", False, (255,255,255))
        screen.blit(color_text, (20, 150))
        
        
                
    
    pygame.display.flip()


            

pygame.quit()
