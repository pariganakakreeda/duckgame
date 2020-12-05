import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
#wood_bg = pygame.image.load('sky.jpg')
#land_bg = pygame.image.load('Land_BG.png')
grass_bg = pygame.image.load('grass.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('Cloud1.png')
cloud2 = pygame.image.load('Cloud2.png')
#bird_bg = pygame.image.load('bird.png')

while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


    screen.blit(wood_bg,(0,0))
   # screen.blit(land_bg,(0,560))
    screen.blit(grass_bg,(0,360))
   # screen.blit(water_bg,(0,640))
    screen.blit(cloud1,(10,10))
    #screen.blit(bird_bg,(15,110))
    pygame.display.update()
    clock.tick(120)
