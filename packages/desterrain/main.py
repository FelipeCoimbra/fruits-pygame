import pygame

#Usual pygame stuff
pygame.init()
display = pygame.display.set_mode((320, 240))

#Import images
background = pygame.image.load("back.png")
destructable = pygame.image.load("front.png")
destructable.set_alpha() #Ensure that the surface won't use alpha
destructable.set_colorkey((255,0,255)) #But rather a colorkey

#Main
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    if pygame.mouse.get_pressed()[0]:
        #Make a portion of the ground invisible
        pygame.draw.circle(destructable, (255, 0, 255), pygame.mouse.get_pos(), 5)
    
    display.blit(background, (0, 0))
    display.blit(destructable, (0, 0))
    pygame.display.flip()
