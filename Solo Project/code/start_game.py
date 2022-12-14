import pygame
import button
from main import Game
# initialize game engine
pygame.init()

window_width=1280
window_height=720

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello World")

start_img = pygame.image.load('graphics/start_btn.png').convert_alpha()
exit_img = pygame.image.load('graphics/exit_btn.png').convert_alpha()

start_button = button.Button(400, 200, start_img, 0.8)
exit_button = button.Button(720, 200, exit_img, 0.8)

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("graphics/napook.png").convert()


while(dead==False):



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
    if start_button.draw(screen):
                game = Game()
                game.run()
    if exit_button.draw(screen):
                exit()
    
    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)