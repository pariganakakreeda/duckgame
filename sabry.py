import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
#wood_bg = pygame.image.load('sky.jpg')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
i=0
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


    screen.blit(wood_bg,(0,0))
    screen.blit(land_bg,(0,560))
    screen.blit(water_bg,(i,600))
    i=i+1
    pygame.display.update()
    clock.tick(120)
