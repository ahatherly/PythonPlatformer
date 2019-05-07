import pygame

class Sounds:

    sound_objects = {}

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        self.sound_objects['jump'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_jump4.wav")
        self.sound_objects['land'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_jump9_landing.wav")
        self.sound_objects['dead'] = pygame.mixer.Sound("./Assets/Sounds/sfx_deathscream_robot2.wav")

        self.sound_objects['walk'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_footsteps1a.wav")
        self.sound_objects['walk'].set_volume(0.2)

    def jump(self):
        self.sound_objects['jump'].play()
    def land(self):
        self.sound_objects['land'].play()
    def dead(self):
        self.sound_objects['dead'].play()
    def walk(self):
        #self.sound_objects['walk'].play()
        pass