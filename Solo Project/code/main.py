import pygame, sys
from settings import *
from level import Level
from pygame.locals import *
from player import Player
import button

class Game:

    def __init__(self): 
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Solo')
        self.clock = pygame.time.Clock()
        
        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('audio/shovel.mp3')
        main_sound.set_volume(0.05)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()


            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
    
            
if __name__ == '__main__':
    pygame.init()
    sound_enger = pygame.mixer.Sound('audio/soundzelda.webm')
    sound_enger.set_volume(0.2)
    sound_enger.play(loops = -1)
    # pygame.init()

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

    start_button = button.Button(495, 550, start_img, 0.8)

    dead=False

    clock = pygame.time.Clock()
    background_image = pygame.image.load("graphics/napook.png").convert()


    while(dead==False):



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
        if start_button.draw(background_image):
                    game = Game()
                    game.run()
        
        screen.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(clock_tick_rate)
