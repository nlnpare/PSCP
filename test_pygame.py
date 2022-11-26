import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #width = กว้าง , hight = ยาว
pygame.display.set_caption('songdaisavogue')
clock = pygame.time.Clock() #ตัวแปรการตั้งเวลา

sky_surface = pygame.image.load('project/graphics/Sky.png')
ground_surface = pygame.image.load('project/graphics/ground.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    
    screen.blit(ground_surface, (0,300))
    screen.blit(sky_surface, (0,0)) #แสดงรูป
    
    pygame.display.update() #update line 4
    clock.tick(60) #จะไม่ทำงานเกิน 60 ครั้งต่อวินาที