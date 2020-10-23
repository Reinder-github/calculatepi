import random
import math
import pygame

def test(aantal):
    aantalbinnencirkel = 0
    aantaltotaal = 0
    global screen
    for x in range (aantal):
        xrand1 = random.uniform(0,500)
        yrand2 = random.uniform(0,500)
        afstand = math.sqrt((xrand1-250)**2+(yrand2-250)**2)
        if afstand <= 250:
            aantalbinnencirkel += 1
            pygame.draw.circle(screen, (255,0,0), (int(xrand1),int(yrand2)),(1))
        else:
            pygame.draw.circle(screen, (0,255,0), (int(xrand1),int(yrand2)), (1))
        pygame.display.update()
        aantaltotaal += 1
    verhouding = 4 * aantalbinnencirkel / aantaltotaal
    print (verhouding)
    return verhouding

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))    
pygame.draw.circle(screen, (255,0,0), (250,250), (250), (1))
pygame.display.flip()


resultaat = test(10000)
font = pygame.font.Font('freesansbold.ttf', 32)  
text = font.render('Pi is ' + str(resultaat), True, (255,255,255), (145,135,135)) 
textRect = text.get_rect()  
textRect.center = (250, 250)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.blit(text, textRect) 
        pygame.display.update()  
