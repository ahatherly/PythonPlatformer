import pygame

class Sounds:

    sound_objects = {}

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        self.sound_objects['jump'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_jump4.wav")
        self.sound_objects['land'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_jump9_landing.wav")
        self.sound_objects['dead'] = pygame.mixer.Sound("./Assets/Sounds/sfx_deathscream_robot2.wav")
        self.sound_objects['damage'] = pygame.mixer.Sound("./Assets/Sounds/sfx_sounds_damage3.wav")
        self.sound_objects['key'] = pygame.mixer.Sound("./Assets/Sounds/sfx_sounds_powerup3.wav")
        self.sound_objects['unlock'] = pygame.mixer.Sound("./Assets/Sounds/sfx_sounds_interaction6.wav")

        self.sound_objects['gameover'] = pygame.mixer.Sound("./Assets/Sounds/sfx_sound_mechanicalnoise2.wav")
        self.sound_objects['won'] = pygame.mixer.Sound("./Assets/Sounds/sfx_sound_poweron.wav")

        self.sound_objects['walk'] = pygame.mixer.Sound("./Assets/Sounds/sfx_movement_footsteps1a.wav")
        self.sound_objects['walk'].set_volume(0.2)

    def jump(self):
        self.sound_objects['jump'].play()
    def land(self):
        self.sound_objects['land'].play()
    def dead(self):
        self.sound_objects['dead'].play()
    def damage(self):
        self.sound_objects['damage'].play()
    def walk(self):
        #self.sound_objects['walk'].play()
        pass
    def key(self):
        self.sound_objects['key'].play()
    def unlock(self):
        self.sound_objects['unlock'].play()
    def gameover(self):
        self.sound_objects['gameover'].play()
    def won(self):
        self.sound_objects['won'].play()